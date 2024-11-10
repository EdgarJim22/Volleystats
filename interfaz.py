"""================================================================================================
Date: 9/11/2024
Owner......: Edgar Enrique Jimenez Hernández
Title......: `interfaz.py`
Function...: Proporciona una interfaz gráfica para el registro y consulta de jugadores.
Python.....: 3.8+
================================================================================================"""

import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
from atletas import crear_jugador, obtener_jugadores
from estadisticas import analizar_rendimiento

# Lista de equipos registrada
equipos = ["Equipo A", "Equipo B", "Equipo C"]

def ventana_principal():
    root = tk.Tk()
    root.title("Sistema de Registro de Jugadores")

    # Función para registrar un nuevo jugador
    def registrar_jugador():
        nombre = entry_nombre.get()
        rol = combo_rol.get()
        altura = float(entry_altura.get())
        peso = float(entry_peso.get())
        alcance_remate = float(entry_alcance_remate.get())
        alcance_bloqueo = float(entry_alcance_bloqueo.get())

        # Asignación de equipo
        equipo = combo_equipo.get()
        if equipo not in equipos:
            equipos.append(equipo)

        # Intentamos crear el jugador
        exito = crear_jugador(nombre, rol, altura, peso, alcance_remate, alcance_bloqueo, equipo)

        if exito:
            messagebox.showinfo("Éxito", "Jugador registrado exitosamente.")
        else:
            messagebox.showerror("Error", "El jugador ya está registrado en este equipo.")

    # Función para consultar jugadores por equipo
    def consultar_jugadores():
        equipo = combo_equipo.get()
        jugadores = obtener_jugadores(equipo)
        lista_jugadores.delete(0, tk.END)
        for jugador in jugadores:
            lista_jugadores.insert(tk.END, jugador["nombre"])

    # Función para ver recomendaciones
    def ver_recomendaciones():
        seleccionado = lista_jugadores.curselection()
        if seleccionado:
            nombre_jugador = lista_jugadores.get(seleccionado[0])
            recomendaciones = analizar_rendimiento(nombre_jugador)
            texto_recomendaciones.delete(1.0, tk.END)
            for recomendacion in recomendaciones:
                texto_recomendaciones.insert(tk.END, recomendacion + "\n")

    # Función para ver todos los jugadores
    def ver_todos_los_jugadores():
        lista_jugadores.delete(0, tk.END)
        jugadores = obtener_jugadores()
        for jugador in jugadores:
            lista_jugadores.insert(tk.END, jugador["nombre"])

    # Crear elementos de la interfaz
    tk.Label(root, text="Nombre:").grid(row=0, column=0)
    entry_nombre = tk.Entry(root)
    entry_nombre.grid(row=0, column=1)

    tk.Label(root, text="Rol:").grid(row=1, column=0)
    combo_rol = Combobox(root, values=["Central", "Punta/Atacante lateral", "Opuesto", "Colocador", "Libero"])
    combo_rol.grid(row=1, column=1)

    tk.Label(root, text="Altura (m):").grid(row=2, column=0)
    entry_altura = tk.Entry(root)
    entry_altura.grid(row=2, column=1)

    tk.Label(root, text="Peso (kg):").grid(row=3, column=0)
    entry_peso = tk.Entry(root)
    entry_peso.grid(row=3, column=1)

    tk.Label(root, text="Alcance de Remate (m):").grid(row=4, column=0)
    entry_alcance_remate = tk.Entry(root)
    entry_alcance_remate.grid(row=4, column=1)

    tk.Label(root, text="Alcance de Bloqueo (m):").grid(row=5, column=0)
    entry_alcance_bloqueo = tk.Entry(root)
    entry_alcance_bloqueo.grid(row=5, column=1)

    tk.Label(root, text="Equipo:").grid(row=6, column=0)
    combo_equipo = Combobox(root, values=equipos)
    combo_equipo.grid(row=6, column=1)

    btn_registrar = tk.Button(root, text="Registrar Jugador", command=registrar_jugador)
    btn_registrar.grid(row=7, column=0, columnspan=2)

    label_equipo = tk.Label(root, text="Ver Jugadores por Equipo:")
    label_equipo.grid(row=8, column=0)
    combo_equipo = Combobox(root, values=equipos)
    combo_equipo.grid(row=8, column=1)
    btn_consultar = tk.Button(root, text="Consultar", command=consultar_jugadores)
    btn_consultar.grid(row=9, column=0, columnspan=2)

    btn_ver_todos = tk.Button(root, text="Ver Todos los Jugadores", command=ver_todos_los_jugadores)
    btn_ver_todos.grid(row=10, column=0, columnspan=2)

    # Lista de jugadores
    lista_jugadores = tk.Listbox(root, height=10, width=50)
    lista_jugadores.grid(row=11, column=0, columnspan=2)

    # Sección de recomendaciones
    label_recomendaciones = tk.Label(root, text="Recomendaciones:")
    label_recomendaciones.grid(row=12, column=0)
    texto_recomendaciones = tk.Text(root, height=10, width=50)
    texto_recomendaciones.grid(row=13, column=0, columnspan=2)

    btn_ver_recomendaciones = tk.Button(root, text="Ver Recomendaciones", command=ver_recomendaciones)
    btn_ver_recomendaciones.grid(row=14, column=0, columnspan=2)

    root.mainloop()