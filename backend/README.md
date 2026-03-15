# Backend (FastAPI) — Smart Resume Analyzer

## What This Service Does
- Accepts a resume PDF URL and job description
- Extracts resume text with `pdfplumber`
- Extracts keywords with `spaCy`
- Calculates an ATS match score
- Optionally stores analysis in Supabase if `resume_id` is provided and env vars are set

## Setup
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Run
```bash
uvicorn main:app --reload
```

## Test
```bash
curl -X POST http://127.0.0.1:8000/analyze ^
  -H "Content-Type: application/json" ^
  -d "{\"resume_url\":\"<SIGNED_PDF_URL>\",\"job_description\":\"<TEXT>\",\"resume_id\":\"<UUID>\"}"
```

## Environment
Copy `backend/.env.example` to `backend/.env` if you plan to add AI suggestions.
