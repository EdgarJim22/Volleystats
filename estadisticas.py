import pandas as pd
from recomendaciones import dar_recomendaciones

def registrar_rendimiento(nombre, saltos, velocidad, reaccion, precision):
    """Registra el rendimiento diario de un jugador."""
    data = {
        "nombre": nombre,
        "saltos": saltos,
        "velocidad": velocidad,
        "reaccion": reaccion,
        "precision": precision
    }
    rendimiento_df = pd.DataFrame([data])
    rendimiento_df.to_csv(f"rendimiento_{nombre}.csv", mode='a', header=False, index=False)
    print(f"Rendimiento registrado para {nombre}.")

def analizar_rendimiento(nombre):
    """Analiza el rendimiento promedio de un jugador y da recomendaciones."""
    rendimiento_df = pd.read_csv(f"rendimiento_{nombre}.csv", names=["nombre", "saltos", "velocidad", "reaccion", "precision"])

    # Calcular promedios
    promedio_saltos = rendimiento_df["saltos"].mean()
    promedio_velocidad = rendimiento_df["velocidad"].mean()
    promedio_reaccion = rendimiento_df["reaccion"].mean()
    promedio_precision = rendimiento_df["precision"].mean()

    print(f"\nAnálisis de rendimiento para {nombre}:")
    print(f"Saltos promedio: {promedio_saltos}")
    print(f"Velocidad promedio: {promedio_velocidad}")
    print(f"Reacción promedio: {promedio_reaccion}")
    print(f"Precisión promedio: {promedio_precision}")

    # Llamamos a la función de recomendaciones
    dar_recomendaciones(nombre)
