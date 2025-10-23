import React, { useState, useEffect } from 'react';
import './App.css';

const API_URL = process.env.REACT_APP_BACKEND_URL || 'http://localhost:8001';

function App() {
  const [vista, setVista] = useState('home');
  const [temario, setTemario] = useState([]);
  const [seccionActual, setSeccionActual] = useState(null);
  const [flashcards, setFlashcards] = useState([]);
  const [flashcardActual, setFlashcardActual] = useState(0);
  const [mostrarRespuesta, setMostrarRespuesta] = useState(false);
  const [filtroCategoria, setFiltroCategoria] = useState('');
  const [filtroDificultad, setFiltroDificultad] = useState('');
  const [categorias, setCategorias] = useState([]);
  const [loading, setLoading] = useState(false);
  const [modoEstudio, setModoEstudio] = useState('todas'); // 'todas' o 'categoria'

  useEffect(() => {
    cargarDatos();
  }, []);

  const cargarDatos = async () => {
    try {
      setLoading(true);
      const [temarioRes, flashcardsRes, categoriasRes] = await Promise.all([
        fetch(`${API_URL}/api/temario`),
        fetch(`${API_URL}/api/flashcards`),
        fetch(`${API_URL}/api/categorias`)
      ]);

      const temarioData = await temarioRes.json();
      const flashcardsData = await flashcardsRes.json();
      const categoriasData = await categoriasRes.json();

      setTemario(temarioData.temario);
      setFlashcards(flashcardsData.flashcards);
      setCategorias(categoriasData.categorias);
    } catch (error) {
      console.error('Error cargando datos:', error);
    } finally {
      setLoading(false);
    }
  };

  const cargarFlashcardsFiltradas = async () => {
    try {
      setLoading(true);
      let url = `${API_URL}/api/flashcards`;
      const params = new URLSearchParams();
      if (filtroCategoria) params.append('categoria', filtroCategoria);
      if (filtroDificultad) params.append('dificultad', filtroDificultad);
      if (params.toString()) url += `?${params.toString()}`;

      const res = await fetch(url);
      const data = await res.json();
      setFlashcards(data.flashcards);
      setFlashcardActual(0);
      setMostrarRespuesta(false);
    } catch (error) {
      console.error('Error filtrando flashcards:', error);
    } finally {
      setLoading(false);
    }
  };

  const siguienteFlashcard = () => {
    setMostrarRespuesta(false);
    setFlashcardActual((prev) => (prev + 1) % flashcards.length);
  };

  const anteriorFlashcard = () => {
    setMostrarRespuesta(false);
    setFlashcardActual((prev) => (prev - 1 + flashcards.length) % flashcards.length);
  };

  const Home = () => (
    <div className="home-container">
      <div className="hero-section">
        <h1 className="hero-title">📚 Guía de Estudio</h1>
        <h2 className="hero-subtitle">Programación en Java</h2>
        <p className="hero-description">
          Aprende los conceptos fundamentales de programación en Java de manera sencilla y efectiva.
          Incluye resúmenes, explicaciones claras y flashcards para practicar.
        </p>
      </div>

      <div className="features-grid">
        <div className="feature-card" onClick={() => setVista('temario')}>
          <div className="feature-icon">📖</div>
          <h3>Temario Completo</h3>
          <p>15 secciones con explicaciones detalladas y conceptos clave destacados</p>
          <button className="feature-button">Explorar Temario</button>
        </div>

        <div className="feature-card" onClick={() => setVista('flashcards')}>
          <div className="feature-icon">🎴</div>
          <h3>Flashcards</h3>
          <p>30 tarjetas de estudio para repasar conceptos y prepararte para el examen</p>
          <button className="feature-button">Practicar Ahora</button>
        </div>

        <div className="feature-card">
          <div className="feature-icon">✨</div>
          <h3>Contenido Destacado</h3>
          <p>Los puntos más importantes de cada tema resaltados para un estudio eficiente</p>
          <button className="feature-button" onClick={() => setVista('temario')}>Ver Destacados</button>
        </div>
      </div>

      <div className="stats-section">
        <div className="stat-item">
          <div className="stat-number">{temario.length}</div>
          <div className="stat-label">Secciones</div>
        </div>
        <div className="stat-item">
          <div className="stat-number">{flashcards.length}</div>
          <div className="stat-label">Flashcards</div>
        </div>
        <div className="stat-item">
          <div className="stat-number">{categorias.length}</div>
          <div className="stat-label">Categorías</div>
        </div>
      </div>
    </div>
  );

  const VistaTemario = () => (
    <div className="temario-container">
      <div className="temario-header">
        <h1>📖 Temario Completo de Programación Java</h1>
        <p>Explora cada sección para entender los conceptos fundamentales</p>
      </div>

      <div className="secciones-grid">
        {temario.map((seccion, index) => (
          <div 
            key={index} 
            className="seccion-card"
            onClick={() => {
              setSeccionActual(seccion);
              setVista('seccion');
            }}
          >
            <div className="seccion-numero">Sección {index + 1}</div>
            <h3>{seccion.titulo}</h3>
            <div className="seccion-nivel">
              Nivel: {seccion.nivel === 1 ? '⭐ Básico' : '⭐⭐ Intermedio'}
            </div>
            <div className="puntos-preview">
              {seccion.puntos_clave.length} puntos clave
            </div>
          </div>
        ))}
      </div>
    </div>
  );

  const VistaSeccion = () => {
    if (!seccionActual) return null;

    return (
      <div className="seccion-detalle">
        <button className="btn-volver" onClick={() => setVista('temario')}>
          ← Volver al Temario
        </button>

        <div className="seccion-header">
          <h1>{seccionActual.titulo}</h1>
          <div className="seccion-meta">
            <span className="nivel-badge">
              {seccionActual.nivel === 1 ? '⭐ Nivel Básico' : '⭐⭐ Nivel Intermedio'}
            </span>
          </div>
        </div>

        <div className="seccion-contenido">
          <div className="contenido-principal">
            <h2>📝 Explicación Detallada</h2>
            <div className="texto-contenido">
              {seccionActual.contenido.split('\n').map((parrafo, i) => (
                <p key={i}>{parrafo}</p>
              ))}
            </div>
          </div>

          <div className="puntos-clave-section">
            <h2>⭐ Puntos Clave - Lo Más Importante</h2>
            <ul className="puntos-clave-lista">
              {seccionActual.puntos_clave.map((punto, i) => (
                <li key={i} className="punto-clave">
                  <span className="punto-icono">✓</span>
                  {punto}
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    );
  };

  const VistaFlashcards = () => (
    <div className="flashcards-container">
      <div className="flashcards-header">
        <h1>🎴 Flashcards de Estudio</h1>
        <p>Practica y repasa los conceptos clave</p>
      </div>

      <div className="filtros-section">
        <div className="filtro-group">
          <label>Categoría:</label>
          <select 
            value={filtroCategoria} 
            onChange={(e) => setFiltroCategoria(e.target.value)}
          >
            <option value="">Todas las categorías</option>
            {categorias.map((cat, i) => (
              <option key={i} value={cat}>{cat}</option>
            ))}
          </select>
        </div>

        <div className="filtro-group">
          <label>Dificultad:</label>
          <select 
            value={filtroDificultad} 
            onChange={(e) => setFiltroDificultad(e.target.value)}
          >
            <option value="">Todas</option>
            <option value="Fácil">Fácil</option>
            <option value="Media">Media</option>
            <option value="Difícil">Difícil</option>
          </select>
        </div>

        <button className="btn-filtrar" onClick={cargarFlashcardsFiltradas}>
          Aplicar Filtros
        </button>
      </div>

      {flashcards.length > 0 ? (
        <div className="flashcard-wrapper">
          <div className="flashcard-contador">
            Tarjeta {flashcardActual + 1} de {flashcards.length}
          </div>

          <div 
            className={`flashcard ${mostrarRespuesta ? 'volteada' : ''}`}
            onClick={() => setMostrarRespuesta(!mostrarRespuesta)}
          >
            {!mostrarRespuesta ? (
              <div className="flashcard-front">
                <div className="flashcard-etiquetas">
                  <span className="categoria-badge">
                    {flashcards[flashcardActual].categoria}
                  </span>
                  <span className={`dificultad-badge ${flashcards[flashcardActual].dificultad.toLowerCase()}`}>
                    {flashcards[flashcardActual].dificultad}
                  </span>
                </div>
                <div className="flashcard-pregunta">
                  <h2>❓ Pregunta</h2>
                  <p>{flashcards[flashcardActual].pregunta}</p>
                </div>
                <div className="flashcard-hint">
                  👆 Haz clic para ver la respuesta
                </div>
              </div>
            ) : (
              <div className="flashcard-back">
                <div className="flashcard-respuesta">
                  <h2>✅ Respuesta</h2>
                  <p>{flashcards[flashcardActual].respuesta}</p>
                </div>
                <div className="flashcard-hint">
                  👆 Haz clic para volver a la pregunta
                </div>
              </div>
            )}
          </div>

          <div className="flashcard-controles">
            <button 
              className="btn-control" 
              onClick={anteriorFlashcard}
              disabled={flashcards.length <= 1}
            >
              ← Anterior
            </button>
            <button 
              className="btn-control btn-voltear" 
              onClick={() => setMostrarRespuesta(!mostrarRespuesta)}
            >
              {mostrarRespuesta ? '🔄 Ver Pregunta' : '🔄 Ver Respuesta'}
            </button>
            <button 
              className="btn-control" 
              onClick={siguienteFlashcard}
              disabled={flashcards.length <= 1}
            >
              Siguiente →
            </button>
          </div>
        </div>
      ) : (
        <div className="no-flashcards">
          <p>No hay flashcards que coincidan con los filtros seleccionados</p>
        </div>
      )}
    </div>
  );

  return (
    <div className="App">
      <nav className="navbar">
        <div className="nav-brand" onClick={() => setVista('home')}>
          <span className="nav-icon">📚</span>
          <span className="nav-title">Programación Java</span>
        </div>
        <div className="nav-links">
          <button 
            className={vista === 'home' ? 'nav-link active' : 'nav-link'} 
            onClick={() => setVista('home')}
          >
            🏠 Inicio
          </button>
          <button 
            className={vista === 'temario' || vista === 'seccion' ? 'nav-link active' : 'nav-link'} 
            onClick={() => setVista('temario')}
          >
            📖 Temario
          </button>
          <button 
            className={vista === 'flashcards' ? 'nav-link active' : 'nav-link'} 
            onClick={() => setVista('flashcards')}
          >
            🎴 Flashcards
          </button>
        </div>
      </nav>

      <main className="main-content">
        {loading && <div className="loading">Cargando...</div>}
        {!loading && vista === 'home' && <Home />}
        {!loading && vista === 'temario' && <VistaTemario />}
        {!loading && vista === 'seccion' && <VistaSeccion />}
        {!loading && vista === 'flashcards' && <VistaFlashcards />}
      </main>

      <footer className="footer">
        <p>📚 Guía de Estudio - Programación en Java</p>
        <p>Creado para ayudarte a aprobar tu examen ✨</p>
      </footer>
    </div>
  );
}

export default App;