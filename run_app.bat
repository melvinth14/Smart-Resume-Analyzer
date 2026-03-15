@echo off
REM Smart Resume Analyzer - Quick Start Script for Windows

echo.
echo ========================================
echo SmartResume Analyzer - Starting App
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
start cmd /k "cd backend && .venv\Scripts\activate && uvicorn main:app --reload --port 8000"
timeout /t 3 /nobreak

REM Start frontend in a new window
start cmd /k "cd frontend && python -m http.server 3000"
timeout /t 2 /nobreak

REM Try to open browser
start http://localhost:3000

echo.
echo ✅ Application started!
echo Waiting for services to initialize...
timeout /t 5 /nobreak

echo.
echo 💡 Tips:
echo - Wait 5 seconds for both servers to start
echo - If browser doesn't open, visit http://localhost:3000 manually
echo - Use browser console (F12) to see detailed errors
echo - Close command windows to stop the application
echo.

pause
