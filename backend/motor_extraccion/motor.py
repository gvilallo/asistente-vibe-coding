"""
Motor de Extracción simplificado para pruebas iniciales
"""

from .tecnicas import TECNICAS, obtener_tecnica_por_orden, obtener_total_tecnicas
from datetime import datetime
from typing import Dict, Any, Optional

class MotorExtraccion:
    def __init__(self):
        self.tecnicas = TECNICAS
        self.estado = {
            "tecnica_actual": 1,
            "pregunta_actual": 0,
            "completado": False,
            "conocimiento_extraido": {},
            "sesion_iniciada": False
        }
        
    def iniciar_sesion(self, contexto_previo: Optional[Dict] = None) -> Dict[str, Any]:
        self.estado["sesion_iniciada"] = True
        tecnica_inicial = obtener_tecnica_por_orden(1)
        
        return {
            "tipo": "inicio_sesion",
            "mensaje": f"¡Bienvenido al proceso de Vibe Coding! {tecnica_inicial['introduccion']}",
            "tecnica_actual": tecnica_inicial["nombre"],
            "progreso": self._calcular_progreso(),
            "primera_pregunta": tecnica_inicial["preguntas"][0]
        }
    
    def procesar_respuesta(self, respuesta: str) -> Dict[str, Any]:
        if not self.estado["sesion_iniciada"]:
            return {"error": "La sesión no ha sido iniciada"}
        
        self._guardar_respuesta(respuesta)
        return self._determinar_siguiente_accion()
    
    def _guardar_respuesta(self, respuesta: str) -> None:
        self.estado["pregunta_actual"] += 1
    
    def _determinar_siguiente_accion(self) -> Dict[str, Any]:
        tecnica_actual = obtener_tecnica_por_orden(self.estado["tecnica_actual"])
        
        if self.estado["pregunta_actual"] >= len(tecnica_actual["preguntas"]):
            return self._completar_tecnica_actual()
        
        return self._generar_siguiente_pregunta()
    
    def _completar_tecnica_actual(self) -> Dict[str, Any]:
        self.estado["tecnica_actual"] += 1
        self.estado["pregunta_actual"] = 0
        
        if self.estado["tecnica_actual"] > obtener_total_tecnicas():
            self.estado["completado"] = True
            return {
                "tipo": "finalizacion_completa",
                "mensaje": "¡Completamos las técnicas disponibles!",
                "progreso": 100
            }
        
        nueva_tecnica = obtener_tecnica_por_orden(self.estado["tecnica_actual"])
        return {
            "tipo": "cambio_tecnica",
            "mensaje": f"Pasemos a '{nueva_tecnica['nombre']}':\n\n{nueva_tecnica['introduccion']}",
            "nueva_tecnica": nueva_tecnica["nombre"],
            "progreso": self._calcular_progreso(),
            "primera_pregunta_nueva": nueva_tecnica["preguntas"][0]
        }
    
    def _generar_siguiente_pregunta(self) -> Dict[str, Any]:
        tecnica_actual = obtener_tecnica_por_orden(self.estado["tecnica_actual"])
        pregunta = tecnica_actual["preguntas"][self.estado["pregunta_actual"]]
        
        return {
            "tipo": "pregunta",
            "mensaje": pregunta,
            "tecnica_actual": tecnica_actual["nombre"],
            "progreso": self._calcular_progreso()
        }
    
    def _calcular_progreso(self) -> Dict[str, Any]:
        total_tecnicas = obtener_total_tecnicas()
        tecnicas_completadas = self.estado["tecnica_actual"] - 1
        
        if self.estado["completado"]:
            porcentaje = 100
        else:
            porcentaje = (tecnicas_completadas / total_tecnicas) * 100
        
        return {
            "porcentaje": min(100, round(porcentaje, 1)),
            "tecnica_actual": self.estado["tecnica_actual"],
            "total_tecnicas": total_tecnicas
        }
    
    def obtener_estado_completo(self) -> Dict[str, Any]:
        return self.estado.copy()
    
    def generar_super_prompt(self) -> Dict[str, Any]:
        return {"mensaje": "Super prompt generado (versión demo)"}
