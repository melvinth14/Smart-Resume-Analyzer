# ⚡ TROUBLESHOOTING - Backend Connection Issue

## Quick Fix Steps

### Step 1: Run Diagnostic Tool

**Open Command Prompt in the project root:**
```
C:\Users\ASUS\OneDrive\Desktop\Projects>
```

**Run the diagnostic:**
```bash
python diagnose.py
```

This will tell you exactly what's wrong!

---

## Common Issues & Fixes

### Issue: "Cannot connect to backend"

**Most Common Cause:** Backend is not actually running or not responding

**Fix:**
1. Open a terminal
2. Navigate to: `C:\Users\ASUS\OneDrive\Desktop\Projects\backend`
3. Run: `.venv\Scripts\activate.bat`
4. Wait for: `(.venv)` to appear in terminal
5. Run: `uvicorn main:app --reload --port 8000`
6. Wait for: `Uvicorn running on http://127.0.0.1:8000`

**Then test in browser:**
- Visit: `http://localhost:8000/health`
- Should see JSON response confirming backend works

---

### Issue: Running python run_app.py from wrong directory

**Error message:**
```
can't open file 'C:\...\frontend\run_app.py'
```

**Fix:**
Make sure you're in the PROJECT ROOT directory:
```
C:\Users\ASUS\OneDrive\Desktop\Projects>
```

Then run:
```bash
python run_app.py
```

---

## Step-by-Step Fix (Most Reliable)

### Terminal 1 - Start Backend

1. **Open new Command Prompt**
2. **Copy and paste this:**
   ```
   cd C:\Users\ASUS\OneDrive\Desktop\Projects\backend
   ```
3. **Press Enter**
4. **Copy and paste this:**
   ```
   .venv\Scripts\activate.bat
   ```
5. **Wait for `(.venv)` to appear**
6. **Copy and paste this:**
   ```
   uvicorn main:app --reload --port 8000
   ```
7. **Wait for:** `Uvicorn running on http://127.0.0.1:8000`

**✅ Leave this terminal running**

---

### Terminal 2 - Start Frontend

1. **Open ANOTHER new Command Prompt**
2. **Copy and paste this:**
   ```
   cd C:\Users\ASUS\OneDrive\Desktop\Projects\frontend
   ```
3. **Press Enter**
4. **Copy and paste this:**
   ```
   python -m http.server 3000
   ```
5. **Wait for:** `Serving HTTP`

**✅ Leave this terminal running**

---

### Browser

1. **Open browser**
2. **Visit:** `http://localhost:3000`
3. **You should see the Resume Analyzer form**

---

## Verification Checklist

Before testing, verify:

- [ ] Backend terminal shows: `Uvicorn running on http://127.0.0.1:8000`
- [ ] Backend terminal shows: `Application startup complete`
- [ ] Frontend terminal shows: `Serving HTTP on 0.0.0.0 port 3000`
- [ ] Open `http://localhost:8000/health` in browser → shows JSON response
- [ ] Open `http://localhost:3000` in browser → shows form

---

## If Still Not Working

### Run the diagnostic tool:
```bash
python diagnose.py
```

It will show exactly:
- ✅ Which services are running
- ✅ Which packages are installed
- ✅ Which configuration is correct
- ❌ What needs to be fixed

---

## CORS Error in Browser Console?

If you see: `"Cross-Origin Request Blocked"`

**This usually means:**
1. Backend isn't running
2. Backend running on wrong port
3. Try hard refresh: `Ctrl+F5`

**Test the backend directly:**
```
http://localhost:8000/health
```

Should show:
```json
{
  "status": "ok",
  "message": "Backend is running and ready",
  "endpoint": "POST /analyze",
  "gemini_key_set": true
}
```

---

## Next: Clerk Setup (Authentication)

You asked about Clerk setup. Currently, the application:
- ✅ Works without authentication (simple version)
- ✅ Anyone can use it
- ❌ No user login required

**Do you want to add Clerk authentication?**

Options:
1. **Keep it simple** (current) - No login needed
2. **Add Clerk login** - Secure, track users, multiple resumes

If you want Clerk, I can add it. Otherwise, the current version works great!

---

## Quick Diagnostic Commands

```bash
# Test Python
python --version

# Test backend import
cd backend
python -c "from main import app; print('OK')"

# Test if port 8000 is available
netstat -ano | findstr :8000

# If port in use, kill it:
taskkill /PID <PID> /F

# Test pip packages
pip list | findstr "fastapi uvicorn pdfplumber"
```

---

**Try these fixes and let me know what the diagnostic tool shows!** 🔍
