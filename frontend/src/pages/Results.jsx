import React from 'react';
import '../styles/Results.css';

export default function Results({ data, onGoBack }) {
  if (!data) {
    return <div>No data available</div>;
  }

  return (
    <div className="results">
      <button onClick={onGoBack} className="back-btn">
        ← Back to Analyzer
      </button>

      <div className="results-container">
        {/* ATS Score Section */}
        <div className="score-card primary">
          <h2>Overall ATS Score</h2>
          <div className="big-score">
            {data.ats_score}
            <span>%</span>
          </div>
          <p>How well your resume matches the job description</p>
        </div>

        {/* Detailed Scores */}
        <div className="scores-grid">
          <div className="score-card">
            <h3>📋 Structure</h3>
            <div className="score">{data.structure_score}%</div>
          </div>
          <div className="score-card">
            <h3>✍️ Content</h3>
            <div className="score">{data.content_score}%</div>
          </div>
          <div className="score-card">
            <h3>🎯 Skills Match</h3>
            <div className="score">{data.skills_score}%</div>
          </div>
          <div className="score-card">
            <h3>💬 Tone & Style</h3>
            <div className="score">{data.tone_style_score}%</div>
          </div>
        </div>

        {/* Skills Analysis */}
        <div className="skills-section">
          <div className="skills-box matched">
            <h3>✅ Matched Skills ({data.matched_skills?.length || 0})</h3>
            <ul>
              {data.matched_skills?.map((skill, i) => (
                <li key={i}>{skill}</li>
              ))}
            </ul>
          </div>

          <div className="skills-box missing">
            <h3>❌ Missing Skills ({data.missing_skills?.length || 0})</h3>
            <ul>
              {data.missing_skills?.map((skill, i) => (
                <li key={i}>{skill}</li>
              ))}
            </ul>
          </div>
        </div>

        {/* Suggestions */}
        {data.suggestions && (
          <div className="suggestions-section">
            <h3>💡 Improvement Suggestions</h3>
            <ul>
              {data.suggestions.split('\n').map((suggestion, i) => (
                suggestion.trim() && (
                  <li key={i}>{suggestion.replace(/^\d+\.\s*/, '')}</li>
                )
              ))}
            </ul>
          </div>
        )}

        {/* AI Info */}
        {data.ai_used && (
          <div className="info-box">
            <p>✨ Analysis powered by AI</p>
          </div>
        )}
        {data.ai_error && (
          <div className="warning-box">
            <p>⚠️ Some features used fallback analysis: {data.ai_error}</p>
          </div>
        )}
      </div>
    </div>
  );
}
