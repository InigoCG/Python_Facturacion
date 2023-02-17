import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter.messagebox import *
from tkinter import Tk, Button

def actualizarNombre(event):
    nombres = nombre.get()

def actualizarEmpresa(event):
    empresas = empresa.get()

def actualizarCiudad(event):
    ciudades = ciudad.get()

def guardar():
    connection = sqlite3.connect('base.db')
    cursor = connection.cursor()

    id = codProveedor.get()
    nombres = nombre.get()
    empresas = empresa.get()
    ciudades = ciudad.get()

    try:
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS proveedores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nombre VARCHAR(40) NOT NULL, 
                    empresa VARCHAR(40) NOT NULL, 
                    ciudad VARCHAR(30) NOT NULL)
                    ''')
        print("Tabla creada correctamente")
    except sqlite3.OperationalError as error:
        print("Error al abrir: ", error)

    registro = "INSERT INTO proveedores (nombre, empresa, ciudad) VALUES(?, ?, ?)"
    cursor.execute(registro, [nombres, empresas, ciudades])
    connection.commit()
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
        codProveedor.delete(0, 'end')
        nombre.delete(0, 'end')
        empresa.delete(0, 'end')
        ciudad.delete(0, 'end')
    elif dato == False:
        marco.destroy()

def altaProveedores():
    global marco
    marco = tk.Tk()
    marco.title("Añadir Proveedores")
    marco.state('zoomed')
    marco.config(bg="blue")
    marco.grid_propagate(0)
    marco.iconbitmap("icono.ico")

    etiqueta0 = tk.Label(marco, text="                     AÑADIR PROVEEDOR                       ", bg="green", font =("Bahnschrift",12)).grid(row=0, column=1, sticky="w", padx=10, pady=10)

    espacio1 = tk.Label(marco, text="", bg="blue").grid(row=1, column=0, sticky="w",padx=10, pady=10)
    espacio2 = tk.Label(marco, text="", bg="blue").grid(row=2, column=0, sticky="w", padx=10, pady=10)
    espacio3 = tk.Label(marco, text="", bg="blue").grid(row=3, column=0, sticky="w", padx=10, pady=10)
    espacio4 = tk.Label(marco, text="", bg="blue").grid(row=4, column=0, sticky="w", padx=10, pady=10)

    etiqueta1 = tk.Label(marco, text="Código del proveedor", bg="green", font=("Bahnschrift",12)).grid(row=5, column=0, sticky="w", padx=10, pady=10)
    global codProveedor
    codProveedor = ttk.Entry(marco)
    codProveedor.grid(row=5, column=1, sticky="w", padx=10, pady=10)
    codProveedor['state'] = 'disabled'

    etiqueta2 = tk.Label(marco, text="Nombre", bg="green", font=("Bahnschrift",12)).grid(row=6, column=0, sticky="w", padx=10, pady=10)
    global nombre
    nombre = tk.Entry(marco, width=100)
    nombre.grid(row=6, column=1, sticky="w", padx=10, pady=10)
    nombre.bind('<Leave>', actualizarNombre)

    etiqueta2 = tk.Label(marco, text="Empresa", bg="green", font=("Bahnschrift",12)).grid(row=7, column=0, sticky="w", padx=10, pady=10)
    global empresa
    empresa = tk.Entry(marco, width=100)
    empresa.grid(row=7, column=1, sticky="w", padx=10, pady=10)
    empresa.bind('<Leave>', actualizarEmpresa)

    etiqueta2 = tk.Label(marco, text="Ciudad", bg="green", font=("Bahnschrift", 12)).grid(row=8, column=0, sticky="w",padx=10, pady=10)
    global ciudad
    ciudad = tk.Entry(marco, width=100)
    ciudad.grid(row=8, column=1, sticky="w", padx=10, pady=10)
    ciudad.bind('<Leave>', actualizarCiudad)

    global tabla
    tabla = ttk.Treeview(marco,
                         columns=("id", "nombre", "empresa", "ciudad"))
    tabla["show"] = "headings"
    tabla.column("#0")
    tabla.column("id", width=150, anchor=tk.CENTER)
    tabla.column("nombre", width=150, anchor=tk.CENTER)
    tabla.column("empresa", width=150, anchor=tk.CENTER)
    tabla.column("ciudad", width=150, anchor=tk.CENTER)

    tabla.heading("id", text="id", anchor=tk.CENTER)
    tabla.heading("nombre", text="nombre", anchor=tk.CENTER)
    tabla.heading("empresa", text="empresa", anchor=tk.CENTER)
    tabla.heading("ciudad", text="precio", anchor=tk.CENTER)

    conexion = sqlite3.connect('base.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM proveedores")

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