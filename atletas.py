"""================================================================================================
Date: 9/11/2024
Owner......: Edgar Enrique Jimenez Hernández
Title......: `atletas.py`
Function...: Maneja el registro de jugadores y equipos, y persiste los datos en un archivo CSV.
Python.....: 3.8+
================================================================================================"""

import pandas as pd
import os

# Crear el DataFrame de jugadores y cargar datos si existe el archivo
df_jugadores = pd.DataFrame(columns=["nombre", "rol", "altura", "peso", "alcance_remate", "alcance_bloqueo", "equipo"])
archivo_jugadores = "jugadores.csv"

if os.path.exists(archivo_jugadores):
    df_jugadores = pd.read_csv(archivo_jugadores)

# Función para verificar si el jugador ya existe
def jugador_existe(nombre, rol, equipo):
    return not df_jugadores[(df_jugadores["nombre"] == nombre) & (df_jugadores["rol"] == rol) & (df_jugadores["equipo"] == equipo)].empty

# Función para crear un jugador y guardar los datos
def crear_jugador(nombre, rol, altura, peso, alcance_remate, alcance_bloqueo, equipo):
    if jugador_existe(nombre, rol, equipo):
        return False  # Si el jugador ya existe, no lo registramos.

    nuevo_jugador = {
        "nombre": nombre,
        "rol": rol,
        "altura": altura,
        "peso": peso,
        "alcance_remate": alcance_remate,
        "alcance_bloqueo": alcance_bloqueo,
        "equipo": equipo
    }

    global df_jugadores
    df_jugadores = pd.concat([df_jugadores, pd.DataFrame([nuevo_jugador])], ignore_index=True)
    df_jugadores.to_csv(archivo_jugadores, index=False)
    return True

# Función para obtener jugadores
def obtener_jugadores(equipo=None):
    if equipo:
        return df_jugadores[df_jugadores["equipo"] == equipo].to_dict(orient="records")
    return df_jugadores.to_dict(orient="records")

# Función para obtener un jugador por su nombre
def obtener_jugador(nombre):
    jugador = df_jugadores[df_jugadores["nombre"] == nombre]
    if not jugador.empty:
        return jugador.iloc[0].to_dict()
    return None