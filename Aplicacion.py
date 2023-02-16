# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 13:10:57 2023

@author: user
"""

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import Tk, Button

from Clientes import altaClientes
from Productos import altaProductos
from Proveedores import altaProveedores


def saludar(texto):
    print(texto)
    if texto == 'Clientes':
        messagebox.showinfo(message=texto, title="Opción Elegida:")
        altaClientes()
    elif texto == 'Proveedores':
        messagebox.showinfo(message=texto, title="Opción Elegida:")
        altaProveedores()
    elif texto == 'Productos':
        messagebox.showinfo(message=texto, title="Opción Elegida:")
        altaProductos()
    elif texto == 'Generar factura':
        messagebox.showinfo(message=texto, title="Opción Elegida:")
    elif texto == 'Emitir factura':
        messagebox.showinfo(message=texto, title="Opción Elegida:")
    elif texto == 'Salir':
        messagebox.showinfo(message=texto, title="Opción Elegida:")
        raiz.destroy()

botones = ['Clientes', 'Proveedores', 'Productos', 'Generar factura', 'Emitir factura', 'Salir']
y = 0
z = 0
raiz = Tk()
raiz.title("Facturacion")
raiz.iconbitmap("icono.ico")
raiz.state('zoomed')
marco = Frame(raiz)
marco.config(bg="#0061FF")
marco.config(width="1024", height="768", bd="10", relief="groove")
marco.pack()

titulo = Label(marco, bg="pink", text="Aplicación de Facturación", font=("Bahnschrift",60)).place(x=40, y=10)

imagen1 = PhotoImage(file="imagen1.png")
etiqueta = Label(marco, image=imagen1, bg="green", bd="10", relief="groove").place(x=100, y=190)

listaBotones = []
for i in range(len(botones)):
    listaBotones.append(Button(marco))

for i in range(len(listaBotones)):
    z+=90
    listaBotones[i].config(text=botones[i], width=20, height=2, anchor="center",
                           activebackground="red", relief="raised",
                           borderwidth=5, font=("Bahnschrift",14),
                           command=lambda m=botones[i]: saludar(m))
    listaBotones[i].place(x=700, y=110+z)
    
raiz.mainloop()