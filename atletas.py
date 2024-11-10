import pandas as pd

# Base de datos inicial de jugadores
jugadores = {
    "nombre": [],
    "rol": [],
    "altura": [],
    "peso": [],
    "puntos_fuertes": [],
    "puntos_debiles": []
}

# Convertimos a DataFrame
df_jugadores = pd.DataFrame(jugadores)

def crear_jugador(nombre, rol, altura, peso, puntos_fuertes, puntos_debiles):
    """Agrega un nuevo jugador al DataFrame."""
    global df_jugadores
    nuevo_jugador = {
        "nombre": nombre,
        "rol": rol,
        "altura": altura,
        "peso": peso,
        "puntos_fuertes": puntos_fuertes,
        "puntos_debiles": puntos_debiles
    }
    df_jugadores = df_jugadores.append(nuevo_jugador, ignore_index=True)
    print(f"Jugador {nombre} creado.")

def mostrar_jugadores():
    """Muestra todos los jugadores registrados."""
    print("\nJugadores Registrados:")
    print(df_jugadores)
