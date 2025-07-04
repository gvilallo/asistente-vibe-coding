"""
Definición completa de las 12 técnicas de extracción del Framework de Vibe Coding.
"""

TECNICAS = [
    {
        "id": "contexto_proyecto",
        "nombre": "Contexto del Proyecto",
        "orden": 1,
        "introduccion": "Para comenzar, me gustaría entender mejor el contexto general del proyecto que estamos analizando.",
        "preguntas": [
            "¿Cuál es el objetivo principal de este proyecto?",
            "¿Quiénes serían los principales usuarios o beneficiarios?",
            "¿Qué problema o desafío actual estás tratando de resolver con esta solución?"
        ]
    },
    {
        "id": "mapeo_ecosistema", 
        "nombre": "Mapeo de Ecosistema",
        "orden": 2,
        "introduccion": "Ahora, me gustaría entender mejor cómo este sistema se conectaría con su entorno.",
        "preguntas": [
            "¿Con qué otros sistemas o aplicaciones debería comunicarse esta solución?",
            "Pensando en todas las personas que interactuarían con el sistema, ¿quiénes serían?",
            "¿Hay procesos externos que el sistema debería integrar o considerar?"
        ]
    }
]

def obtener_tecnica_por_orden(orden):
    """Obtiene una técnica específica por su orden de ejecución"""
    for tecnica in TECNICAS:
        if tecnica["orden"] == orden:
            return tecnica
    return None

def obtener_total_tecnicas():
    """Retorna el número total de técnicas"""
    return len(TECNICAS)
