"""================================================================================================
Date: 9/11/2024
Owner......: Edgar Enrique Jimenez Hernández
Title......: `estadisticas.py`
Function...: Analiza las estadísticas del jugador y proporciona recomendaciones.
Python.....: 3.8+
================================================================================================"""

import pandas as pd
from atletas import obtener_jugador

# Función para calcular el IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Función para dar recomendaciones en base al rol
def dar_recomendaciones(jugador):
    recomendaciones = []
    
    if jugador["rol"] == "Punta/Atacante lateral":
        recomendaciones.append("Debes centrarte en la recepción y el ataque.")
    elif jugador["rol"] == "Central":
        recomendaciones.append("Debes mejorar tu capacidad de bloqueo y tu juego en el centro de la red.")
    elif jugador["rol"] == "Opuesto":
        recomendaciones.append("Tu principal objetivo debe ser el remate y el bloqueo.")
    elif jugador["rol"] == "Colocador":
        recomendaciones.append("Mejora tu visión de juego y tu capacidad para distribuir el balón.")
    elif jugador["rol"] == "Libero":
        recomendaciones.append("Debes enfocarte en la defensa y en la recepción de saques difíciles.")
    
    # Recomendaciones en base a la estatura
    if jugador["altura"] <= 1.80:
        recomendaciones.append("Debes trabajar en tu pliometría para mejorar el salto.")
    elif jugador["altura"] > 1.80 and jugador["altura"] <= 1.90:
        recomendaciones.append("Aprovecha tu estatura para mejorar el bloqueo y el remate.")
    else:
        recomendaciones.append("Con tu altura, el bloqueo y el remate deben ser tu prioridad.")
    
    # Recomendaciones en base al IMC
    imc = calcular_imc(jugador["peso"], jugador["altura"])
    if imc < 18.5:
        recomendaciones.append("Tu IMC es bajo, debes aumentar tu peso, enfocándote en ganar músculo.")
    elif imc >= 18.5 and imc <= 24.9:
        recomendaciones.append("Tu IMC es ideal, sigue manteniéndote en forma con entrenamiento adecuado.")
    else:
        recomendaciones.append("Tu IMC es alto, considera reducir el peso para mejorar tu agilidad y resistencia.")
    
    return recomendaciones

# Función para analizar el rendimiento de un jugador
def analizar_rendimiento(nombre):
    jugador = obtener_jugador(nombre)
    if jugador is not None:
        recomendaciones = dar_recomendaciones(jugador)
        return recomendaciones
    else:
        return "Jugador no encontrado."