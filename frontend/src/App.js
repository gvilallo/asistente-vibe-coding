import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';

// Componentes de página (temporales)
const HomePage = () => (
  <div style={{ padding: '40px 20px', textAlign: 'center' }}>
    <h1>Asistente de Vibe Coding</h1>
    <p>Extracción de conocimiento para desarrollo de software</p>
    <div style={{ maxWidth: '600px', margin: '0 auto', textAlign: 'left', padding: '20px' }}>
      <h2>Transforma el conocimiento en código</h2>
      <p>
        El Asistente de Vibe Coding te guía a través de un proceso estructurado para capturar 
        el conocimiento de expertos de dominio y transformarlo en especificaciones técnicas.
      </p>
      <div style={{ display: 'flex', gap: '20px', marginTop: '30px', justifyContent: 'center' }}>
        <button style={{ padding: '10px 20px', background: '#3498db', color: 'white', border: 'none', borderRadius: '4px' }}>
          Ver Proyectos
        </button>
        <button style={{ padding: '10px 20px', background: '#f1f1f1', color: '#333', border: 'none', borderRadius: '4px' }}>
          Nuevo Proyecto
        </button>
      </div>
    </div>
  </div>
);

const ProjectsPage = () => <div>Lista de Proyectos (Por implementar)</div>;
const ProjectPage = () => <div>Detalle de Proyecto (Por implementar)</div>;
const SessionPage = () => <div>Sesión de Extracción (Por implementar)</div>;

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/projects" element={<ProjectsPage />} />
          <Route path="/projects/:projectId" element={<ProjectPage />} />
          <Route path="/projects/:projectId/sessions/:sessionId" element={<SessionPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
