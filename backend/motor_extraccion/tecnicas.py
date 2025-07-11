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
    },
    {
        "id": "analisis_volumen",
        "nombre": "Análisis de Volumen y Criticidad",
        "orden": 6,
        "introduccion": "Ahora necesito entender qué procesos son más críticos y manejan mayor volumen de información.",
        "preguntas": [
            "¿Qué procesos o operaciones manejan el mayor volumen de información en tu sistema?",
            "¿Qué operaciones son críticas y no pueden fallar bajo ninguna circunstancia?",
            "¿Qué operaciones necesitan respuesta inmediata vs. cuáles pueden procesarse en segundo plano?"
        ]
    },
    {
        "id": "patrones_acceso",
        "nombre": "Patrones de Acceso a Datos",
        "orden": 7,
        "introduccion": "Es importante entender cómo se accede y modifica la información en tu dominio.",
        "preguntas": [
            "Para cada tipo de información importante, ¿con qué frecuencia se consulta vs. se modifica?",
            "¿Quién necesita acceso a cada tipo de información y con qué propósito?",
            "¿Qué información necesita estar disponible en tiempo real vs. puede tener retrasos?"
        ]
    },
    {
        "id": "requisitos_no_funcionales",
        "nombre": "Requisitos No Funcionales",
        "orden": 8,
        "introduccion": "Ahora me gustaría conocer tus expectativas sobre el funcionamiento general del sistema, más allá de lo que hace: cómo debe comportarse en cuanto a rapidez, disponibilidad y seguridad.",
        "preguntas": [
            "¿Qué tan rápido esperas que el sistema responda cuando lo usas en situaciones normales?",
            "¿En qué situaciones sería inaceptable que el sistema deje de funcionar o no esté disponible?",
            "¿Hay alguna preocupación sobre la seguridad o privacidad de la información que el sistema manejará?"
        ]
    },
    {
        "id": "gestion_estado",
        "nombre": "Gestión de Estado",
        "orden": 9,
        "introduccion": "Ahora me gustaría saber cómo esperas que el sistema recuerde o gestione información entre diferentes usos o sesiones.",
        "preguntas": [
            "¿Hay información que deba mantenerse igual aunque cierres y vuelvas a abrir el sistema?",
            "¿Qué datos deberían recordarse automáticamente para cada usuario entre diferentes sesiones de uso?",
            "¿En qué situaciones sería importante que el sistema ‘olvide’ o reinicie cierta información?"
        ]
    },
    {
        "id": "restricciones_tecnologicas",
        "nombre": "Restricciones Tecnológicas",
        "orden": 10,
        "introduccion": "Quisiera conocer si existen preferencias o limitaciones respecto a las tecnologías, plataformas o herramientas que debe usar el sistema.",
        "preguntas": [
            "¿El sistema debe funcionar en algún dispositivo, sistema operativo o navegador específico?",
            "¿Hay alguna herramienta, plataforma o tecnología que prefieras evitar o que sea obligatoria usar?",
            "¿El sistema debe integrarse con alguna tecnología o sistema que ya usas actualmente?"
        ]
    },
    {
        "id": "ciclo_vida_datos",
        "nombre": "Ciclo de Vida de Datos",
        "orden": 11,
        "introduccion": "Me gustaría entender cómo debería manejarse la información a lo largo del tiempo dentro del sistema.",
        "preguntas": [
            "¿Qué información es importante guardar por mucho tiempo y cuál puede eliminarse después de un periodo?",
            "¿Hay datos que deban actualizarse automáticamente o eliminarse bajo ciertas condiciones?",
            "¿Quién debería poder ver, modificar o eliminar la información en diferentes etapas de su vida útil?"
        ]
    },
    {
        "id": "priorizacion_cualidades",
        "nombre": "Priorización de Cualidades",
        "orden": 12,
        "introduccion": "Por último, quiero saber qué cualidades valoras más en el sistema para poder priorizarlas en el desarrollo.",
        "preguntas": [
            "Si tuvieras que elegir, ¿qué es más importante para ti: que el sistema sea rápido, seguro o fácil de usar?",
            "¿En qué situaciones aceptarías sacrificar facilidad de uso por mayor seguridad, o viceversa?",
            "¿Qué aspecto del sistema te generaría más problemas si no funcionara bien?"
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
