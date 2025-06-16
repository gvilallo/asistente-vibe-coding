from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import uvicorn
import os

# Cargar variables de entorno
load_dotenv()

# Crear la aplicación FastAPI
app = FastAPI(title="Asistente de Vibe Coding API")

# Configurar CORS para permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Endpoint de prueba para verificar que la API está funcionando"""
    return {"message": "Bienvenido a la API del Asistente de Vibe Coding"}

# Aquí agregaremos más endpoints más adelante

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)
from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
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

# Configurar CORS para permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Almacenamiento temporal hasta que implementemos MongoDB
# En una aplicación real, esto estaría en la base de datos
projects_db = {}
sessions_db = {}

@app.get("/")
async def root():
    """Endpoint de prueba para verificar que la API está funcionando"""
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
    """Crea una nueva sesión para un proyecto"""
    if project_id not in projects_db:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado")
        
    session_id = f"sess_{len(sessions_db) + 1}"
    session_data = session.dict()
    session_data["id"] = session_id
    session_data["project_id"] = project_id
    session_data["created_at"] = datetime.now().isoformat()
    session_data["messages"] = []
    session_data["state"] = {
        "tecnica_actual": 0,
        "pregunta_actual": 0,
        "completado": False,
        "conocimiento": {}
    }
    
    sessions_db[session_id] = session_data
    
    # Mensaje de bienvenida
    sessions_db[session_id]["messages"].append({
        "sender": "assistant",
        "content": "Bienvenido al asistente de Vibe Coding. ¿Cuál es el objetivo principal de este proyecto?",
        "timestamp": datetime.now().isoformat(),
        "type": "introduccion"
    })
    
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
    """Procesa una interacción del usuario con la sesión"""
    if session_id not in sessions_db:
        raise HTTPException(status_code=404, detail="Sesión no encontrada")
    
    # Obtener el contenido del mensaje
    content = request.get("content", "")
    if not content:
        raise HTTPException(status_code=400, detail="El mensaje no puede estar vacío")
    
    # Guardar mensaje del usuario
    sessions_db[session_id]["messages"].append({
        "sender": "user",
        "content": content,
        "timestamp": datetime.now().isoformat()
    })
    
    # Simulación básica de respuesta del asistente (para MVP)
    # En la implementación real, esto usaría el Motor de Extracción
    response = {
        "sender": "assistant",
        "content": f"He recibido tu mensaje: '{content}'. Esta es una respuesta simulada para el MVP.",
        "timestamp": datetime.now().isoformat(),
        "type": "respuesta"
    }
    
    # Guardar respuesta del asistente
    sessions_db[session_id]["messages"].append(response)
    
    return response

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)
