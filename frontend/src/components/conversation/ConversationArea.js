import React, { useState, useEffect, useRef } from 'react';

function ConversationArea({ sessionId }) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [currentProgress, setCurrentProgress] = useState(null);
  const [sessionReady, setSessionReady] = useState(false);
  const messagesEndRef = useRef(null);

  // Inicializar sesión al montar el componente
  useEffect(() => {
    if (sessionId === 'demo') {
      initializeDemoSession();
    } else if (sessionId) {
      loadMessages();
      loadProgress();
    }
  }, [sessionId]);

  // Scroll automático al final con animación suave
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ 
      behavior: 'smooth',
      block: 'end'
    });
  }, [messages]);

  const initializeDemoSession = async () => {
    try {
      setIsLoading(true);
      const response = await fetch('http://localhost:8000/demo/create-session', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        }
      });

      if (response.ok) {
        await loadMessages();
        await loadProgress();
        setSessionReady(true);
      }
    } catch (error) {
      console.error('Error initializing demo session:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const loadMessages = async () => {
    try {
      const response = await fetch(`http://localhost:8000/sessions/${sessionId}/messages`);
      if (response.ok) {
        const data = await response.json();
        setMessages(data);
      }
    } catch (error) {
      console.error('Error loading messages:', error);
    }
  };

  const loadProgress = async () => {
    try {
      const response = await fetch(`http://localhost:8000/sessions/${sessionId}/progress`);
      if (response.ok) {
        const data = await response.json();
        setCurrentProgress(data);
      }
    } catch (error) {
      console.error('Error loading progress:', error);
    }
  };

  const handleSendMessage = async () => {
    if (!input.trim() || isLoading) return;

    const userMessage = {
      sender: 'user',
      content: input.trim(),
      timestamp: new Date().toISOString()
    };

    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setIsLoading(true);

    try {
      const response = await fetch(`http://localhost:8000/sessions/${sessionId}/interact`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ content: userMessage.content })
      });

      if (response.ok) {
        const assistantMessage = await response.json();
        setMessages(prev => [...prev, assistantMessage]);
        await loadProgress();
      } else {
        console.error('Error sending message');
      }
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  // Mostrar loading mejorado
  if (sessionId === 'demo' && !sessionReady) {
    return (
      <div style={{ 
        display: 'flex', 
        justifyContent: 'center', 
        alignItems: 'center', 
        height: '400px',
        background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        borderRadius: '12px',
        color: 'white',
        boxShadow: '0 8px 32px rgba(0,0,0,0.1)'
      }}>
        <div style={{ textAlign: 'center' }}>
          <div style={{ 
            marginBottom: '20px', 
            fontSize: '48px',
            animation: 'pulse 2s infinite'
          }}>🚀</div>
          <div style={{ fontSize: '18px', fontWeight: 'bold' }}>
            Iniciando Vibe Coding...
          </div>
          <div style={{ fontSize: '14px', opacity: 0.8, marginTop: '10px' }}>
            Preparando el motor de extracción de conocimiento
          </div>
        </div>
      </div>
    );
  }

  return (
    <div style={{ 
      display: 'flex', 
      flexDirection: 'column', 
      height: '70vh',
      border: '1px solid #e0e0e0',
      borderRadius: '16px',
      overflow: 'hidden',
      background: 'white',
      boxShadow: '0 8px 32px rgba(0,0,0,0.08)'
    }}>
      {/* Header con progreso mejorado */}
      {currentProgress && (
        <div style={{ 
          padding: '20px', 
          background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)', 
          color: 'white'
        }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '15px' }}>
            <div>
              <h3 style={{ margin: 0, fontSize: '18px', fontWeight: 'bold' }}>
                🎯 Técnica {currentProgress.tecnica_actual} de {currentProgress.progreso.total_tecnicas}
              </h3>
              <p style={{ margin: '5px 0 0 0', fontSize: '14px', opacity: 0.9 }}>
                Contexto del Proyecto
              </p>
            </div>
            <div style={{ 
              background: 'rgba(255,255,255,0.2)', 
              borderRadius: '20px', 
              padding: '8px 16px',
              fontSize: '14px',
              fontWeight: 'bold',
              backdropFilter: 'blur(10px)'
            }}>
              {currentProgress.progreso.porcentaje}% completado
            </div>
          </div>
          
          {/* Barra de progreso mejorada */}
          <div style={{ position: 'relative' }}>
            <div style={{ 
              background: 'rgba(255,255,255,0.2)', 
              borderRadius: '12px', 
              height: '12px',
              overflow: 'hidden'
            }}>
              <div style={{ 
                background: 'linear-gradient(90deg, #4facfe 0%, #00f2fe 100%)', 
                height: '100%', 
                width: `${currentProgress.progreso.porcentaje}%`,
                transition: 'width 0.8s cubic-bezier(0.4, 0, 0.2, 1)',
                borderRadius: '12px',
                boxShadow: '0 2px 8px rgba(79, 172, 254, 0.3)'
              }} />
            </div>
            {/* Indicador de progreso con texto */}
            <div style={{
              position: 'absolute',
              top: '20px',
              left: '0',
              fontSize: '12px',
              opacity: 0.8
            }}>
              {currentProgress.progreso.porcentaje > 0 && (
                <span>✨ Progresando en la extracción de conocimiento</span>
              )}
            </div>
          </div>
        </div>
      )}

      {/* Área de mensajes con animaciones */}
      <div style={{ 
        flex: 1, 
        padding: '20px', 
        overflowY: 'auto',
        background: '#fafbfc'
      }}>
        {messages.map((message, index) => (
          <div 
            key={index} 
            style={{ 
              marginBottom: '24px',
              display: 'flex',
              flexDirection: 'column',
              alignItems: message.sender === 'user' ? 'flex-end' : 'flex-start',
              animation: 'slideIn 0.3s ease-out',
              animationFillMode: 'both',
              animationDelay: `${index * 0.1}s`
            }}
          >
            <div style={{
              background: message.sender === 'user' 
                ? 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)' 
                : 'white',
              color: message.sender === 'user' ? 'white' : '#333',
              padding: '16px 20px',
              borderRadius: '20px',
              maxWidth: '85%',
              boxShadow: message.sender === 'user' 
                ? '0 4px 16px rgba(102, 126, 234, 0.3)' 
                : '0 2px 12px rgba(0,0,0,0.08)',
              border: message.sender === 'assistant' ? '1px solid #f0f0f0' : 'none',
              position: 'relative',
              ...(message.sender === 'user' ? {
                borderBottomRightRadius: '8px'
              } : {
                borderBottomLeftRadius: '8px'
              })
            }}>
              <div style={{ lineHeight: '1.5' }}>{message.content}</div>
              
              {/* Indicador de tipo de mensaje mejorado */}
              {message.type && message.type !== 'respuesta' && (
                <div style={{ 
                  fontSize: '12px', 
                  opacity: 0.8, 
                  marginTop: '8px',
                  fontStyle: 'italic',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '4px'
                }}>
                  {message.type === 'pregunta' && (
                    <>
                      <span style={{ 
                        background: 'rgba(255,255,255,0.2)', 
                        borderRadius: '8px', 
                        padding: '2px 8px',
                        fontSize: '10px'
                      }}>
                        ❓ PREGUNTA
                      </span>
                    </>
                  )}
                  {message.type === 'inicio_sesion' && (
                    <span style={{ 
                      background: 'rgba(40, 167, 69, 0.1)', 
                      color: '#28a745',
                      borderRadius: '8px', 
                      padding: '2px 8px',
                      fontSize: '10px'
                    }}>
                      🎯 BIENVENIDA
                    </span>
                  )}
                  {message.type === 'cambio_tecnica' && (
                    <span style={{ 
                      background: 'rgba(255, 193, 7, 0.1)', 
                      color: '#ffc107',
                      borderRadius: '8px', 
                      padding: '2px 8px',
                      fontSize: '10px'
                    }}>
                      🔄 NUEVA TÉCNICA
                    </span>
                  )}
                  {message.type === 'finalizacion_completa' && (
                    <span style={{ 
                      background: 'rgba(23, 162, 184, 0.1)', 
                      color: '#17a2b8',
                      borderRadius: '8px', 
                      padding: '2px 8px',
                      fontSize: '10px'
                    }}>
                      🎉 ¡COMPLETADO!
                    </span>
                  )}
                </div>
              )}
            </div>
            
            <div style={{ 
              fontSize: '12px', 
              color: '#999', 
              marginTop: '6px',
              marginLeft: message.sender === 'user' ? '0' : '20px',
              marginRight: message.sender === 'user' ? '20px' : '0',
              display: 'flex',
              alignItems: 'center',
              gap: '6px'
            }}>
              <span style={{
                width: '8px',
                height: '8px',
                borderRadius: '50%',
                background: message.sender === 'user' ? '#667eea' : '#28a745'
              }}></span>
              {message.sender === 'user' ? 'Tú' : 'Asistente Vibe Coding'} • {new Date(message.timestamp).toLocaleTimeString()}
            </div>
          </div>
        ))}
        
        {/* Indicador de escritura mejorado */}
        {isLoading && (
          <div style={{ 
            display: 'flex', 
            alignItems: 'center', 
            marginBottom: '20px',
            animation: 'slideIn 0.3s ease-out'
          }}>
            <div style={{
              background: 'white',
              padding: '16px 20px',
              borderRadius: '20px',
              borderBottomLeftRadius: '8px',
              boxShadow: '0 2px 12px rgba(0,0,0,0.08)',
              border: '1px solid #f0f0f0'
            }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                <div style={{ 
                  display: 'flex', 
                  gap: '4px',
                  alignItems: 'center'
                }}>
                  <div style={{ 
                    width: '8px', 
                    height: '8px', 
                    borderRadius: '50%', 
                    background: '#667eea', 
                    animation: 'bounce 1.4s infinite ease-in-out' 
                  }}></div>
                  <div style={{ 
                    width: '8px', 
                    height: '8px', 
                    borderRadius: '50%', 
                    background: '#667eea', 
                    animation: 'bounce 1.4s infinite ease-in-out 0.16s' 
                  }}></div>
                  <div style={{ 
                    width: '8px', 
                    height: '8px', 
                    borderRadius: '50%', 
                    background: '#667eea', 
                    animation: 'bounce 1.4s infinite ease-in-out 0.32s' 
                  }}></div>
                </div>
                <span style={{ color: '#666', fontSize: '14px' }}>
                  El asistente está procesando tu respuesta...
                </span>
              </div>
            </div>
          </div>
        )}
        
        <div ref={messagesEndRef} />
      </div>

      {/* Área de entrada mejorada */}
{/* Área de entrada mejorada */}
      <div style={{ 
        padding: '20px', 
        borderTop: '1px solid #f0f0f0',
        background: 'white'
      }}>
        <div style={{ 
          display: 'flex', 
          gap: '12px', 
          alignItems: 'flex-end',
          width: '100%'
        }}>
          <div style={{ flex: 1 }}>
            <textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Describe tu respuesta aquí... (Presiona Enter para enviar)"
              style={{
                width: '100%',
                padding: '16px 20px',
                border: '2px solid #f0f0f0',
                borderRadius: '16px',
                resize: 'none',
                minHeight: '56px',
                maxHeight: '120px',
                fontSize: '16px',
                outline: 'none',
                transition: 'all 0.2s ease',
                fontFamily: 'inherit',
                backgroundColor: '#fafbfc',
                boxSizing: 'border-box'
              }}
              onFocus={(e) => {
                e.target.style.borderColor = '#667eea';
                e.target.style.backgroundColor = 'white';
                e.target.style.boxShadow = '0 0 0 3px rgba(102, 126, 234, 0.1)';
              }}
              onBlur={(e) => {
                e.target.style.borderColor = '#f0f0f0';
                e.target.style.backgroundColor = '#fafbfc';
                e.target.style.boxShadow = 'none';
              }}
              disabled={isLoading}
            />
          </div>
          <div>
            <button
              onClick={handleSendMessage}
              disabled={!input.trim() || isLoading}
              style={{
                padding: '16px 24px',
                background: input.trim() && !isLoading 
                  ? 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)' 
                  : '#e0e0e0',
                color: input.trim() && !isLoading ? 'white' : '#999',
                border: 'none',
                borderRadius: '16px',
                cursor: input.trim() && !isLoading ? 'pointer' : 'not-allowed',
                fontWeight: 'bold',
                fontSize: '16px',
                transition: 'all 0.2s ease',
                height: '56px',
                whiteSpace: 'nowrap',
                boxShadow: input.trim() && !isLoading 
                  ? '0 4px 16px rgba(102, 126, 234, 0.3)' 
                  : 'none'
              }}
            >
              {isLoading ? '⏳' : '📤'} Enviar
            </button>
          </div>
        </div>
      </div>

      {/* Estilos CSS en línea para animaciones */}
      <style>{`
        @keyframes slideIn {
          from {
            opacity: 0;
            transform: translateY(20px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
        
        @keyframes bounce {
          0%, 80%, 100% {
            transform: scale(0);
          }
          40% {
            transform: scale(1);
          }
        }
        
        @keyframes pulse {
          0% {
            transform: scale(1);
          }
          50% {
            transform: scale(1.1);
          }
          100% {
            transform: scale(1);
          }
        }
      `}</style>
    </div>
  );
}

export default ConversationArea;
