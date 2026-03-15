# 🚀 How to Start the Resume Analyzer

## Method 1: One-Click Start (Windows) ⭐ EASIEST

**Double-click:** `run_app.bat`

That's it! It will:
- ✅ Start the backend on localhost:8000
- ✅ Start the frontend on localhost:3000
- ✅ Open your browser automatically

---

## Method 2: Manual Start (Two Terminal Windows)

### Step 1: Open First Terminal Window

**For Windows Command Prompt:**
```
Search for "cmd" → Right-click → "Run as administrator"
```

**For PowerShell:**
```
Right-click Start menu → Select "Windows PowerShell (Admin)" or "Terminal (Admin)"
```

### Step 2: Start Backend in First Window

Copy and paste this command:
```
cd C:\Users\ASUS\OneDrive\Desktop\Projects\backend
.venv\Scripts\activate.bat
uvicorn main:app --reload --port 8000
```

**Wait for it to say:** `Uvicorn running on http://127.0.0.1:8000`

### Step 3: Open Second Terminal Window

Repeat Step 1 (open another terminal/cmd window)

### Step 4: Start Frontend in Second Window

Copy and paste this command:
```
cd C:\Users\ASUS\OneDrive\Desktop\Projects\frontend
python -m http.server 3000
```

**Wait for it to say:** `Serving HTTP on...`

### Step 5: Open Browser

Visit: **http://localhost:3000**

---

## ✅ Verification Checklist

- [ ] Backend window shows: `Uvicorn running on http://127.0.0.1:8000`
- [ ] Frontend window shows: `Serving HTTP on...`
- [ ] Browser opened at http://localhost:3000
- [ ] You see the Resume Analyzer form
- [ ] Both input boxes are visible (Resume and Job Description)

---

## 🧪 Quick Test

Once the app is running, try this:

**In the Resume field (paste this):**
```
John Smith
Senior Python Developer

EXPERIENCE
5+ years building microservices with Python, FastAPI, PostgreSQL

SKILLS
Python, FastAPI, PostgreSQL, Docker, AWS, React, JavaScript
```

**In the Job Description field (paste this):**
```
Senior Python Engineer Needed

Required:
- Python and FastAPI expertise
- PostgreSQL knowledge
- Docker experience
- AWS cloud skills

Nice to have:
- React frontend skills
- Kubernetes experience
```

**Click:** "Analyze Resume"

**You should see:**
- ATS Score: ~75-85%
- Matched skills list
- Missing skills list
- Improvement suggestions

---

## ❌ Troubleshooting

### "Command not found" or "Python not recognized"
- **Solution:** Make sure Python is installed: `python --version`
- If not installed: Download from https://www.python.org

### Backend won't start ("port 8000 in use")
```
# Change port in the command:
uvicorn main:app --reload --port 8001
# Then in browser, backend URL becomes: http://localhost:8001
# Update API_URL in frontend/index.html line 395:
const API_URL = 'http://localhost:8001';
```

### Frontend won't start ("port 3000 in use")
```
# Change port in the frontend command:
python -m http.server 3001
# Then visit: http://localhost:3001
```

### "Cannot connect to backend"
- Make sure backend window shows: `Uvicorn running on...`
- Check firewall isn't blocking port 8000
- Try: http://localhost:8000/docs in browser (should work)

### "Analysis failed" error
1. Press **F12** in browser
2. Click **Console** tab
3. Look for error message
4. Check backend terminal for errors
5. Try "Paste Text" option if PDF upload fails

---

## 🛑 Stopping the Application

Simply close the terminal windows:
- Close backend terminal (Ctrl+C or click X)
- Close frontend terminal (Ctrl+C or click X)

---

## 📚 For More Help

- **Full documentation:** See `RUNNING_THE_APP.md`
- **Quick reference:** See `QUICK_START.md`
- **Sample data:** See `QUICK_START.md`

---

**That's all you need to know to get started!** 🎉
