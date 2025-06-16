import React from 'react';
import { Link } from 'react-router-dom';

function HomePage() {
  return (
    <div className="home-page">
      <header style={{ padding: '40px 20px', background: '#f5f5f5', textAlign: 'center' }}>
        <h1>Asistente de Vibe Coding</h1>
        <p>Extracción de conocimiento para desarrollo de software</p>
      </header>
      
      <main style={{ padding: '40px 20px', maxWidth: '800px', margin: '0 auto' }}>
        <section>
          <h2>Transforma el conocimiento en código</h2>
          <p>
            El Asistente de Vibe Coding te guía a través de un proceso estructurado para capturar 
            el conocimiento de expertos de dominio y transformarlo en especificaciones técnicas.
          </p>
          
          <div style={{ display: 'flex', gap: '20px', marginTop: '30px' }}>
            <Link to="/projects" style={{ 
              padding: '10px 20px', 
              background: '#3498db', 
              color: 'white', 
              textDecoration: 'none',
              borderRadius: '4px'
            }}>
              Ver Proyectos
            </Link>
            <Link to="/projects/new" style={{ 
              padding: '10px 20px', 
              background: '#f1f1f1', 
              color: '#333', 
              textDecoration: 'none',
              borderRadius: '4px'
            }}>
              Nuevo Proyecto
            </Link>
          </div>
        </section>
      </main>
    </div>
  );
}

export default HomePage;
