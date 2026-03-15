import React, { useState } from 'react';
import '../styles/Analyzer.css';

const API_BASE = 'http://localhost:8000';

export default function Analyzer({ onAnalysisComplete }) {
  const [resumeText, setResumeText] = useState('');
  const [jobDescription, setJobDescription] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    if (!resumeText.trim()) {
      setError('Please paste your resume text');
      return;
    }

    if (!jobDescription.trim()) {
      setError('Please paste the job description');
      return;
    }

    setLoading(true);

    try {
      const response = await fetch(`${API_BASE}/analyze`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          resume_text: resumeText,
          job_description: jobDescription,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Analysis failed');
      }

      const data = await response.json();
      onAnalysisComplete(data);
    } catch (err) {
      setError(`Error: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="analyzer">
      <form onSubmit={handleSubmit} className="analyzer-form">
        <div className="form-group">
          <label htmlFor="resume">
            📄 Your Resume
          </label>
          <textarea
            id="resume"
            value={resumeText}
            onChange={(e) => setResumeText(e.target.value)}
            placeholder="Paste your resume text here..."
            rows="10"
          />
        </div>

        <div className="form-group">
          <label htmlFor="job">
            💼 Job Description
          </label>
          <textarea
            id="job"
            value={jobDescription}
            onChange={(e) => setJobDescription(e.target.value)}
            placeholder="Paste the job description here..."
            rows="10"
          />
        </div>

        {error && <div className="error-message">{error}</div>}

        <button type="submit" disabled={loading} className="submit-btn">
          {loading ? 'Analyzing...' : 'Analyze Resume'}
        </button>
      </form>

      <div className="tips">
        <h3>💡 Tips</h3>
        <ul>
          <li>Copy your resume from a text file or PDF converter</li>
          <li>Paste the complete job description</li>
          <li>The AI will match your skills and suggest improvements</li>
        </ul>
      </div>
    </div>
  );
}
