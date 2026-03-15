#!/usr/bin/env python3
"""
Smart Resume Analyzer - Complete Application Runner
Runs both frontend (HTTP server) and backend (FastAPI) on localhost:3000 and localhost:8000
"""

import os
import subprocess
import sys
import time
import webbrowser
from pathlib import Path

def run_command(cmd, cwd=None, shell=True):
    """Run a shell command in a subprocess"""
    print(f">>> Running: {cmd}")
    if shell:
        subprocess.Popen(cmd, cwd=cwd, shell=True)
    else:
        subprocess.Popen(cmd, cwd=cwd)
    return True

def main():
    project_root = Path(__file__).parent
    backend_dir = project_root / "backend"
    frontend_dir = project_root / "frontend"

    print("=" * 60)
    print("Smart Resume Analyzer - Starting Application")
    print("=" * 60)

    # Check if required files exist
    if not (backend_dir / "main.py").exists():
        print("❌ Backend main.py not found!")
        return False

    if not (frontend_dir / "index.html").exists():
        print("❌ Frontend index.html not found!")
        return False

    if not (backend_dir / ".env").exists():
        print("❌ Backend .env file not found!")
        return False

    print("✅ All required files found\n")

    # Start backend
    print("📌 Starting Backend (FastAPI on localhost:8000)...")
    backend_cmd = f"cd \"{backend_dir}\" && .venv\\Scripts\\activate && uvicorn main:app --reload --port 8000"
    run_command(backend_cmd)
    time.sleep(2)

    # Start frontend HTTP server
    print("📌 Starting Frontend (HTTP Server on localhost:3000)...")
    # Using Python's built-in HTTP server
    frontend_cmd = f"cd \"{frontend_dir}\" && python -m http.server 3000"
    run_command(frontend_cmd)
    time.sleep(2)

    print("\n" + "=" * 60)
    print("✅ Application Started Successfully!")
    print("=" * 60)
    print("\n📍 Frontend available at: http://localhost:3000")
    print("📍 Backend API available at: http://localhost:8000")
    print("📍 API Docs available at: http://localhost:8000/docs")
    print("\n💡 Tips:")
    print("   - Upload a PDF resume or paste text")
    print("   - Paste a job description")
    print("   - Click 'Analyze Resume' to get ATS score and suggestions")
    print("\n🔌 Press Ctrl+C to stop the application")
    print("=" * 60 + "\n")

    # Optionally open browser
    try:
        print("Opening application in browser...")
        webbrowser.open("http://localhost:3000")
    except Exception as e:
        print(f"Could not open browser: {e}")

    # Keep the script running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nShutting down application...")
        print("✅ Application stopped")
        sys.exit(0)

if __name__ == "__main__":
    main()
