from atletas import crear_jugador, mostrar_jugadores
from estadisticas import registrar_rendimiento, analizar_rendimiento

# Crear algunos jugadores
crear_jugador("Juan", "Atacante lateral", 1.75, 70, "remate", "defensa")
crear_jugador("Pedro", "Central", 1.99, 85, "bloqueo", "movilidad lateral")
crear_jugador("Luis", "Libero", 1.80, 65, "defensa", "salto")

# Mostrar jugadores disponibles
mostrar_jugadores()

# Registrar rendimiento para un jugador
registrar_rendimiento("Juan", saltos=25, velocidad=8.5, reaccion=0.5, precision=80)
registrar_rendimiento("Juan", saltos=28, velocidad=8.7, reaccion=0.6, precision=82)

# Analizar rendimiento de un jugador
analizar_rendimiento("Juan")
