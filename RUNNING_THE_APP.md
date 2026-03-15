# 🎯 Smart Resume Analyzer - Complete Guide

## Quick Start (5 minutes)

### Prerequisites
- Python 3.8+
- Windows (or modify commands for your OS)

### Running the Application

**Option 1: Automatic (Recommended)**
```bash
python run_app.py
```
This will:
- Start the backend on `http://localhost:8000`
- Start the frontend on `http://localhost:3000`
- Open the app in your browser automatically

**Option 2: Manual (Two Terminal Windows)**

**Terminal 1 - Backend:**
```bash
cd backend
.venv\Scripts\activate
uvicorn main:app --reload --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
python -m http.server 3000
```

Then open: **http://localhost:3000**

---

## ✨ Features

### 📄 Resume Analysis
- **PDF Upload**: Upload your resume as PDF, DOC, or DOCX
- **Text Paste**: Paste your resume as plain text (copy from any text editor)
- **Job Description**: Paste the job description you want to apply to

### 🎯 ATS Scoring
Get detailed analysis with 4 key metrics:
- **📋 Structure Score**: How well-organized your resume is
- **✍️ Content Score**: How relevant your content is
- **🎯 Skills Match**: How many required skills you have
- **💬 Tone & Style**: Writing quality and professionalism

### 🔍 Skill Analysis
- **✅ Matched Skills**: Skills you have that the job needs
- **❌ Missing Skills**: Skills you should add or develop
- **💡 Suggestions**: AI-powered recommendations to improve your resume

### 🤖 AI-Powered Analysis
Powered by **Google Gemini AI**, the system:
- Analyzes your resume for ATS compatibility
- Extracts and matches key skills
- Provides personalized improvement suggestions
- Identifies missing qualifications

---

## 🔧 Setup & Troubleshooting

### First Time Setup

1. **Install Backend Dependencies:**
   ```bash
   cd backend
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Verify Backend Configuration:**
   - Check `backend/.env` has required API keys
   - Ensure Gemini API key is valid

3. **Run the Application:**
   ```bash
   python run_app.py
   ```

### Common Issues

**Issue: "Cannot connect to backend"**
- Make sure backend is running: `http://localhost:8000/docs` should open
- Check firewall settings
- Ensure port 8000 is not in use

**Issue: "Analysis failed"**
- Check browser console (F12) for detailed error
- Verify Gemini API key in `backend/.env`
- Ensure you've pasted BOTH resume AND job description

**Issue: "Resume text could not be extracted"**
- If uploading PDF: Try saving PDF as text first and paste instead
- Some PDFs have encryption - convert to text if possible
- Use "Paste Text" option - it's often more reliable

**Issue: Port 3000 or 8000 already in use**
```bash
# Find what's using port 3000
netstat -ano | findstr :3000

# Use different ports:
# Backend: uvicorn main:app --port 8001
# Frontend: python -m http.server 3001
```

---

## 📊 How It Works

### 1. Resume Upload Flow
```
Your Resume (PDF/Text)
        ↓
[Frontend] Encodes to Base64
        ↓
[Backend] Decodes & Extracts Text
        ↓
Text Processing & Analysis
        ↓
Returns Results
```

### 2. Analysis Algorithms

**Keyword Extraction:**
- Uses fallback regex tokenizer (fast, reliable)
- Extracts and normalizes words
- Compares with job description

**ATS Score Calculation:**
- 40% Skills Match (most important)
- 30% Content Relevance
- 20% Structure Quality
- 10% Tone & Professionalism

**Skill Matching:**
- Role-based skill database (IT, Finance, Marketing, etc.)
- Matches resume skills against job requirements
- Identifies gaps for improvement

---

## 🎓 Example Usage

### Try This Test:

**Resume Text:**
```
John Doe
Email: john@example.com

EXPERIENCE
Senior Software Engineer at TechCorp (2020-2024)
- Developed microservices using Python and FastAPI
- Led team of 5 engineers
- Improved performance by 40%

SKILLS
Python, FastAPI, PostgreSQL, Docker, Kubernetes, AWS, React

EDUCATION
BS Computer Science, State University
```

**Job Description:**
```
Senior Full Stack Engineer

Requirements:
- 5+ years software development experience
- Python and FastAPI expertise
- React and JavaScript knowledge
- PostgreSQL database design
- Docker and Kubernetes experience
- AWS cloud platform
- Team leadership skills

Nice to have:
- CI/CD pipeline experience
- Agile methodology
- Open source contributions
```

**Expected Result:**
- ATS Score: ~85-90%
- Most matched skills shown
- Suggestions to add CI/CD, Agile, OSS experience

---

## 📁 Project Structure

```
.
├── run_app.py              ← Start here! Runs everything
├── backend/
│   ├── main.py            ← FastAPI server with /analyze endpoint
│   ├── ai_suggestions.py  ← Gemini API integration
│   ├── skills.py          ← Skill extraction & database
│   ├── .env               ← API keys (keep secret!)
│   └── requirements.txt    ← Python dependencies
└── frontend/
    ├── index.html         ← Complete UI (no build needed!)
    └── (no npm, no build tools needed!)
```

---

## 🚀 Deployment

### Deploy to Heroku:

**Backend:**
```bash
# Create Procfile
echo "web: uvicorn main:app --host 0.0.0.0 --port $PORT" > backend/Procfile

# Deploy
cd backend
heroku create my-resume-analyzer-api
git push heroku main
```

**Frontend:**
```bash
# Deploy to GitHub Pages or any static hosting
# Or use Vercel, Netlify, Cloudflare Pages
```

### Environment Variables Needed:
- `SUPABASE_URL`
- `SUPABASE_SERVICE_ROLE_KEY`
- `AI_API_KEY` (Gemini)
- `AI_PROVIDER` (gemini)
- `AI_MODEL` (gemini-2.5-flash)

---

## 🔐 Security & Privacy

- ✅ Your resume data is processed locally (fast)
- ✅ No resume data is stored without your consent
- ✅ API calls use HTTPS
- ✅ Environment variables keep secrets safe
- ❌ Never commit `.env` file to git

---

## 📞 Support

**Issue with Analysis?**
1. Check browser console (F12) → Console tab
2. Check backend logs in terminal
3. Try the "Paste Text" option instead of PDF
4. Verify both resume AND job description are filled

**Want to Add Features?**
- Extend `backend/skills.py` for more job roles
- Customize scoring weights in `backend/main.py`
- Improve UI in `frontend/index.html`

---

## 📝 API Documentation

**Frontend → Backend Communication:**

**Request:**
```json
{
  "job_description": "Senior Python Developer...",
  "resume_text": "John Doe...",
  // or
  "resume_file": "base64encodedpdfhere..."
}
```

**Response:**
```json
{
  "ats_score": 85,
  "structure_score": 80,
  "content_score": 90,
  "skills_score": 85,
  "tone_style_score": 75,
  "matched_skills": ["Python", "FastAPI", "PostgreSQL"],
  "missing_skills": ["Kubernetes", "Docker"],
  "suggestions": ["Add CI/CD experience", "Mention Agile methodology"],
  "ai_used": true
}
```

---

## ✅ Checklist for First Run

- [ ] Python 3.8+ installed
- [ ] Backend venv created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file exists with API keys
- [ ] Backend starts without errors
- [ ] Frontend loads at `http://localhost:3000`
- [ ] Can type and submit data
- [ ] Backend responds with analysis
- [ ] Results display correctly

---

**Happy analyzing! 🎉**
