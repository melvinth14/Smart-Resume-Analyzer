# Smart Resume Analyzer

Full-stack resume analyzer that scores ATS fit, extracts matched/missing skills, and generates role-aware suggestions. Built with Next.js, FastAPI, and Supabase.

## Live Demo
- Vercel: https://YOUR-VERCEL-URL

## Features
- Resume upload (PDF) or paste resume text
- Job description matching with ATS score
- Category scores: Tone & Style, Content, Structure, Skills
- Matched/missing skills + improvement suggestions
- History dashboard for previous analyses

## Tech Stack
- Frontend: Next.js + Tailwind CSS
- Backend: FastAPI (Python)
- Database/Auth/Storage: Supabase
- AI: Gemini or OpenAI (configurable)

## Project Structure
```
smart-resume-analyzer/
├── frontend/          (Next.js app)
├── backend/           (FastAPI service)
├── supabase/          (SQL migrations)
└── README.md
```

## Setup

### 1) Supabase
1. Create a Supabase project.
2. Enable Auth (email/password).
3. Create a Storage bucket named `resumes` (private recommended).
4. Run SQL migrations (in order):
   1. `supabase/migrations/001_init.sql`
   2. `supabase/migrations/002_rls.sql`
   3. `supabase/migrations/004_indexes.sql`
   4. `supabase/migrations/005_add_storage_path.sql`
   5. `supabase/migrations/006_add_resume_text.sql`
   6. `supabase/migrations/007_add_analysis_scores.sql`

Storage policies must be created in the Supabase UI for the `resumes` bucket:
- SELECT, INSERT, UPDATE, DELETE
- Condition:
  `bucket_id = 'resumes' AND auth.uid() = owner`

### 2) Backend
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
uvicorn main:app --reload --port 8000
```

Create `backend/.env`:
```
SUPABASE_URL=...
SUPABASE_SERVICE_ROLE_KEY=...
FRONTEND_ORIGIN=http://127.0.0.1:3000
AI_PROVIDER=gemini   # or openai
AI_API_KEY=...
AI_MODEL=gemini-2.5-flash
```

### 3) Frontend
```bash
cd frontend
npm install
npm run dev
```

Create `frontend/.env.local`:
```
NEXT_PUBLIC_SUPABASE_URL=...
NEXT_PUBLIC_SUPABASE_ANON_KEY=...
NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8000
```

Open: http://127.0.0.1:3000

## Deployment
- Frontend: Vercel
- Backend: Railway (or Render/Fly)

### Add your Vercel link here
Update the "Live Demo" section once deployed.
