import json
import os
import re
from typing import Any, Dict, List, Optional

import requests


def _fallback_suggestions() -> List[str]:
    return [
        "Add 2–3 bullet points that explicitly mention the missing skills.",
        "Quantify impact for matched skills (metrics, outcomes, scale).",
        "Mirror key job description phrases in your experience section.",
    ]


def _build_prompt(matched_skills: List[str], missing_skills: List[str]) -> str:
    return (
        "You are a resume coach. Provide 3 to 5 specific, actionable suggestions "
        "to improve the resume for the given job. Return ONLY a JSON array of strings.\n\n"
        f"Matched skills: {', '.join(matched_skills) if matched_skills else 'None'}\n"
        f"Missing skills: {', '.join(missing_skills) if missing_skills else 'None'}\n"
    )


def _parse_suggestions(text: str) -> List[str]:
    if not text:
        return []

    # Try to parse a JSON array from the response.
    try:
        data = json.loads(text)
        if isinstance(data, list):
            return [str(item).strip() for item in data if str(item).strip()]
        if isinstance(data, dict) and "suggestions" in data:
            return [str(item).strip() for item in data["suggestions"] if str(item).strip()]
    except json.JSONDecodeError:
        pass

    # Try to extract JSON array embedded in text.
    match = re.search(r"\[[\s\S]*\]", text)
    if match:
        try:
            data = json.loads(match.group(0))
            if isinstance(data, list):
                return [str(item).strip() for item in data if str(item).strip()]
        except json.JSONDecodeError:
            pass

    # Fallback: split lines or numbered bullets.
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    cleaned = []
    for line in lines:
        cleaned.append(re.sub(r"^\d+[\).\s-]+", "", line).strip())
    return [item for item in cleaned if item]


def _parse_json_object(text: str) -> Optional[Dict[str, Any]]:
    if not text:
        return None

    try:
        data = json.loads(text)
        if isinstance(data, dict):
            return data
    except json.JSONDecodeError:
        pass

    match = re.search(r"\{[\s\S]*\}", text)
    if match:
        try:
            data = json.loads(match.group(0))
            if isinstance(data, dict):
                return data
        except json.JSONDecodeError:
            return None

    return None


def _call_gemini(prompt: str, api_key: str) -> List[str]:
    model = os.getenv("AI_MODEL", "").strip() or "gemini-2.5-flash"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    headers = {"Content-Type": "application/json", "x-goog-api-key": api_key}
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.4, "maxOutputTokens": 256},
    }

    response = requests.post(url, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
    data = response.json()

    text = ""
    try:
        text = data["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError, TypeError):
        text = ""
    return _parse_suggestions(text)


def _call_openai(prompt: str, api_key: str) -> List[str]:
    model = os.getenv("AI_MODEL", "").strip() or "gpt-4o-mini"
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    payload = {
        "model": model,
        "temperature": 0.4,
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant that follows formatting exactly.",
            },
            {"role": "user", "content": prompt},
        ],
    }

    response = requests.post(url, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
    data = response.json()

    text = ""
    try:
        text = data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError):
        text = ""
    return _parse_suggestions(text)


def _call_openai_json(prompt: str, api_key: str) -> Optional[Dict[str, Any]]:
    model = os.getenv("AI_MODEL", "").strip() or "gpt-4o-mini"
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    payload = {
        "model": model,
        "temperature": 0.2,
        "response_format": {"type": "json_object"},
        "messages": [
            {
                "role": "system",
                "content": "You return strictly valid JSON with no extra text.",
            },
            {"role": "user", "content": prompt},
        ],
    }

    response = requests.post(url, headers=headers, json=payload, timeout=45)
    response.raise_for_status()
    data = response.json()

    text = ""
    try:
        text = data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError):
        text = ""
    return _parse_json_object(text)


def _call_gemini_json(prompt: str, api_key: str) -> Optional[Dict[str, Any]]:
    model = os.getenv("AI_MODEL", "").strip() or "gemini-2.5-flash"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    headers = {"Content-Type": "application/json", "x-goog-api-key": api_key}
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.2, "maxOutputTokens": 512},
    }

    response = requests.post(url, headers=headers, json=payload, timeout=45)
    response.raise_for_status()
    data = response.json()

    text = ""
    try:
        text = data["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError, TypeError):
        text = ""
    return _parse_json_object(text)


def generate_ai_analysis(
    resume_text: str, job_description: str
) -> tuple[Optional[Dict[str, Any]], Optional[str]]:
    api_key = os.getenv("AI_API_KEY", "").strip()
    provider = os.getenv("AI_PROVIDER", "gemini").strip().lower()

    if not api_key:
        return None, "missing_api_key"

    prompt = (
        "You are an Applicant Tracking System (ATS) resume analyzer.\n\n"
        "Analyze the resume against the job description and provide an ATS-style "
        "evaluation similar to professional resume scanners.\n\n"
        "Evaluate the following aspects:\n"
        "1. Tone & Style\n"
        "2. Content relevance\n"
        "3. Resume Structure\n"
        "4. Skills match\n\n"
        "Return the analysis strictly in JSON format.\n\n"
        "Scoring rules:\n"
        "- Each category should have a score from 0–100.\n"
        "- Provide matched skills found in both resume and job description.\n"
        "- Provide missing skills from the job description that are not found in the resume.\n"
        "- Provide clear suggestions to improve the resume for ATS systems.\n\n"
        f"Resume Text:\n{resume_text}\n\n"
        f"Job Description:\n{job_description}\n\n"
        "Return JSON in this format:\n"
        "{\n"
        '  "ats_score": number,\n'
        '  "tone_style_score": number,\n'
        '  "content_score": number,\n'
        '  "structure_score": number,\n'
        '  "skills_score": number,\n'
        '  "matched_skills": [],\n'
        '  "missing_skills": [],\n'
        '  "suggestions": ["string"]\n'
        "}\n"
    )

    try:
        if provider == "openai":
            return _call_openai_json(prompt, api_key), None
        return _call_gemini_json(prompt, api_key), None
    except Exception as exc:
        return None, str(exc)


def generate_suggestions(matched_skills, missing_skills):
    api_key = os.getenv("AI_API_KEY", "").strip()
    provider = os.getenv("AI_PROVIDER", "gemini").strip().lower()

    if not api_key:
        return _fallback_suggestions()

    prompt = _build_prompt(matched_skills, missing_skills)

    try:
        if provider == "openai":
            suggestions = _call_openai(prompt, api_key)
        else:
            suggestions = _call_gemini(prompt, api_key)
    except Exception:
        return _fallback_suggestions()

    return suggestions if suggestions else _fallback_suggestions()
