import io
import os
import re
import urllib.request
import base64
from typing import Optional
from uuid import UUID

import pdfplumber

try:
    import spacy
except Exception:
    spacy = None
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, HttpUrl

from ai_suggestions import generate_ai_analysis, generate_suggestions
from skills import extract_known_skills, role_skill_set, role_suggestions
from supabase_client import get_supabase_client

app = FastAPI(title="Smart Resume Analyzer API")

load_dotenv()

allowed_origins = [
    os.getenv("FRONTEND_ORIGIN", "").strip(),
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
allowed_origins = [origin for origin in allowed_origins if origin]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health check endpoint for testing
@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "Backend is running and ready",
        "endpoint": "POST /analyze",
        "gemini_key_set": bool(os.getenv("AI_API_KEY", "").strip()),
    }


class AnalyzeRequest(BaseModel):
    resume_url: HttpUrl | None = None
    job_description: str
    resume_text: str | None = None
    resume_file: str | None = None
    resume_id: Optional[UUID] = None


def load_spacy_model():
    if spacy is None:
        return None
    try:
        return spacy.load("en_core_web_sm")
    except Exception:
        return None


NLP = load_spacy_model()

FALLBACK_STOPWORDS = {
    "a",
    "an",
    "the",
    "and",
    "or",
    "but",
    "if",
    "to",
    "of",
    "in",
    "for",
    "on",
    "with",
    "by",
    "is",
    "are",
    "was",
    "were",
    "be",
    "been",
    "as",
    "at",
    "from",
    "that",
    "this",
    "it",
    "we",
    "you",
    "your",
    "our",
    "they",
    "their",
    "i",
    "me",
    "my",
}


def download_pdf(url: str) -> bytes:
    try:
        with urllib.request.urlopen(url, timeout=20) as response:
            return response.read()
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Failed to download PDF: {exc}") from exc


def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    try:
        with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
            pages = [page.extract_text() or "" for page in pdf.pages]
        return "\n".join(pages)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=f"Failed to parse PDF: {exc}") from exc


def normalize_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_keywords(text: str) -> set[str]:
    if NLP is not None:
        doc = NLP(text)
        keywords = {
            token.lemma_.lower()
            for token in doc
            if token.is_alpha
            and not token.is_stop
            and token.pos_ in {"NOUN", "PROPN", "ADJ"}
        }
        return {k for k in keywords if len(k) > 1}

    # Fallback tokenizer for environments where spaCy isn't available
    tokens = re.findall(r"[a-zA-Z][a-zA-Z0-9+\-#]*", text.lower())
    keywords = {token for token in tokens if token not in FALLBACK_STOPWORDS}
    keywords = {k for k in keywords if len(k) > 1}

    known_skills = extract_known_skills(text)
    return keywords | known_skills


def calculate_ats_score(job_keywords: set[str], resume_keywords: set[str]) -> int:
    if not job_keywords:
        return 0
    matched = job_keywords & resume_keywords
    score = int(round(len(matched) / len(job_keywords) * 100))
    return max(0, min(score, 100))


def clamp_score(value: int) -> int:
    return max(0, min(int(value), 100))


def compute_structure_score(resume_text: str) -> int:
    headings = [
        "summary",
        "skills",
        "projects",
        "experience",
        "work experience",
        "education",
        "certifications",
    ]
    count = 0
    for heading in headings:
        if re.search(rf"\b{re.escape(heading)}\b", resume_text, re.I):
            count += 1
    if count == 0:
        words = re.findall(r"[A-Za-z0-9']+", resume_text)
        return 35 if len(words) > 50 else 25
    return clamp_score(round(min(count / 5, 1) * 100))


def compute_tone_style_score(resume_text: str) -> int:
    sentences = [s for s in re.split(r"[.!?]+", resume_text) if s.strip()]
    lines = [s for s in re.split(r"[\n\r]+", resume_text) if s.strip()]
    chunks = sentences if len(sentences) >= 2 else lines
    if not chunks:
        return 50
    total_words = sum(len(re.findall(r"[A-Za-z0-9']+", s)) for s in chunks)
    avg_words = total_words / max(len(chunks), 1)
    score = 80 - abs(avg_words - 16) * 3
    return clamp_score(round(score))


def compute_content_score(job_keywords: set[str], resume_keywords: set[str]) -> int:
    if not job_keywords:
        return 0
    matched = job_keywords & resume_keywords
    return clamp_score(round(len(matched) / len(job_keywords) * 100))


def compute_skills_score(
    job_skills: set[str],
    resume_skills: set[str],
    job_keywords: set[str],
    resume_keywords: set[str],
) -> int:
    if job_skills:
        matched = job_skills & resume_skills
        return clamp_score(round(len(matched) / len(job_skills) * 100))
    if job_keywords:
        matched = job_keywords & resume_keywords
        return clamp_score(round(len(matched) / len(job_keywords) * 100))
    return 0


def compute_weighted_ats(
    tone_score: int, content_score: int, structure_score: int, skills_score: int
) -> int:
    weighted = (
        0.1 * tone_score
        + 0.3 * content_score
        + 0.2 * structure_score
        + 0.4 * skills_score
    )
    return clamp_score(round(weighted))


def safe_list(value) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    return []


def safe_score(value, fallback: int) -> int:
    try:
        return clamp_score(int(value))
    except (TypeError, ValueError):
        return fallback


@app.post("/analyze")
def analyze(payload: AnalyzeRequest):
    if not payload.job_description.strip():
        raise HTTPException(status_code=400, detail="job_description is required")

    resume_text = normalize_text(payload.resume_text or "")

    # Handle base64 encoded PDF file
    if not resume_text and payload.resume_file:
        try:
            # Decode base64 to PDF bytes
            pdf_bytes = base64.b64decode(payload.resume_file)
            resume_text = normalize_text(extract_text_from_pdf(pdf_bytes))
            if not resume_text:
                raise HTTPException(
                    status_code=400, detail="Resume text could not be extracted from PDF"
                )
        except Exception as exc:
            raise HTTPException(
                status_code=400, detail=f"Failed to process PDF file: {str(exc)}"
            )

    if not resume_text:
        if not payload.resume_url:
            raise HTTPException(
                status_code=400, detail="Please upload a PDF, paste text, or provide a resume URL"
            )
        pdf_bytes = download_pdf(str(payload.resume_url))
        resume_text = normalize_text(extract_text_from_pdf(pdf_bytes))
        if not resume_text:
            raise HTTPException(
                status_code=400, detail="Resume text could not be extracted"
            )

    job_text = normalize_text(payload.job_description)

    job_keywords = extract_keywords(job_text)
    resume_keywords = extract_keywords(resume_text)
    role_skills = role_skill_set(job_text)
    allowed_skills = role_skills if role_skills else None
    job_skill_set = extract_known_skills(job_text, allowed_skills)
    resume_skill_set = extract_known_skills(resume_text, allowed_skills)

    matched = sorted(job_keywords & resume_keywords)
    missing = sorted(job_keywords - resume_keywords)
    ats_score = calculate_ats_score(job_keywords, resume_keywords)

    ai_analysis, ai_error = generate_ai_analysis(resume_text, job_text)
    ai_used = ai_analysis is not None
    if ai_used:
        matched = safe_list(ai_analysis.get("matched_skills")) or matched
        missing = safe_list(ai_analysis.get("missing_skills")) or missing
        ats_score = safe_score(ai_analysis.get("ats_score"), ats_score)
    elif job_skill_set:
        matched = sorted(job_skill_set & resume_skill_set)
        missing = sorted(job_skill_set - resume_skill_set)

    if role_skills:
        matched = [skill for skill in matched if skill in role_skills]
        missing = [skill for skill in missing if skill in role_skills]
        if not matched and not missing and job_skill_set:
            matched = sorted(job_skill_set & resume_skill_set)
            missing = sorted(job_skill_set - resume_skill_set)

    suggestions_list = generate_suggestions(matched, missing)
    if ai_used:
        ai_suggestions = safe_list(ai_analysis.get("suggestions"))
        if ai_suggestions:
            suggestions_list = ai_suggestions
    else:
        role_based = role_suggestions(job_text)
        if role_based:
            suggestions_list = role_based
    suggestions_text = "\n".join(
        f"{index + 1}. {item}" for index, item in enumerate(suggestions_list)
    )

    fallback_tone = compute_tone_style_score(resume_text)
    fallback_content = compute_content_score(job_keywords, resume_keywords)
    fallback_structure = compute_structure_score(resume_text)
    fallback_skills = compute_skills_score(
        job_skill_set, resume_skill_set, job_keywords, resume_keywords
    )

    tone_style_score = safe_score(
        ai_analysis.get("tone_style_score") if ai_used else None, fallback_tone
    )
    content_score = safe_score(
        ai_analysis.get("content_score") if ai_used else None, fallback_content
    )
    structure_score = safe_score(
        ai_analysis.get("structure_score") if ai_used else None, fallback_structure
    )
    skills_score = safe_score(
        ai_analysis.get("skills_score") if ai_used else None, fallback_skills
    )

    ats_score = compute_weighted_ats(
        tone_style_score, content_score, structure_score, skills_score
    )

    stored = False
    storage_error = None
    if payload.resume_id:
        client = get_supabase_client()
        if client:
            try:
                client.table("resumes").update({"ats_score": ats_score}).eq(
                    "id", str(payload.resume_id)
                ).execute()
                client.table("analysis").insert(
                    {
                        "resume_id": str(payload.resume_id),
                        "ats_score": ats_score,
                        "tone_style_score": tone_style_score,
                        "content_score": content_score,
                        "structure_score": structure_score,
                        "skills_score": skills_score,
                        "matched_skills": matched,
                        "missing_skills": missing,
                        "suggestions": suggestions_text,
                    }
                ).execute()
                stored = True
            except Exception as exc:
                storage_error = str(exc)

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "ats_score": ats_score,
        "tone_style_score": tone_style_score,
        "content_score": content_score,
        "structure_score": structure_score,
        "skills_score": skills_score,
        "ai_used": ai_used,
        "ai_error": ai_error,
        "suggestions": suggestions_list,
        "stored": stored,
        "storage_error": storage_error,
    }
