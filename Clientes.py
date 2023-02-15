import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter.messagebox import *
from tkinter import Tk, Button

def actualizarNombre(event):
    name = nombre.get()

def guardar():
    connection = sqlite3.connect('base.db')
    cursor = connection.cursor()

    id = codCliente.get()
    name = nombre.get()




def altaClientes():
    global marco
    marco = tk.Tk()
    marco.title("Añadir Clientes")
    marco.state('zoomed')
    marco.config(bg="pink")
    marco.grid_propagate(0)
    marco.iconbitmap("icono.ico")

    etiqueta0 = tk.Label(marco,text="                     AÑADIR PRODUCTO                       ", bg="purple", font =("Bahnschrift",12)).grid(row=0, column=1, sticky="w", padx=10, pady=10)

    espacio1 = tk.Label(marco, text="", bg="red").grid(row=1, column=0, sticky="w", padx=10, pady=10)
    espacio2 = tk.Label(marco, text="", bg="red").grid(row=2, column=0, sticky="w", padx=10, pady=10)
    espacio3 = tk.Label(marco, text="", bg="red").grid(row=3, column=0, sticky="w", padx=10, pady=10)
    espacio4 = tk.Label(marco, text="", bg="red").grid(row=4, column=0, sticky="w", padx=10, pady=10)
    etiqueta1 = tk.Label(marco, text="Código del cliente", bg="purple", font=("Bahnschrift",12)).grid(row=5, column=0, sticky="w", padx=10, pady=10)

    global codCliente
    codCliente = ttk.Entry(marco)
    codCliente.grid(row=5, column=1, sticky="w", padx=10, pady=10)
    codCliente['state'] = 'disabled'

    etiqueta2 = tk.Label(marco, text="nombre", bg="purple", font=("Banschrift",12)).grid(row=6, column=0, sticky="w", padx=10, pady=10)
    global nombre
    nombre = tk.Entry(marco, width=100)
    nombre.grid(row=6, column=1, sticky="w", padx=10, pady=10)
    nombre.bind('<Leave>', actualizarNombre)




    global botonGuardar
    botonGuardar = Button(marco)
    botonGuardar.config(text="GUARDAR", width=10, height=2, anchor="center", activebackground="blue", relief="raised",
                        borderwidth=5, font=("Banschrift", 11), command=lambda: guardar())
    botonGuardar.grid(row=13, column=1, sticky="w", padx=100, pady=100)