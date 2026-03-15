@echo off
REM Smart Resume Analyzer - Quick Start Script for Windows

echo.
echo ========================================
echo Smart Resume Analyzer - Starting App
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python from https://www.python.org
    pause
    exit /b 1
)

echo ✅ Python detected

REM Check if backend .env exists
if not exist "backend\.env" (
    echo ❌ backend/.env file not found!
    echo Make sure you're running from the project root directory
    pause
    exit /b 1
)

echo ✅ Backend configuration found

REM Check if venv exists, if not create it
if not exist "backend\.venv" (
    echo 📦 Creating Python virtual environment...
    cd backend
    python -m venv .venv
    cd ..
    echo ✅ Virtual environment created
)

echo.
echo 🚀 Starting application...
echo.
echo 📌 Frontend: http://localhost:3000
echo 📌 Backend:  http://localhost:8000
echo 📌 API Docs: http://localhost:8000/docs
echo.

REM Start backend in a new window
start "Resume Analyzer Backend" cmd /k "cd /d %cd%\backend && .venv\Scripts\activate.bat && uvicorn main:app --reload --port 8000"
timeout /t 3 /nobreak

REM Start frontend in a new window
start "Resume Analyzer Frontend" cmd /k "cd /d %cd%\frontend && python -m http.server 3000"
timeout /t 2 /nobreak

REM Try to open browser
echo Opening browser...
start http://localhost:3000

echo.
echo ✅ Application started!
echo.
echo 💡 Tips:
echo - Both command windows should be running now
echo - Wait 5 seconds for servers to fully initialize
echo - If browser doesn't open, manually visit: http://localhost:3000
echo - Use browser console (F12 key) to see detailed errors
echo - Close the command windows to stop the application
echo.
echo Backend logs will appear in the first window
echo Frontend logs will appear in the second window
echo.

pause
