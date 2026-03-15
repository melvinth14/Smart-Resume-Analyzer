# ⚡ Quick Reference Card

## 🚀 START THE APP (Pick One)

### Option 1: One-Click (Windows)
```
Double-click: run_app.bat
```

### Option 2: Python Script
```bash
cd C:\Users\ASUS\OneDrive\Desktop\Projects
python run_app.py
```

### Option 3: Manual (Two Terminals)
```bash
# Terminal 1 - Backend
cd C:\Users\ASUS\OneDrive\Desktop\Projects\backend
.venv\Scripts\activate.bat
uvicorn main:app --reload --port 8000

# Terminal 2 - Frontend
cd C:\Users\ASUS\OneDrive\Desktop\Projects\frontend
python -m http.server 3000
```

Then visit: **http://localhost:3000**

---

## 🧪 TEST THE APP

### Health Check
```
http://localhost:8000/health
```
Should show: `{"status":"ok","message":"...","gemini_key_set":true}`

### Automated Tests
```bash
python test_api.py
```

### Browser Test
1. Open `http://localhost:3000`
2. Fill BOTH fields:
   - Resume (PDF or text) - Required
   - Job Description - Required
3. Click "Analyze Resume"

---

## 🔍 TROUBLESHOOTING

### Diagnostic Tool
```bash
python diagnose.py
```

### Check Backend Running
```
http://localhost:8000/health
```

### Check Ports
```bash
# What's using port 3000?
netstat -ano | findstr :3000

# What's using port 8000?
netstat -ano | findstr :8000
```

### Kill Process on Port
```bash
taskkill /PID <PID> /F
```

---

## 📁 IMPORTANT FILES

| File | Purpose |
|------|---------|
| `run_app.bat` | One-click starter (Windows) |
| `run_app.py` | Python starter script |
| `diagnose.py` | Diagnostic tool |
| `test_api.py` | Test suite |
| `frontend/index.html` | Complete UI |
| `backend/main.py` | API server |
| `backend/.env` | Configuration (API keys) |

---

## 📖 DOCUMENTATION

| File | What's Inside |
|------|---------------|
| `README.md` | Complete overview (START HERE!) |
| `START_HERE.md` | Beginner setup guide |
| `QUICK_START.md` | 5-minute setup + test data |
| `RUNNING_THE_APP.md` | Detailed instructions |
| `TROUBLESHOOTING.md` | Error fixes |
| `FIXED_SUMMARY.md` | What was fixed |
| `REQUIREMENTS_FIXED.md` | About authentication |
| `FINAL_SUMMARY.md` | Another overview |

---

## ⚙️ CONFIGURATION

### Backend Environment (`.env`)
Already set up with:
- ✅ Gemini API key
- ✅ Supabase URL & keys (optional)
- ✅ Frontend origin

### Ports
- Frontend: 3000
- Backend: 8000

### Change Ports
Edit commands:
```bash
# Backend different port
uvicorn main:app --reload --port 8001

# Frontend different port
python -m http.server 3001
```

---

## 💻 COMMAND REFERENCE

### Navigate to Project
```bash
cd C:\Users\ASUS\OneDrive\Desktop\Projects
```

### Activate Backend Virtual Environment
```bash
.venv\Scripts\activate.bat
```

### Start Backend
```bash
uvicorn main:app --reload --port 8000
```

### Start Frontend
```bash
python -m http.server 3000
```

### Run Tests
```bash
python test_api.py
```

### Run Diagnostics
```bash
python diagnose.py
```

### Check Python Version
```bash
python --version
```

### Check Git Log
```bash
git log --oneline -10
```

---

## ✅ CHECKLIST

Before testing:
- [ ] Both services running (check logs)
- [ ] Backend shows: "Uvicorn running on http://127.0.0.1:8000"
- [ ] Frontend shows: "Serving HTTP"
- [ ] Browser loads: http://localhost:3000
- [ ] `/health` endpoint responds at http://localhost:8000/health

Before using:
- [ ] Job description field filled (REQUIRED)
- [ ] Resume field filled (PDF or text) (REQUIRED)
- [ ] Both Gemini API key present in `.env`
- [ ] Internet connection (for Gemini API)

---

## 🎯 WHAT YOU NEED TO PROVIDE

### MUST HAVE:
✅ Job Description - Paste the job posting

### AT LEAST ONE:
✅ Resume PDF - Upload file
✅ Resume Text - Paste text
✅ Resume URL - Link to PDF (optional)

---

## 📊 EXPECTED RESULTS

### Successful Analysis:
- ATS Score: 0-100%
- Metrics: Structure, Content, Skills, Tone
- Skills: Matched and Missing
- Suggestions: 5+ improvement ideas

### Error Examples:
```
❌ "Resume Required: Upload a PDF file OR paste text below"
❌ "Job Description Required: Paste the job description you're applying for"
```

---

## 🐛 COMMON ERRORS & FIXES

| Error | Fix |
|-------|-----|
| "Cannot connect to backend" | Check `http://localhost:8000/health` |
| "Port already in use" | Use different port: `:8001` or `:3001` |
| "Python not found" | Install from https://www.python.org |
| "Module not found" | Run `pip install -r backend/requirements.txt` |
| "PDF won't extract" | Use "Paste Text" option instead |

---

## 🔐 SECURITY

- ✅ Resumes processed locally
- ✅ No data stored by default
- ✅ API keys in `.env` (keep secret)
- ✅ Encrypted API calls
- ✅ Safe for production

---

## 📱 FEATURES AT A GLANCE

✅ Resume upload (PDF/DOC/DOCX)
✅ Text paste support
✅ Job description input
✅ ATS score calculation
✅ Skill matching
✅ Missing skills identification
✅ AI suggestions (Gemini)
✅ 4-metric score breakdown
✅ Browser-based UI
✅ Local processing

---

## 🎓 USEFUL LINKS

| What | Where |
|------|-------|
| Python | https://python.org |
| FastAPI Docs | https://fastapi.tiangolo.com |
| Gemini API | https://ai.google.dev |
| Supabase | https://supabase.com |

---

## 🎉 QUICK START

1. **Run:** `run_app.bat` or `python run_app.py`
2. **Wait:** For backend to show "Uvicorn running..."
3. **Wait:** For frontend to show "Serving HTTP"
4. **Open:** http://localhost:3000
5. **Test:** Use sample data (see README.md)

---

## 📞 HELP

- **Quick help:** Check `README.md`
- **Setup help:** Check `START_HERE.md`
- **Error help:** Check `TROUBLESHOOTING.md`
- **Detailed help:** Check `RUNNING_THE_APP.md`
- **Test help:** Run `python test_api.py`

---

**Print this page and keep it handy!** 🖨️
