from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from motor_extraccion.motor import MotorExtraccion
from models import InteractionRequest, Project, Session
import uvicorn
import os
import json
from datetime import datetime
from typing import Dict, Any

# Cargar variables de entorno
load_dotenv()

# Crear la aplicación FastAPI
app = FastAPI(title="Asistente de Vibe Coding API")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Almacenamiento temporal (en memoria)
projects_db = {}
sessions_db = {}
motors_db = {}  # Almacena instancias del motor por sesión

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API del Asistente de Vibe Coding"}

@app.post("/projects/")
async def create_project(project: Project):
    """Crea un nuevo proyecto"""
    project_id = f"proj_{len(projects_db) + 1}"
    project_data = project.dict()
    project_data["id"] = project_id
    project_data["created_at"] = datetime.now().isoformat()
    
    projects_db[project_id] = project_data
    return project_data

@app.get("/projects/")
async def list_projects():
    """Lista todos los proyectos"""
    return list(projects_db.values())

@app.get("/projects/{project_id}")
async def get_project(project_id: str):
    """Obtiene un proyecto por su ID"""
    if project_id not in projects_db:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
    return projects_db[project_id]

@app.post("/projects/{project_id}/sessions/")
async def create_session(project_id: str, session: Session):
    """Crea una nueva sesión de extracción para un proyecto"""
    if project_id not in projects_db:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
        
    session_id = f"sess_{len(sessions_db) + 1}"
    session_data = session.dict()
    session_data["id"] = session_id
    session_data["project_id"] = project_id
    session_data["created_at"] = datetime.now().isoformat()
    session_data["messages"] = []
    session_data["status"] = "iniciando"
    
    # Crear instancia del Motor de Extracción para esta sesión
    motor = MotorExtraccion()
    motors_db[session_id] = motor
    
    # Iniciar el proceso de extracción
    intro_response = motor.iniciar_sesion()
    
    # Guardar mensaje inicial del asistente
    session_data["messages"].append({
        "sender": "assistant",
        "content": intro_response["mensaje"],
        "timestamp": datetime.now().isoformat(),
        "type": intro_response["tipo"],
        "metadata": {
            "tecnica_actual": intro_response.get("tecnica_actual"),
            "progreso": intro_response.get("progreso"),
            "primera_pregunta": intro_response.get("primera_pregunta")
        }
    })
    
    # Agregar la primera pregunta como mensaje separado
    if "primera_pregunta" in intro_response:
        session_data["messages"].append({
            "sender": "assistant", 
            "content": intro_response["primera_pregunta"],
            "timestamp": datetime.now().isoformat(),
            "type": "pregunta",
            "metadata": {
                "tecnica_actual": intro_response.get("tecnica_actual"),
                "progreso": intro_response.get("progreso")
            }
        })
    
    session_data["status"] = "activa"
    sessions_db[session_id] = session_data
    
    return session_data

@app.get("/sessions/{session_id}")
async def get_session(session_id: str):
    """Obtiene una sesión por su ID"""
    if session_id not in sessions_db:
        raise HTTPException(status_code=404, detail="Sesión no encontrada")
    return sessions_db[session_id]

@app.get("/sessions/{session_id}/messages")
async def get_session_messages(session_id: str):
    """Obtiene los mensajes de una sesión"""
    if session_id not in sessions_db:
        raise HTTPException(status_code=404, detail="Sesión no encontrada")
    return sessions_db[session_id]["messages"]

@app.post("/sessions/{session_id}/interact")
async def process_interaction(session_id: str, request: Dict[str, Any] = Body(...)):
    """Procesa una interacción del usuario con el Motor de Extracción"""
    if session_id not in sessions_db:
        raise HTTPException(status_code=404, detail="Sesión no encontrada")
    
    if session_id not in motors_db:
        raise HTTPException(status_code=500, detail="Motor de extracción no encontrado")
    
    content = request.get("content", "")
    if not content.strip():
        raise HTTPException(status_code=400, detail="El mensaje no puede estar vacío")
    
    # Guardar mensaje del usuario
    user_message = {
        "sender": "user",
        "content": content,
        "timestamp": datetime.now().isoformat()
    }
    sessions_db[session_id]["messages"].append(user_message)
    
    # Procesar con el Motor de Extracción
    motor = motors_db[session_id]
    response = motor.procesar_respuesta(content)
    
    # Crear mensaje de respuesta del asistente
    assistant_message = {
        "sender": "assistant",
        "content": response.get("mensaje", ""),
        "timestamp": datetime.now().isoformat(),
        "type": response.get("tipo", "respuesta"),
        "metadata": {
            "tecnica_actual": response.get("tecnica_actual"),
            "progreso": response.get("progreso"),
            "pregunta_numero": response.get("pregunta_numero"),
            "total_preguntas_tecnica": response.get("total_preguntas_tecnica"),
            "opciones": response.get("opciones"),
            "visualizacion_tipo": response.get("visualizacion_tipo")
        }
    }
    
    # Guardar respuesta del asistente
    sessions_db[session_id]["messages"].append(assistant_message)
    
    # Actualizar estado de la sesión
    if response.get("tipo") == "finalizacion_completa":
        sessions_db[session_id]["status"] = "completada"
    
    return assistant_message

@app.post("/sessions/{session_id}/visualize")
async def handle_visualization_response(session_id: str, request: Dict[str, Any] = Body(...)):
    """Maneja la respuesta del usuario a una oferta de visualización"""
    if session_id not in sessions_db:
        raise HTTPException(status_code=404, detail="Sesión no encontrada")
    
    if session_id not in motors_db:
        raise HTTPException(status_code=500, detail="Motor de extracción no encontrado")
    
    opcion = request.get("opcion", "")
    
    # Procesar respuesta de visualización
    if "sí" in opcion.lower() or "si" in opcion.lower():
        # Aquí implementaríamos la generación real de la visualización
        # Por ahora, simulamos la respuesta
        response_message = {
            "sender": "assistant",
            "content": "Aquí tienes la visualización solicitada. ¿Te parece que refleja correctamente lo que has descrito?",
            "timestamp": datetime.now().isoformat(),
            "type": "visualizacion_generada",
            "metadata": {
                "visualizacion_tipo": request.get("tipo", "generico"),
                "visualizacion_data": "datos_de_ejemplo"
            }
        }
    else:
        response_message = {
            "sender": "assistant", 
            "content": "Perfecto, continuemos con las preguntas.",
            "timestamp": datetime.now().isoformat(),
            "type": "continuar"
        }
    
    # Guardar respuesta
    sessions_db[session_id]["messages"].append(response_message)
    
    return response_message

@app.get("/sessions/{session_id}/progress")
async def get_session_progress(session_id: str):
    """Obtiene el progreso actual de una sesión"""
    if session_id not in sessions_db:
        raise HTTPException(status_code=404, detail="Sesión no encontrada")
    
    if session_id not in motors_db:
        raise HTTPException(status_code=500, detail="Motor de extracción no encontrado")
    
    motor = motors_db[session_id]
    estado = motor.obtener_estado_completo()
    
    return {
        "progreso": motor._calcular_progreso(),
        "tecnica_actual": estado.get("tecnica_actual"),
        "pregunta_actual": estado.get("pregunta_actual"),
        "completado": estado.get("completado", False),
        "tecnicas_completadas": len(estado.get("conocimiento_extraido", {}))
    }

@app.post("/sessions/{session_id}/generate-super-prompt")
async def generate_super_prompt(session_id: str):
    """Genera el super prompt basado en el conocimiento extraído"""
    if session_id not in sessions_db:
        raise HTTPException(status_code=404, detail="Sesión no encontrada")
    
    if session_id not in motors_db:
        raise HTTPException(status_code=500, detail="Motor de extracción no encontrado")
    
    motor = motors_db[session_id]
    super_prompt = motor.generar_super_prompt()
    
    if "error" in super_prompt:
        raise HTTPException(status_code=400, detail=super_prompt["error"])
    
    return super_prompt

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)

@app.post("/demo/create-session")
async def create_demo_session():
    """Crea una sesión demo para probar el sistema"""
    # Crear proyecto demo
    demo_project = {
        "id": "demo",
        "name": "Proyecto Demo - Vibe Coding",
        "description": "Sesión de demostración del Framework de Vibe Coding",
        "domain": "Educativo",
        "created_by": "Sistema Demo",
        "created_at": datetime.now().isoformat()
    }
    projects_db["demo"] = demo_project
    
    # Crear sesión demo
    session_data = {
        "id": "demo",
        "name": "Sesión Demo",
        "description": "Demostración del proceso de extracción",
        "project_id": "demo",
        "created_at": datetime.now().isoformat(),
        "messages": [],
        "status": "iniciando"
    }
    
    # Crear motor de extracción
    motor = MotorExtraccion()
    motors_db["demo"] = motor
    
    # Iniciar proceso
    intro_response = motor.iniciar_sesion()
    
    # Agregar mensajes iniciales
    session_data["messages"].append({
        "sender": "assistant",
        "content": intro_response["mensaje"],
        "timestamp": datetime.now().isoformat(),
        "type": intro_response["tipo"],
        "metadata": {
            "tecnica_actual": intro_response.get("tecnica_actual"),
            "progreso": intro_response.get("progreso"),
            "primera_pregunta": intro_response.get("primera_pregunta")
        }
    })
    
    if "primera_pregunta" in intro_response:
        session_data["messages"].append({
            "sender": "assistant",
            "content": intro_response["primera_pregunta"],
            "timestamp": datetime.now().isoformat(),
            "type": "pregunta",
            "metadata": {
                "tecnica_actual": intro_response.get("tecnica_actual"),
                "progreso": intro_response.get("progreso")
            }
        })
    
    session_data["status"] = "activa"
    sessions_db["demo"] = session_data
    
    return session_data

