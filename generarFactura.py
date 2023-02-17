import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter.messagebox import *
from tkinter import Tk, Button

def actualizarFechaExpedicion(event):
    fechaExpedicion = fechaExp.get()

def actualizarClientes(event):
    cliente = clientes.current()

def actualizarProveedores(event):
    proveedor = proveedores.current()

def actualizarProductos(event):
    producto = productos.current()

def guardar():
    connection = sqlite3.connect('base.db')
    cursor = connection.cursor()

    id = codFactura.get()
    fecha = fechaExp.get()
    cliente = clientes.current()
    proveedor = proveedores.current()
    producto = productos.current()

    try:
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS generar_facturas (
                       id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       fecha_expedicion VARCHAR(40) NOT NULL, 
                       cliente VARCHAR(60) NOT NULL, 
                       proveedor VARCHAR(60) NOT NULL, 
                       producto VARCHAR(60) NOT NULL)
                       ''')
        print("Tabla creada correctamente")
    except sqlite3.OperationalError as error:
        print("Error al abrir: ", error)

    registro = "INSERT INTO generar_factura (fechaExp, clientes, proveedores, productos) VALUES(?, ?, ?, ?)"
    cursor.execute(registro, [fecha, cliente, proveedor, producto])
    connection.commit()
    mostrar()
    continuar()


def mostrar():
    try:
        botonGuardar['state'] = 'disabled'
        conexion = sqlite3.connect("base.db")
        cursor = conexion.cursor()
        registro = "SELECT * FROM generar_factura;"
        cursor.execute(registro)
        factura = cursor.fetchall()
        print(factura)

    except sqlite3.OperationalError as error:
        print("Error al abrir:", error)


def continuar():
    dato = tk.messagebox.askyesno(message="¿Desea continuar?", title="Título", parent=marco)
    if dato == True:
        botonGuardar['state'] = 'normal'
        codFactura.delete(0, 'end')
        fechaExp.delete(0, 'end')
        clientes.delete(0, 'end')
        proveedores.delete(0, 'end')
        productos.delete(0, 'end')
    elif dato == False:
        marco.destroy()


def creacionFacturas():
    global marco
    marco = tk.Tk()
    marco.title("Generar Facturas")
    marco.state('zoomed')
    marco.config(bg="yellow")
    marco.grid_propagate(0)
    marco.iconbitmap("icono.ico")

    etiqueta0 = tk.Label(marco, text="                     GENERAR FACTURAS                       ", bg="blue", font =("Bahnschrift",12)).grid(row=0, column=1, sticky="w", padx=10, pady=10)

    espacio1 = tk.Label(marco, text="", bg="yellow").grid(row=1, column=0, sticky="w",padx=10, pady=10)
    espacio2 = tk.Label(marco, text="", bg="yellow").grid(row=2, column=0, sticky="w", padx=10, pady=10)
    espacio3 = tk.Label(marco, text="", bg="yellow").grid(row=3, column=0, sticky="w", padx=10, pady=10)
    espacio4 = tk.Label(marco, text="", bg="yellow").grid(row=4, column=0, sticky="w", padx=10, pady=10)

    etiqueta1 = tk.Label(marco, text="Código de la factura", bg="blue", font=("Bahnschrift",12)).grid(row=5, column=0, sticky="w", padx=10, pady=10)
    global codFactura
    codFactura = ttk.Entry(marco)
    codFactura.grid(row=5, column=1, sticky="w", padx=10, pady=10)
    codFactura['state'] = 'disabled'

    etiqueta2 = tk.Label(marco, text="Fecha expedición", bg="blue", font=("Bahnschrift",12)).grid(row=6, column=0, sticky="w", padx=10, pady=10)
    global fechaExp
    fechaExp = tk.Entry(marco, width=100)
    fechaExp.grid(row=6, column=1, sticky="w", padx=10, pady=10)
    fechaExp.bind('<Leave>', actualizarFechaExpedicion)

    etiqueta3 = tk.Label(marco, text="Clientes", bg="blue", font=("Bahnschrift",12)).grid(row=7, column=0, sticky="w", padx=10, pady=10)
    global clientes
    clientes = ttk.Combobox(marco)
    clientes['values'] = ("SELECT nombre FROM clientes")
    clientes.grid(row=10, column=1, sticky="w", padx=10, pady=10)
    clientes.bind('<<ComboboxSelected>>', actualizarClientes)

    etiqueta4 = tk.Label(marco, text="Proveedores", bg="green", font=("Bahnschrift", 12)).grid(row=8, column=0, sticky="w",padx=10, pady=10)
    global proveedores
    proveedores = ttk.Combobox(marco)
    proveedores['values'] = ("SELECT nombre FROM proveedores")
    proveedores.grid(row=10, column=1, sticky="w", padx=10, pady=10)
    proveedores.bind('<<ComboboxSelected>>', actualizarProveedores)

    etiqueta4 = tk.Label(marco, text="Productos", bg="green", font=("Bahnschrift", 12)).grid(row=8, column=0,sticky="w", padx=10,pady=10)
    global productos
    productos = ttk.Combobox(marco)
    productos['values'] = ("SELECT nombre, precio FROM productos")
    productos.grid(row=10, column=1, sticky="w", padx=10, pady=10)
    productos.bind('<<ComboboxSelected>>', actualizarProveedores)

    global tabla
    tabla = ttk.Treeview(marco,
                         columns=("id", "fecha_expedicion", "cliente", "proveedor","producto"))
    tabla["show"] = "headings"
    tabla.column("#0")
    tabla.column("id", width=150, anchor=tk.CENTER)
    tabla.column("fecha_expedicion", width=150, anchor=tk.CENTER)
    tabla.column("cliente", width=150, anchor=tk.CENTER)
    tabla.column("proveedor", width=150, anchor=tk.CENTER)
    tabla.column("producto", width=150, anchor=tk.CENTER)

    tabla.heading("id", text="id", anchor=tk.CENTER)
    tabla.heading("fecha_expedicion", text="fecha_expedicion", anchor=tk.CENTER)
    tabla.heading("cliente", text="cliente", anchor=tk.CENTER)
    tabla.heading("cliente", text="cliente", anchor=tk.CENTER)
    tabla.heading("producto", text="producto", anchor=tk.CENTER)

    conexion = sqlite3.connect('base.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM generar_facturas")

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