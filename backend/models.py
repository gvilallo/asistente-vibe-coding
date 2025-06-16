from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime

class Project(BaseModel):
    name: str
    description: str
    domain: str
    created_by: str
    
class Session(BaseModel):
    name: str
    description: Optional[str] = None
    project_id: Optional[str] = None
    
class Message(BaseModel):
    content: str
    sender: str = "user"  # "user" o "assistant"
    timestamp: Optional[datetime] = None
    
class InteractionRequest(BaseModel):
    content: str
    session_id: str
    
class VisualizationRequest(BaseModel):
    type: str
    context: Optional[Dict[str, Any]] = None
