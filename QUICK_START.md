## 🚀 QUICK START - Resume Analyzer

### For Windows Users (Easiest):

**Just double-click this file:**
```
run_app.bat
```

That's it! It will:
✅ Start the backend server
✅ Start the frontend server
✅ Open the app in your browser

---

## Alternative: Command Line

**Open Terminal in project folder and run:**

```bash
python run_app.py
```

Or manually (two terminal windows):

**Terminal 1:**
```bash
cd backend
.venv\Scripts\activate
uvicorn main:app --reload --port 8000
```

**Terminal 2:**
```bash
cd frontend
python -m http.server 3000
```

Then visit: **http://localhost:3000**

---

## 🧪 Testing the Application

### Step 1: Open the App
Go to: **http://localhost:3000**

### Step 2: Try with Sample Data (Copy & Paste)

**Resume Text Option:**
```
John Smith
john.smith@email.com
(555) 123-4567

PROFESSIONAL SUMMARY
Senior Software Engineer with 8 years of experience developing scalable applications.

EXPERIENCE
Senior Developer - Tech Company (2020-Present)
- Designed and implemented microservices using Python and FastAPI
- Led development team of 5 engineers
- Reduced API response time by 45% using caching strategies
- Implemented CI/CD pipelines with Docker and Kubernetes

Skills: Python, FastAPI, PostgreSQL, Docker, Kubernetes, AWS, React, JavaScript, Git, Linux

EDUCATION
Bachelor of Science in Computer Science
State University, 2016
```

**Job Description Option:**
```
Senior Full Stack Engineer

About the Role:
We're looking for an experienced Senior Full Stack Engineer to join our team.

Required Skills:
- 5+ years of software development experience
- Expert in Python and FastAPI
- Strong knowledge of React and JavaScript
- PostgreSQL database design and optimization
- Docker containerization experience
- Kubernetes orchestration experience
- AWS cloud platform experience
- Leadership and team mentoring skills

Nice to Have:
- CI/CD pipeline experience
- CI/CD with Jenkins/GitLab
- Agile/Scrum methodology
- Open source contributions
```

### Step 3: Click "Analyze Resume"

### Expected Results:
- **ATS Score**: 80-85%
- **Matched Skills**: Python, FastAPI, PostgreSQL, Docker, Kubernetes, AWS, React, JavaScript
- **Missing Skills**: CI/CD, Jenkins, Agile
- **Suggestions**: Add CI/CD experience, mention Agile methodology

---

## 🔍 Troubleshooting

### "Cannot connect to backend" ❌
Check that backend is running:
- Open new browser tab: **http://localhost:8000/docs**
- If it loads → Backend is OK
- If it fails → Start backend (see above)

### "Analysis failed" ❌
Look at browser console (Press **F12** → **Console** tab):
- Shows detailed error message
- Common: Empty resume or job description

### "Resume text could not be extracted" ❌
- PDF might be encrypted or image-based
- **Solution**: Use "Paste Text" option instead
- Copy text from PDF into the text area

### Port Already in Use ❌
```bash
# Change port in run_app.bat or uvicorn command
# Example: uvicorn main:app --port 8001
```

---

## 📋 Feature Checklist

✅ Upload PDF resume or paste text
✅ Paste job description
✅ Get ATS compatibility score
✅ See detailed scoring breakdown
✅ View matched and missing skills
✅ Get AI-powered improvement suggestions
✅ View analysis powered by Google Gemini

---

## 🎯 Next Steps After Testing

1. **Fix any errors** (check console errors)
2. **Try your own resume**
3. **Test with different job descriptions**
4. **Check improvements** with revisions
5. **Deploy to production** (see RUNNING_THE_APP.md)

---

## 📝 Files You'll Need

- ✅ `backend/main.py` - API server
- ✅ `backend/.env` - Configuration (already set up)
- ✅ `frontend/index.html` - Web interface
- ✅ `run_app.bat` or `run_app.py` - Start everything

---

## 💡 Tips

- **Try multiple resumes:** Different experiences give different scores
- **Check the logs:** Terminal shows what's happening
- **Use browser console:** F12 → Console shows errors
- **Small changes matter:** Even adding one skill can change score

---

**Everything is ready! Just start the app and test it! 🎉**
