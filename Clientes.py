import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter.messagebox import *
from tkinter import Tk, Button

def actualizarNombre(event):
    name = nombre.get()

def actualizarApellido(event):
    lastname = apellido.get()

def actualizarCiudad(event):
    town = ciudad.get()

def guardar():
    connection = sqlite3.connect('base.db')
    cursor = connection.cursor()

    id = codCliente.get()
    nombres = nombre.get()
    lastname = apellido.get()
    town = ciudad.get()

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre VARCHAR(40) NOT NULL, 
            apellido VARCHAR(40) NOT NULL, 
            ciudad VARCHAR(30) NOT NULL)
            ''')
        print("Tabla creada correctamente")
    except sqlite3.OperationalError as error:
        print("Erorr al abrir: ", error)

    registro = "INSERT INTO clientes (nombre, apellido, ciudad) VALUES(?,?,?)"
    cursor.execute(registro, [nombres, lastname, town])
    connection.commit()

    tabla.delete(*tabla.get_children())

    cursor.execute("SELECT * FROM clientes")

    i = 0
    for a in cursor:
        tabla.insert("", i, text="", values=(a[0], a[1], a[2], a[3]))
        i += 1
    tabla.place(x=450, y=450)

    mostrar()
    continuar()

def mostrar():
    try:
        botonGuardar['state'] = 'disabled'
        conexion = sqlite3.connect("base.db")
        cursor = conexion.cursor()
        registro = "SELECT * FROM clientes;"
        cursor.execute(registro)
        cliente = cursor.fetchall()
        print(cliente)

    except sqlite3.OperationalError as error:
        print("Error al abrir: ", error)

def continuar():
    dato = tk.messagebox.askyesno(message="¿Desea continuar?", title="Título", parent=marco)
    if dato == True:
        botonGuardar['state'] = 'normal'
        codCliente.delete(0, 'end')
        nombre.delete(0, 'end')
        apellido.delete(0, 'end')
        ciudad.delete(0, 'end')
    elif dato == False:
        marco.destroy()


def altaClientes():
    global marco
    marco = tk.Tk()
    marco.title("Añadir Clientes")
    marco.state('zoomed')
    marco.config(bg="pink")
    marco.grid_propagate(0)
    marco.iconbitmap("icono.ico")

    etiqueta0 = tk.Label(marco,text="                     AÑADIR CLIENTE                       ", bg="purple", font =("Bahnschrift",12)).grid(row=0, column=1, sticky="w", padx=10, pady=10)

    espacio1 = tk.Label(marco, text="", bg="pink").grid(row=1, column=0, sticky="w", padx=10, pady=10)
    espacio2 = tk.Label(marco, text="", bg="pink").grid(row=2, column=0, sticky="w", padx=10, pady=10)
    espacio3 = tk.Label(marco, text="", bg="pink").grid(row=3, column=0, sticky="w", padx=10, pady=10)
    espacio4 = tk.Label(marco, text="", bg="pink").grid(row=4, column=0, sticky="w", padx=10, pady=10)
    etiqueta1 = tk.Label(marco, text="Código del cliente", bg="purple", font=("Bahnschrift",12)).grid(row=5, column=0, sticky="w", padx=10, pady=10)

    global codCliente
    codCliente = ttk.Entry(marco)
    codCliente.grid(row=5, column=1, sticky="w", padx=10, pady=10)
    codCliente['state'] = 'disabled'

    etiqueta2 = tk.Label(marco, text="nombre", bg="purple", font=("Bahnschrift",12)).grid(row=6, column=0, sticky="w", padx=10, pady=10)
    global nombre
    nombre = tk.Entry(marco, width=100)
    nombre.grid(row=6, column=1, sticky="w", padx=10, pady=10)
    nombre.bind('<Leave>', actualizarNombre)

    etiqueta3 = tk.Label(marco, text="apellido", bg="purple", font=("Bahnschrift",12)).grid(row=7, column=0, sticky="w", padx=10, pady=10)
    global apellido
    apellido = tk.Entry(marco, width=100)
    apellido.grid(row=7, column=1, sticky="w", padx=10, pady=10)
    apellido.bind('<Leave>', actualizarApellido)

    etiqueta4 = tk.Label(marco, text="ciudad", bg="purple", font=("Bahnschrift",12)).grid(row=8, column=0, sticky="w", padx=10, pady=10)
    global ciudad
    ciudad = tk.Entry(marco, width=100)
    ciudad.grid(row=8, column=1, sticky="w", padx=10, pady=10)
    ciudad.bind('<Leave>', actualizarCiudad)

    global tabla
    tabla = ttk.Treeview(marco,
                         columns=("id", "nombre", "apellido", "ciudad"))
    tabla["show"] = "headings"
    tabla.column("#0")
    tabla.column("id", width=150, anchor=tk.CENTER)
    tabla.column("nombre", width=150, anchor=tk.CENTER)
    tabla.column("apellido", width=150, anchor=tk.CENTER)
    tabla.column("ciudad", width=150, anchor=tk.CENTER)

    tabla.heading("id", text="id", anchor=tk.CENTER)
    tabla.heading("nombre", text="nombre", anchor=tk.CENTER)
    tabla.heading("apellido", text="apellido", anchor=tk.CENTER)
    tabla.heading("ciudad", text="ciudad", anchor=tk.CENTER)

    conexion = sqlite3.connect('base.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM clientes")

    i = 0
    for a in cursor:
        tabla.insert("", i, text="", values=(a[0], a[1], a[2], a[3]))
        i += 1
    tabla.place(x=450, y=450)

    global botonGuardar
    botonGuardar = Button(marco)
    botonGuardar.config(text="GUARDAR", width=10, height=2, anchor="center", activebackground="blue", relief="raised",
                        borderwidth=5, font=("Banschrift", 11), command=lambda: guardar())
    botonGuardar.grid(row=13, column=1, sticky="w", padx=100, pady=100)