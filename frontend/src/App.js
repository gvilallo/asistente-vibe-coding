import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import SessionPage from './pages/SessionPage';
import './App.css';

// Página de inicio
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
        <Link 
          to="/projects"
          style={{ 
            padding: '10px 20px', 
            background: '#007bff', 
            color: 'white', 
            border: 'none', 
            borderRadius: '4px',
            textDecoration: 'none',
            display: 'inline-block'
          }}
        >
          Ver Proyectos
        </Link>
        <Link 
          to="/demo-session"
          style={{ 
            padding: '10px 20px', 
            background: '#28a745', 
            color: 'white', 
            border: 'none', 
            borderRadius: '4px',
            textDecoration: 'none',
            display: 'inline-block'
          }}
        >
          🚀 Probar Demo
        </Link>
      </div>
    </div>
  </div>
);

// Páginas temporales
const ProjectsPage = () => <div>Lista de Proyectos (Por implementar)</div>;
const ProjectPage = () => <div>Detalle de Proyecto (Por implementar)</div>;

// Página demo para probar inmediatamente
const DemoSessionPage = () => {
  // Para el demo, usamos un sessionId fijo
  return <SessionPage sessionId="demo" projectId="demo" />;
};

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/projects" element={<ProjectsPage />} />
          <Route path="/projects/:projectId" element={<ProjectPage />} />
          <Route path="/projects/:projectId/sessions/:sessionId" element={<SessionPage />} />
          <Route path="/demo-session" element={<DemoSessionPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
