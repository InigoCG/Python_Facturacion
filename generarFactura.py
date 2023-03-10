import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter.messagebox import *
from tkinter import Tk, Button
from Facturas import imprimirFactura

def actualizarClientes(event):
    cliente = clientes.current()

def actualizarProveedores(event):
    proveedor = proveedores.current()

def actualizarProductos(event):
    producto = Nombreproductos.current()

def actualizarPrecioProductos(event):
    precioProducto = Precioproductos.current()

def guardar():
    connection = sqlite3.connect('base.db')
    cursor = connection.cursor()

    id = codFactura.get()
    cliente = clientes.get()
    proveedor = proveedores.get()
    producto = Nombreproductos.get()
    precio = Precioproductos.get()

    try:
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS generar_facturas (
                       id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       cliente VARCHAR(60) NOT NULL, 
                       proveedor VARCHAR(60) NOT NULL, 
                       nombre_producto VARCHAR(60) NOT NULL,
                       precio_producto VARCHAR(60) NOT NULL)
                       ''')
        print("Tabla creada correctamente")
    except sqlite3.OperationalError as error:
        print("Error al abrir: ", error)

    registro = "INSERT INTO generar_facturas (cliente, proveedor, nombre_producto, precio_producto) VALUES(?, ?, ?, ?)"
    cursor.execute(registro, [cliente, proveedor, producto, precio])
    connection.commit()

    tabla.delete(*tabla.get_children())

    cursor.execute("SELECT * FROM generar_facturas")

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
        clientes.delete(0, 'end')
        proveedores.delete(0, 'end')
        Nombreproductos.delete(0, 'end')
        Precioproductos.delete(0, 'end')
    elif dato == False:
        marco.destroy()

global codigoSeleccionado
codigoSeleccionado = None
global datosFactura

def onSelected(evnt):
    for a in tabla.selection():
        item = tabla.item(a)
        cod, cli, prov, prod, prec = item["values"][0:5]
        global codigoSeleccionado
        codigoSeleccionado = cod
        global datosFactura
        datosFactura = []
        datosFactura.append(cli)
        datosFactura.append(prov)
        datosFactura.append(prod)
        datosFactura.append(prec)
        print(len(datosFactura))

def accionboton():
    if (codigoSeleccionado == None):
        tk.messagebox.showerror(message="Debes seleccionar una factura en la tabla", title="Error", parent=marco)
    else:
        tk.messagebox.showinfo(message=f'Factura nº{codigoSeleccionado} impresa', title="Info", parent=marco)
        imprimirFactura(codigoSeleccionado, datosFactura)

def creacionFacturas():
    connection = sqlite3.connect('base.db')
    cursor = connection.cursor()

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

    etiqueta3 = tk.Label(marco, text="Clientes", bg="blue", font=("Bahnschrift",12)).grid(row=7, column=0, sticky="w", padx=10, pady=10)
    global clientes
    clientes = ttk.Combobox(marco)

    clientes['values'] = cursor.execute("SELECT nombre FROM clientes").fetchall()
    clientes.grid(row=7, column=1, sticky="w", padx=10, pady=10)
    clientes.bind('<<ComboboxSelected>>', actualizarClientes)

    etiqueta4 = tk.Label(marco, text="Proveedores", bg="blue", font=("Bahnschrift", 12)).grid(row=8, column=0, sticky="w",padx=10, pady=10)
    global proveedores
    proveedores = ttk.Combobox(marco)
    proveedores['values'] = cursor.execute("SELECT nombre FROM proveedores").fetchall()
    proveedores.grid(row=8, column=1, sticky="w", padx=10, pady=10)
    proveedores.bind('<<ComboboxSelected>>', actualizarProveedores)

    etiqueta4 = tk.Label(marco, text="Nombre del producto", bg="blue", font=("Bahnschrift", 12)).grid(row=9, column=0,sticky="w", padx=10,pady=10)
    global Nombreproductos
    Nombreproductos = ttk.Combobox(marco)
    Nombreproductos['values'] = cursor.execute("SELECT nombre FROM productos").fetchall()
    Nombreproductos.grid(row=9, column=1, sticky="w", padx=10, pady=10)
    Nombreproductos.bind('<<ComboboxSelected>>', actualizarProductos)

    etiqueta5 = tk.Label(marco, text="Precio del producto", bg="blue", font=("Bahnschrift", 12)).grid(row=10, column=0,sticky="w",padx=10, pady=10)
    global Precioproductos
    Precioproductos = ttk.Combobox(marco)
    Precioproductos['values'] = (10,20,30,40,50)
    Precioproductos.grid(row=10, column=1, sticky="w", padx=10, pady=10)
    Precioproductos.bind('<<ComboboxSelected>>', actualizarPrecioProductos)

    global tabla
    tabla = ttk.Treeview(marco,
                         columns=("id", "cliente", "proveedor","nombre_producto", "precio_producto"))
    tabla["show"] = "headings"
    tabla.column("#0")
    tabla.column("id", width=150, anchor=tk.CENTER)
    tabla.column("cliente", width=150, anchor=tk.CENTER)
    tabla.column("proveedor", width=150, anchor=tk.CENTER)
    tabla.column("nombre_producto", width=150, anchor=tk.CENTER)
    tabla.column("precio_producto", width=150, anchor=tk.CENTER)

    tabla.heading("id", text="id", anchor=tk.CENTER)
    tabla.heading("cliente", text="cliente", anchor=tk.CENTER)
    tabla.heading("proveedor", text="proveedor", anchor=tk.CENTER)
    tabla.heading("nombre_producto", text="nombre_producto", anchor=tk.CENTER)
    tabla.heading("precio_producto", text="precio_producto", anchor=tk.CENTER)

    conexion = sqlite3.connect('base.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM generar_facturas")

    i = 0
    for a in cursor:
        tabla.insert("", i, text="", values=(a[0], a[1], a[2], a[3], a[4]))
        i += 1
    tabla.bind("<<TreeviewSelect>>", onSelected)
    tabla.place(x=450, y=450)


    global botonGuardar
    botonGuardar = Button(marco)
    botonGuardar.config(text="GUARDAR", width=10, height=2, anchor="center", activebackground="blue", relief="raised",
                        borderwidth=5, font=("Banschrift", 11), command=lambda: guardar())
    botonGuardar.grid(row=13, column=1, sticky="w", padx=100, pady=100)

    global botonImprimir
    botonImprimir = Button(marco)
    botonImprimir.config(text="IMPRIMIR FACTURA", width=10, height=2, anchor="center",
                      activebackground="blue", relief="raised",
                      borderwidth=5, font=("Bahnschrift", 11), command=lambda: accionboton())
    botonImprimir.place(x=700, y=680, width=200)