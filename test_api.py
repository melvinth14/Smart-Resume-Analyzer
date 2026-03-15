#!/usr/bin/env python3
"""
Quick test script to verify Resume Analyzer is working correctly
Tests both backend API and frontend
"""

import json
import time
import urllib.request
import urllib.error


def test_health_check():
    """Test backend health endpoint"""
    print("\n🔍 Testing Backend Health Check...")
    print("   Endpoint: http://localhost:8000/health")

    try:
        response = urllib.request.urlopen("http://localhost:8000/health", timeout=3)
        data = json.loads(response.read().decode())

        print("   ✅ Backend is responding")
        print(f"   Status: {data.get('status')}")
        print(f"   Gemini API Key Set: {data.get('gemini_key_set')}")

        return data.get("gemini_key_set", False)
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False


def test_analyze_with_text():
    """Test analyze endpoint with resume text"""
    print("\n🔍 Testing Analysis with Resume Text...")
    print("   Endpoint: POST http://localhost:8000/analyze")

    payload = {
        "job_description": "Senior Python Developer with FastAPI experience required",
        "resume_text": "John Smith - 5 years Python experience, FastAPI developer"
    }

    try:
        data = json.dumps(payload).encode('utf-8')
        request = urllib.request.Request(
            "http://localhost:8000/analyze",
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST"
        )

        response = urllib.request.urlopen(request, timeout=30)
        result = json.loads(response.read().decode())

        if "ats_score" in result:
            print("   ✅ Analysis successful")
            print(f"   ATS Score: {result.get('ats_score')}%")
            print(f"   Matched Skills: {result.get('matched_skills', [])}")
            print(f"   Missing Skills: {result.get('missing_skills', [])}")
            print(f"   AI Used: {result.get('ai_used')}")
            return True
        else:
            print(f"   ❌ Unexpected response: {result}")
            return False

    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        print(f"   ❌ HTTP Error {e.code}: {error_body}")
        return False
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False


def test_missing_resume():
    """Test error when resume is missing"""
    print("\n🔍 Testing Error: Missing Resume...")

    payload = {
        "job_description": "Senior Python Developer"
        # No resume provided
    }

    try:
        data = json.dumps(payload).encode('utf-8')
        request = urllib.request.Request(
            "http://localhost:8000/analyze",
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST"
        )

        response = urllib.request.urlopen(request, timeout=10)
        print("   ❌ Should have failed but didn't!")
        return False

    except urllib.error.HTTPError as e:
        error_body = json.loads(e.read().decode())
        error_msg = error_body.get("detail", "")

        if "Please provide resume" in error_msg:
            print(f"   ✅ Correct error message: {error_msg}")
            return True
        else:
            print(f"   ⚠️  Got error but different message: {error_msg}")
            return False

    except Exception as e:
        print(f"   ❌ Unexpected error: {e}")
        return False


def test_missing_job():
    """Test error when job description is missing"""
    print("\n🔍 Testing Error: Missing Job Description...")

    payload = {
        "resume_text": "John Smith - Python developer"
        # No job_description
    }

    try:
        data = json.dumps(payload).encode('utf-8')
        request = urllib.request.Request(
            "http://localhost:8000/analyze",
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST"
        )

        response = urllib.request.urlopen(request, timeout=10)
        print("   ❌ Should have failed but didn't!")
        return False

    except urllib.error.HTTPError as e:
        error_body = json.loads(e.read().decode())
        error_msg = error_body.get("detail", "")

        if "Job description is required" in error_msg:
            print(f"   ✅ Correct error message: {error_msg}")
            return True
        else:
            print(f"   ⚠️  Got error but different message: {error_msg}")
            return False

    except Exception as e:
        print(f"   ❌ Unexpected error: {e}")
        return False


def main():
    print("\n" + "=" * 60)
    print("Resume Analyzer - Full Test Suite")
    print("=" * 60)

    print("\nMake sure both services are running:")
    print("  Backend: uvicorn main:app --reload --port 8000")
    print("  Frontend: python -m http.server 3000")

    print("\nWaiting 3 seconds before starting tests...")
    time.sleep(3)

    results = {
        "Health Check": test_health_check(),
        "Analyze with Text": test_analyze_with_text(),
        "Error: Missing Resume": test_missing_resume(),
        "Error: Missing Job": test_missing_job(),
    }

    print("\n" + "=" * 60)
    print("TEST RESULTS SUMMARY")
    print("=" * 60)

    all_passed = True
    for test_name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} - {test_name}")
        if not passed:
            all_passed = False

    print("\n" + "=" * 60)

    if all_passed:
        print("✅ ALL TESTS PASSED!")
        print("\nThe application is working correctly!")
        print("You can now:")
        print("  1. Open http://localhost:3000 in browser")
        print("  2. Paste a job description (required)")
        print("  3. Upload PDF or paste resume text (required - at least one)")
        print("  4. Click 'Analyze Resume'")
    else:
        print("❌ SOME TESTS FAILED")
        print("\nTroubleshooting:")
        print("  - Make sure backend is running on port 8000")
        print("  - Check for errors in backend terminal")
        print("  - Verify Gemini API key is set in .env")
        print("  - Try: python diagnose.py")

    print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    main()
