import tkinter as tk
from tkinter import messagebox, Button, Label
from tkinter.ttk import Combobox
import pygame
from ffpyplayer.player import MediaPlayer
from atletas import crear_jugador, obtener_jugadores, obtener_jugador
from recomendaciones import dar_recomendaciones

equipos = ["Equipo A", "Equipo B", "Equipo C"]

def ventana_principal():
    # Configuración de la ventana principal
    root = tk.Tk()
    root.title("Sistema de Registro de Jugadores")
    root.geometry("800x600")
    modo_oscuro = False

    # Cambio entre modos oscuro y claro
    def alternar_modo():
        nonlocal modo_oscuro
        modo_oscuro = not modo_oscuro
        color_bg = "black" if modo_oscuro else "white"
        color_fg = "white" if modo_oscuro else "black"
        root.config(bg=color_bg)
        for widget in root.winfo_children():
            widget.config(bg=color_bg, fg=color_fg)

    # Ventana para registrar un nuevo jugador
    def ventana_registrar_jugador():
        ventana = tk.Toplevel(root)
        ventana.title("Registrar Jugador")
        ventana.geometry("800x600")

        def registrar():
            nombre = entry_nombre.get()
            rol = combo_rol.get()
            altura = float(entry_altura.get())
            peso = float(entry_peso.get())
            alcance_remate = float(entry_alcance_remate.get())
            alcance_bloqueo = float(entry_alcance_bloqueo.get())
            equipo = combo_equipo.get()

            if equipo not in equipos:
                equipos.append(equipo)

            if crear_jugador(nombre, rol, altura, peso, alcance_remate, alcance_bloqueo, equipo):
                messagebox.showinfo("Éxito", "Jugador registrado exitosamente.")
                ventana.destroy()
            else:
                messagebox.showerror("Error", "El jugador ya está registrado.")

        tk.Label(ventana, text="Nombre:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        entry_nombre = tk.Entry(ventana)
        entry_nombre.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        tk.Label(ventana, text="Rol:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        combo_rol = Combobox(ventana, values=["Central", "Punta/Atacante lateral", "Opuesto", "Colocador", "Libero"])
        combo_rol.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        tk.Label(ventana, text="Altura (m):").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        entry_altura = tk.Entry(ventana)
        entry_altura.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        tk.Label(ventana, text="Peso (kg):").grid(row=3, column=0, sticky="w", padx=10, pady=5)
        entry_peso = tk.Entry(ventana)
        entry_peso.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        tk.Label(ventana, text="Alcance de Remate (m):").grid(row=4, column=0, sticky="w", padx=10, pady=5)
        entry_alcance_remate = tk.Entry(ventana)
        entry_alcance_remate.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

        tk.Label(ventana, text="Alcance de Bloqueo (m):").grid(row=5, column=0, sticky="w", padx=10, pady=5)
        entry_alcance_bloqueo = tk.Entry(ventana)
        entry_alcance_bloqueo.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

        tk.Label(ventana, text="Equipo:").grid(row=6, column=0, sticky="w", padx=10, pady=5)
        combo_equipo = Combobox(ventana, values=equipos)
        combo_equipo.grid(row=6, column=1, padx=10, pady=5, sticky="ew")

        btn_registrar = tk.Button(ventana, text="Registrar Jugador", command=registrar)
        btn_registrar.grid(row=7, column=0, columnspan=2, pady=10)

        ventana.grid_columnconfigure(1, weight=1)

    # Ventana para mostrar detalles y recomendaciones del jugador
    def ventana_detalles_jugador(jugador):
        ventana = tk.Toplevel(root)
        ventana.title(f"Detalles de {jugador['nombre']}")
        ventana.geometry("800x600")

        for i, (campo, valor) in enumerate(jugador.items()):
            tk.Label(ventana, text=f"{campo}: {valor}").grid(row=i, column=0, sticky="w", padx=10)

        recomendaciones = dar_recomendaciones(jugador)
        tk.Label(ventana, text="Recomendaciones:", font=("Arial", 10, "bold")).grid(row=len(jugador), column=0, sticky="w", padx=10)
        for i, rec in enumerate(recomendaciones):
            tk.Label(ventana, text=rec).grid(row=len(jugador) + 1 + i, column=0, sticky="w", padx=10)

    # Ventana para ver todos los jugadores
    def ventana_ver_todos():
        ventana = tk.Toplevel(root)
        ventana.title("Todos los Jugadores")
        ventana.geometry("800x600")

        lista_jugadores = tk.Listbox(ventana)
        lista_jugadores.grid(row=0, column=0, sticky="nsew")

        for jugador in obtener_jugadores():
            datos_jugador = f"{jugador['nombre']} | {jugador['rol']} | {jugador['altura']} m | {jugador['peso']} kg"
            lista_jugadores.insert(tk.END, datos_jugador)

        def mostrar_detalle():
            seleccion = lista_jugadores.curselection()
            if seleccion:
                nombre = lista_jugadores.get(seleccion).split(" | ")[0]
                jugador = obtener_jugador(nombre)
                if jugador:
                    ventana_detalles_jugador(jugador)

        btn_detalle = tk.Button(ventana, text="Ver Detalle", command=mostrar_detalle)
        btn_detalle.grid(row=1, column=0, pady=10)

        ventana.grid_rowconfigure(0, weight=1)
        ventana.grid_columnconfigure(0, weight=1)

    # Función para reproducir videos de jugadas destacadas con pygame y ffpyplayer
    def abrir_video_jugada(posicion):
        videos_jugadas = {
            "Punta": "Z:/CODIGOS/VolleyStats/Videos/Francesco Recine - Italian Volleyball Lightning _ Monster of the Vertical Jump - Epic Volleyball (720p50, h264, youtube).mp4",
            "Libero": "Z:/CODIGOS/VolleyStats/Videos/Jenia Grebennikov_ Master of Defense - Epic Volleyball (720p, h264, youtube).mp4",
            "Opuesto": "Z:/CODIGOS/VolleyStats/Videos/Jesus Herrera Jaime _ Monster of the Vertical Jump - Epic Volleyball (720p, h264, youtube).mp4",
            "Central": "Z:/CODIGOS/VolleyStats/Videos/Top 40 Monster Volleyball Spikes by Flavio Gualberto - Epic Volleyball (720p, h264, youtube).mp4",
            "Colocador": "Z:/CODIGOS/VolleyStats/Videos/Masahiro Sekita _ The Most Creative Setter in Volleyball History !!! - Power Volleyball (720p60, h264, youtube).mp4"
        }
        
        ruta_video = videos_jugadas.get(posicion)
        if not ruta_video:
            messagebox.showerror("Error", "Video no disponible para esta posición.")
            return

        # Inicializar pygame para reproducir el video
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption(f"Video de Jugada - {posicion}")
        player = MediaPlayer(ruta_video)

        # Reproducir el video
        clock = pygame.time.Clock()
        while True:
            frame, val = player.get_frame()
            if val == 'eof':
                break
            if frame:
                img, t = frame
                img = pygame.image.frombuffer(img.to_bytearray()[0], img.get_size(), "RGB")
                screen.blit(img, (0, 0))
                pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    player.close()
                    pygame.quit()
                    return
            clock.tick(30)

    # Función de salida
    def salir():
        root.destroy()

    # Botones principales
    tk.Button(root, text="Registrar Jugador", command=ventana_registrar_jugador).pack(pady=10)
    tk.Button(root, text="Ver Todos los Jugadores", command=ventana_ver_todos).pack(pady=10)
    tk.Button(root, text="Alternar Modo Oscuro/Claro", command=alternar_modo).pack(pady=10)
    
    # Botón para ver videos de jugadas destacadas
    tk.Label(root, text="Seleccione la posición para ver jugada:").pack(pady=5)
    combo_posiciones = Combobox(root, values=["Punta", "Libero", "Opuesto", "Central", "Colocador"])
    combo_posiciones.pack(pady=5)
    Button(root, text="Ver Jugada", command=lambda: abrir_video_jugada(combo_posiciones.get())).pack(pady=10)

    tk.Button(root, text="Salir", command=salir).pack(pady=10)

    root.mainloop()