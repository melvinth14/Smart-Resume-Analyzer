import React, { useState } from 'react';
import './App.css';
import Analyzer from './pages/Analyzer';
import Results from './pages/Results';

function App() {
  const [page, setPage] = useState('analyzer');
  const [analysisData, setAnalysisData] = useState(null);

  const handleAnalysisComplete = (data) => {
    setAnalysisData(data);
    setPage('results');
  };

  const handleGoBack = () => {
    setPage('analyzer');
    setAnalysisData(null);
  };

  return (
    <div className="app">
      <header className="header">
        <h1>📄 Resume Analyzer</h1>
        <p>Match your resume with job descriptions</p>
      </header>

      <main className="main-content">
        {page === 'analyzer' ? (
          <Analyzer onAnalysisComplete={handleAnalysisComplete} />
        ) : (
          <Results data={analysisData} onGoBack={handleGoBack} />
        )}
      </main>

      <footer className="footer">
        <p>&copy; 2024 Smart Resume Analyzer</p>
      </footer>
    </div>
  );
}

export default App;
