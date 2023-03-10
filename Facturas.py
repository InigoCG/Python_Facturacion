from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import subprocess

imagen = "imagen1.png"

def imprimirLogo():
    logo = ImageReader(imagen)
    canvasPDF.drawImage(logo, x=10, y=740, width=100, height=100)

def imprimirCabecera(nombreFactura):
    nombreFactura = nombreFactura.replace("_", " Nº ").upper()

    imprimirEtiqueta(x=500, y=750, text=nombreFactura)
    canvasPDF.line(x1=0, y1=730, x2=600, y2=730)

def imprimirCliente(cliente):
    etiquetaCliente = "CLIENTE:"
    imprimirEtiqueta(x=25, y=700, text=etiquetaCliente)
    imprimirEtiqueta(x=300, y=700, text=cliente[0])

def imprimirEtiqueta(x, y, text):
    canvasPDF.drawString(x=x, y=y, text=text)

def imprimirProductos(productos):
    imprimirEtiqueta(x=25, y=650, text="PROVEEDOR: ")
    imprimirEtiqueta(x=25, y=600, text="NOMBRE DEL PRODUCTO: ")
    imprimirEtiqueta(x=25, y=550, text="PRECIO: ")


    imprimirEtiqueta(x=300, y=650, text=str(productos[1]))
    imprimirEtiqueta(x=300, y=600, text=str(productos[2]))
    imprimirEtiqueta(x=300, y=550, text=str(productos[3]))

def imprimirFactura(id ,datosFactura):
    nombreFactura = "Factura_" + str(id)

    global canvasPDF
    canvasPDF = canvas.Canvas(nombreFactura + ".pdf", pagesize=A4)

    imprimirLogo()
    imprimirCabecera(nombreFactura)
    imprimirCliente(datosFactura)
    imprimirProductos(datosFactura)

    canvasPDF.save()
    canvasPDF.showPage()
    subprocess.Popen([nombreFactura + ".pdf"], shell=True)