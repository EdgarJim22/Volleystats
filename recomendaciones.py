from atletas import df_jugadores

def dar_recomendaciones(nombre):
    """Da recomendaciones personalizadas basadas en el rol y puntos fuertes/débiles."""
    jugador = df_jugadores[df_jugadores["nombre"] == nombre].iloc[0]
    rol = jugador["rol"]
    puntos_fuertes = jugador["puntos_fuertes"]
    puntos_debiles = jugador["puntos_debiles"]

    print(f"\nRecomendaciones para {nombre} ({rol}):")

    # Recomendaciones para puntos fuertes
    print(f"- Fortalecer punto fuerte ({puntos_fuertes}): Realiza ejercicios específicos para mantener tu rendimiento en {puntos_fuertes}.")

    # Recomendaciones para puntos débiles
    if puntos_debiles == "defensa":
        print("- Mejora en defensa: Trabaja en velocidad de reacción y desplazamientos laterales.")
    elif puntos_debiles == "movilidad lateral":
        print("- Mejora en movilidad lateral: Realiza ejercicios de agilidad para aumentar velocidad en desplazamientos.")
    elif puntos_debiles == "salto":
        print("- Mejora en salto: Enfócate en ejercicios pliométricos para mejorar la altura y resistencia de tus saltos.")
