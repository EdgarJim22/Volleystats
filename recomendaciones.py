"""================================================================================================
Date: 9/11/2024
Owner......: Edgar Enrique Jimenez Hernández
Title......: `recomendaciones.py`
Function...: Proporciona recomendaciones para un jugador basadas en su rol y estadísticas.
Python.....: 3.8+
================================================================================================"""

import pandas as pd

# Recomendaciones en función del rol
def dar_recomendaciones(jugador):
    recomendaciones = []
    
    if jugador["rol"] == "Punta/Atacante lateral":
        recomendaciones.append("Debes enfocarte en la recepción y el ataque.")
    elif jugador["rol"] == "Central":
        recomendaciones.append("Mejora tu capacidad de bloqueo y el juego en el centro de la red.")
    elif jugador["rol"] == "Opuesto":
        recomendaciones.append("Tu principal objetivo debe ser el remate y el bloqueo.")
    elif jugador["rol"] == "Colocador":
        recomendaciones.append("Debes mejorar tu visión de juego y distribuir mejor el balón.")
    elif jugador["rol"] == "Libero":
        recomendaciones.append("Debes enfocarte en la defensa y recepción de saques difíciles.")
    
    # Recomendaciones por estatura
    if jugador["altura"] <= 1.80:
        recomendaciones.append("Trabaja en tu pliometría para mejorar el salto.")
    elif jugador["altura"] > 1.80 and jugador["altura"] <= 1.95:
        recomendaciones.append("Aprovecha tu estatura para mejorar el bloqueo y el remate.")
    else:
        recomendaciones.append("Tu altura es una ventaja, centrándote en el bloqueo y remate.")
    
    # Recomendaciones según IMC
    imc = jugador["peso"] / (jugador["altura"] ** 2)
    if imc < 18.5:
        recomendaciones.append("Tu IMC es bajo, enfócate en ganar masa muscular.")
    elif 18.5 <= imc <= 24.9:
        recomendaciones.append("Tu IMC es ideal, mantén tu dieta y entrenamiento.")
    else:
        recomendaciones.append("Tu IMC es alto, deberías reducir peso para mejorar tu agilidad.")
    
    return recomendaciones