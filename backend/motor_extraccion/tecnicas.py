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
    },
    {
        "id": "flujos_trabajo",
        "nombre": "Flujos de Trabajo Visuales", 
        "orden": 3,
        "introduccion": "Ahora me gustaría entender cómo fluye el trabajo y los procesos en tu dominio.",
        "preguntas": [
            "¿Podrías describir el proceso completo desde que se inicia una operación hasta que se completa?",
            "¿Cuáles son los puntos de decisión más importantes en estos procesos?",
            "¿Qué información necesita cada paso del proceso para poder ejecutarse correctamente?"
        ]
    },
    {
        "id": "descomposicion_modular",
        "nombre": "Descomposición Modular",
        "orden": 4, 
        "introduccion": "Pensemos en cómo podríamos dividir lógicamente tu sistema en componentes independientes.",
        "preguntas": [
            "Si tuvieras que dividir tu sistema en 'departamentos' o áreas funcionales, ¿cuáles serían?",
            "¿Qué partes del sistema deberían poder cambiar sin afectar a otras?",
            "¿Qué áreas comparten información similar o trabajan con los mismos tipos de datos?"
        ]
    },
    {
        "id": "escenarios_adaptacion",
        "nombre": "Escenarios de Adaptación",
        "orden": 5,
        "introduccion": "Es importante entender cómo el sistema debería adaptarse a cambios futuros.",
        "preguntas": [
            "¿Cómo crees que podrían cambiar los requisitos en el próximo año?",
            "Si tu organización creciera significativamente, ¿qué aspectos del sistema deberían adaptarse?",
            "¿Qué componentes necesitarían ser personalizables por diferentes tipos de usuarios?"
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
