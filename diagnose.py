#!/usr/bin/env python3
"""
Quick diagnostic tool to test Resume Analyzer setup
Run from project root directory
"""

import subprocess
import sys
import time
from pathlib import Path


def test_backend_connection():
    """Test if backend is running and responding"""
    print("\n📌 Testing Backend Connection...")
    print("   Trying: http://localhost:8000/health")

    try:
        import urllib.request
        import json

        response = urllib.request.urlopen("http://localhost:8000/health", timeout=3)
        data = json.loads(response.read().decode())

        if data.get("status") == "ok":
            print("   ✅ BACKEND CONNECTED!")
            print(f"   Status: {data.get('message')}")
            print(f"   Gemini API: {'✅' if data.get('gemini_key_set') else '❌'}")
            return True
        else:
            print(f"   ❌ Unexpected response: {data}")
            return False
    except urllib.error.URLError as e:
        print(f"   ❌ Cannot connect to backend: {e}")
        print("   Make sure backend is running: uvicorn main:app --reload --port 8000")
        return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False


def test_frontend_connection():
    """Test if frontend is running"""
    print("\n📌 Testing Frontend Connection...")
    print("   Trying: http://localhost:3000")

    try:
        import urllib.request

        response = urllib.request.urlopen("http://localhost:3000", timeout=3)
        if response.status == 200:
            print("   ✅ FRONTEND LOADED!")
            return True
    except urllib.error.URLError as e:
        print(f"   ❌ Cannot connect to frontend: {e}")
        print("   Make sure frontend is running: python -m http.server 3000")
        return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False


def test_python_packages():
    """Test if required packages are installed"""
    print("\n📌 Testing Python Packages...")
    packages = ["fastapi", "uvicorn", "pdfplumber", "requests"]

    all_ok = True
    for package in packages:
        try:
            __import__(package)
            print(f"   ✅ {package}")
        except ImportError:
            print(f"   ❌ {package} - NOT INSTALLED")
            all_ok = False

    return all_ok


def test_env_file():
    """Check if .env file exists and has API keys"""
    print("\n📌 Checking Configuration...")

    env_path = Path("backend/.env")
    if env_path.exists():
        print(f"   ✅ .env file found")

        with open(env_path) as f:
            content = f.read()
            if "AI_API_KEY" in content:
                print(f"   ✅ Gemini API key configured")
            else:
                print(f"   ❌ Gemini API key missing")
        return True
    else:
        print(f"   ❌ .env file not found at {env_path.absolute()}")
        return False


def main():
    print("\n" + "=" * 50)
    print("Smart Resume Analyzer - Diagnostic Tool")
    print("=" * 50)

    # Check working directory
    if not Path("backend").exists() or not Path("frontend").exists():
        print("\n❌ ERROR: Must run from project root directory")
        print(f"   Current directory: {Path.cwd()}")
        print(f"   Expected 'backend' folder here: {Path('backend').absolute()}")
        sys.exit(1)

    print(f"\n📁 Project directory: {Path.cwd()}")

    # Run tests
    env_ok = test_env_file()
    packages_ok = test_python_packages()
    frontend_ok = test_frontend_connection()
    backend_ok = test_backend_connection()

    # Summary
    print("\n" + "=" * 50)
    print("RESULTS SUMMARY")
    print("=" * 50)

    if backend_ok and frontend_ok:
        print("✅ Everything is working!")
        print("\nNext steps:")
        print("1. Open browser: http://localhost:3000")
        print("2. Paste resume text and job description")
        print("3. Click 'Analyze Resume'")
    else:
        print("\n❌ Issues found:\n")
        if not env_ok:
            print("1. Configuration issue:")
            print("   - Check backend/.env exists")
            print("   - Verify AI_API_KEY is set")
        if not packages_ok:
            print("2. Missing packages:")
            print("   - Run: pip install -r backend/requirements.txt")
        if not frontend_ok:
            print("3. Frontend not running:")
            print("   - Terminal 2: cd frontend && python -m http.server 3000")
        if not backend_ok:
            print("4. Backend not running or not responding:")
            print("   - Terminal 1: cd backend && .venv\\Scripts\\activate.bat")
            print("   - Then: uvicorn main:app --reload --port 8000")
            print("   - Wait for: 'Uvicorn running on http://127.0.0.1:8000'")

    print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    main()
