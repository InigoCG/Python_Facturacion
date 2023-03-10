import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter.messagebox import *
from tkinter import Tk, Button

import tabla as tabla


def actualizarcombo(event):
    index = combobo.current()

def actualizarNombre(event):
    nombres = nombre.get()

def actualizarEmpresa(event):
    empresas = empresa.get()

"""def actualizarPrecio(event):
    precios = precio.get()"""

def actualizarCantidad(event):
    cantidades = cantidad.get()

def guardar():
    connection = sqlite3.connect('base.db')
    cursor = connection.cursor()

    id = codProducto.get()
    nombres = nombre.get()
    empresas = empresa.get()
    #precios = precio.get()
    cantidades = cantidad.get()
    index = combobo.current()
    if index == 0:
        consumible = "Perecedero"
    elif index == 1:
        consumible = "No perecedero"

    try:
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS productos (
                       id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       nombre VARCHAR(40) NOT NULL, 
                       empresa VARCHAR(40) NOT NULL, 
                       cantidad INTEGER NOT NULL, 
                       consumible VARCHAR(12) NOT NULL)
                       ''')
        print("Tabla creada correctamente")
    except sqlite3.OperationalError as error:
        print("Error al abrir: ", error)

    registro = "INSERT INTO productos (nombre, empresa, cantidad, consumible) VALUES(?, ?, ?, ?)"
    cursor.execute(registro, [nombres, empresas, cantidades, consumible])
    connection.commit()

    tabla.delete(*tabla.get_children())

    cursor.execute("SELECT * FROM productos")

    i = 0
    for a in cursor:
        tabla.insert("", i, text="", values=(a[0], a[1], a[2], a[3], a[4]))
        i += 1
    tabla.place(x=450, y=450)

    mostrar()
    continuar()


def mostrar():
    try:
        botonGuardar['state'] = 'disabled'
        conexion = sqlite3.connect("base.db")
        cursor = conexion.cursor()
        registro = "SELECT * FROM productos;"
        cursor.execute(registro)
        producto = cursor.fetchall()
        print(producto)

    except sqlite3.OperationalError as error:
        print("Error al abrir:", error)


def continuar():
    dato = tk.messagebox.askyesno(message="??Desea continuar?", title="T??tulo", parent=marco)
    if dato == True:
        botonGuardar['state'] = 'normal'
        codProducto.delete(0, 'end')
        nombre.delete(0, 'end')
        empresa.delete(0, 'end')
        #precio.delete(0, 'end')
        cantidad.delete(0, 'end')
        combobo.delete(0, 'end')
    elif dato == False:
        marco.destroy()

def altaProductos():
    global marco
    marco = tk.Tk()
    marco.title("A??adir Productos")
    marco.state('zoomed')
    marco.config(bg="brown")
    marco.grid_propagate(0)
    marco.iconbitmap("icono.ico")

    etiqueta0 = tk.Label(marco, text="                     A??ADIR PRODUCTO                       ", bg="yellow", font =("Bahnschrift",12)).grid(row=0, column=1, sticky="w", padx=10, pady=10)

    espacio1 = tk.Label(marco, text="", bg="brown").grid(row=1, column=0, sticky="w",padx=10, pady=10)
    espacio2 = tk.Label(marco, text="", bg="brown").grid(row=2, column=0, sticky="w", padx=10, pady=10)
    espacio3 = tk.Label(marco, text="", bg="brown").grid(row=3, column=0, sticky="w", padx=10, pady=10)
    espacio4 = tk.Label(marco, text="", bg="brown").grid(row=4, column=0, sticky="w", padx=10, pady=10)

    etiqueta1 = tk.Label(marco, text="C??digo del producto", bg="yellow", font=("Bahnschrift",12)).grid(row=5, column=0, sticky="w", padx=10, pady=10)
    global codProducto
    codProducto = ttk.Entry(marco)
    codProducto.grid(row=5, column=1, sticky="w", padx=10, pady=10)
    codProducto['state'] = 'disabled'

    etiqueta2 = tk.Label(marco, text="Nombre", bg="yellow", font=("Bahnschrift",12)).grid(row=6, column=0, sticky="w", padx=10, pady=10)
    global nombre
    nombre = tk.Entry(marco, width=100)
    nombre.grid(row=6, column=1, sticky="w", padx=10, pady=10)
    nombre.bind('<Leave>', actualizarNombre)

    etiqueta2 = tk.Label(marco, text="Empresa", bg="yellow", font=("Bahnschrift",12)).grid(row=7, column=0, sticky="w", padx=10, pady=10)
    global empresa
    empresa = tk.Entry(marco, width=100)
    empresa.grid(row=7, column=1, sticky="w", padx=10, pady=10)
    empresa.bind('<Leave>', actualizarEmpresa)

    """etiqueta2 = tk.Label(marco, text="precio", bg="yellow", font=("Bahnschrift", 12)).grid(row=8, column=0, sticky="w",padx=10, pady=10)
    global precio
    precio = tk.Entry(marco, width=100)
    precio.grid(row=8, column=1, sticky="w", padx=10, pady=10)
    precio.bind('<Leave>', actualizarPrecio)"""

    etiqueta2 = tk.Label(marco, text="cantidad", bg="yellow", font=("Bahnschrift", 12)).grid(row=8, column=0, sticky="w",padx=10, pady=10)
    global cantidad
    cantidad = tk.Entry(marco, width=100)
    cantidad.grid(row=8, column=1, sticky="w", padx=10, pady=10)
    cantidad.bind('<Leave>', actualizarCantidad)

    etiqueta4 = tk.Label(marco, text="Durabilidad", bg="yellow", font=("Bahnschrift", 12)).grid(row=9, column=0,sticky="w", padx=10,pady=10)
    global combobo
    combobo = ttk.Combobox(marco)
    combobo['values'] = ("Perecedro", "No Perecedero")
    combobo.grid(row=9, column=1, sticky="w", padx=10, pady=10)
    combobo.bind('<<ComboboxSelected>>', actualizarcombo)

    global tabla
    tabla = ttk.Treeview(marco,
                         columns=("id", "nombre", "empresa", "cantidad", "consumible"))
    tabla["show"] = "headings"
    tabla.column("#0")
    tabla.column("id", width=150, anchor=tk.CENTER)
    tabla.column("nombre", width=150, anchor=tk.CENTER)
    tabla.column("empresa", width=150, anchor=tk.CENTER)
    tabla.column("cantidad", width=150, anchor=tk.CENTER)
    tabla.column("consumible", width=150, anchor=tk.CENTER)

    tabla.heading("id", text="id", anchor=tk.CENTER)
    tabla.heading("nombre", text="nombre", anchor=tk.CENTER)
    tabla.heading("empresa", text="empresa", anchor=tk.CENTER)
    tabla.heading("cantidad", text="cantidad", anchor=tk.CENTER)
    tabla.heading("consumible", text="consumible", anchor=tk.CENTER)

    conexion = sqlite3.connect('base.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")

    i = 0
    for a in cursor:
        tabla.insert("", i, text="", values=(a[0], a[1], a[2], a[3], a[4]))
        i += 1
    tabla.place(x=450, y= 450)

    global botonGuardar
    botonGuardar = Button(marco)
    botonGuardar.config(text="GUARDAR", width=10, height=2, anchor="center", activebackground="blue", relief="raised",
                        borderwidth=5, font=("Banschrift", 11), command=guardar)
    botonGuardar.grid(row=13, column=1, sticky="w", padx=100, pady=100)