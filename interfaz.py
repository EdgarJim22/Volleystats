"""================================================================================================
Date: 9/11/2024
Owner......: Edgar Enrique Jimenez Hernández
Title......: `interfaz.py`
Function...: Proporciona la interfaz gráfica principal con subventanas para cada opción.
Python.....: 3.8+
================================================================================================"""

import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
from atletas import crear_jugador, obtener_jugadores
from estadisticas import analizar_rendimiento

equipos = ["Equipo A", "Equipo B", "Equipo C"]

# Función principal de la ventana
def ventana_principal():
    root = tk.Tk()
    root.title("Sistema de Registro de Jugadores")

    # Ventana para registrar un nuevo jugador
    def ventana_registrar_jugador():
        ventana = tk.Toplevel(root)
        ventana.title("Registrar Jugador")

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

        tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
        entry_nombre = tk.Entry(ventana)
        entry_nombre.grid(row=0, column=1)

        tk.Label(ventana, text="Rol:").grid(row=1, column=0)
        combo_rol = Combobox(ventana, values=["Central", "Punta/Atacante lateral", "Opuesto", "Colocador", "Libero"])
        combo_rol.grid(row=1, column=1)

        tk.Label(ventana, text="Altura (m):").grid(row=2, column=0)
        entry_altura = tk.Entry(ventana)
        entry_altura.grid(row=2, column=1)

        tk.Label(ventana, text="Peso (kg):").grid(row=3, column=0)
        entry_peso = tk.Entry(ventana)
        entry_peso.grid(row=3, column=1)

        tk.Label(ventana, text="Alcance de Remate (m):").grid(row=4, column=0)
        entry_alcance_remate = tk.Entry(ventana)
        entry_alcance_remate.grid(row=4, column=1)

        tk.Label(ventana, text="Alcance de Bloqueo (m):").grid(row=5, column=0)
        entry_alcance_bloqueo = tk.Entry(ventana)
        entry_alcance_bloqueo.grid(row=5, column=1)

        tk.Label(ventana, text="Equipo:").grid(row=6, column=0)
        combo_equipo = Combobox(ventana, values=equipos)
        combo_equipo.grid(row=6, column=1)

        btn_registrar = tk.Button(ventana, text="Registrar Jugador", command=registrar)
        btn_registrar.grid(row=7, column=0, columnspan=2)

    # Ventana para consultar jugadores por equipo
    def ventana_consultar_por_equipo():
        ventana = tk.Toplevel(root)
        ventana.title("Consultar Jugadores por Equipo")

        def mostrar_jugadores():
            equipo = combo_equipo.get()
            jugadores = obtener_jugadores(equipo)
            lista_jugadores.delete(0, tk.END)
            for jugador in jugadores:
                lista_jugadores.insert(tk.END, jugador["nombre"])

        tk.Label(ventana, text="Seleccione Equipo:").grid(row=0, column=0)
        combo_equipo = Combobox(ventana, values=equipos)
        combo_equipo.grid(row=0, column=1)
        btn_mostrar = tk.Button(ventana, text="Mostrar", command=mostrar_jugadores)
        btn_mostrar.grid(row=0, column=2)

        lista_jugadores = tk.Listbox(ventana, width=50)
        lista_jugadores.grid(row=1, column=0, columnspan=3)

    # Ventana para ver todos los jugadores
    def ventana_ver_todos():
        ventana = tk.Toplevel(root)
        ventana.title("Todos los Jugadores")

        lista_jugadores = tk.Listbox(ventana, width=50)
        lista_jugadores.grid(row=0, column=0)

        for jugador in obtener_jugadores():
            lista_jugadores.insert(tk.END, jugador["nombre"])

    # Botones principales
    btn_registrar_jugador = tk.Button(root, text="Registrar Jugador", command=ventana_registrar_jugador)
    btn_registrar_jugador.pack(pady=5)

    btn_consultar_por_equipo = tk.Button(root, text="Consultar Jugadores por Equipo", command=ventana_consultar_por_equipo)
    btn_consultar_por_equipo.pack(pady=5)

    btn_ver_todos = tk.Button(root, text="Ver Todos los Jugadores", command=ventana_ver_todos)
    btn_ver_todos.pack(pady=5)

    btn_salir = tk.Button(root, text="Salir", command=root.quit)
    btn_salir.pack(pady=5)

    root.mainloop()

# Ejecutar la interfaz
ventana_principal()