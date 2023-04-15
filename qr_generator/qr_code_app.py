#Importar librerías
from tkinter import *
import qrcode

#Crear ventana - Parametros basicos
ventana = Tk()
ventana.title("QR Generator")
ventana.iconbitmap('Icon/qr.ico')
ventana.geometry("1000x550")
ventana.configure(bg="#7C96AB")
ventana.resizable(False, False)

#Funciones
def generate():
    name=title.get()
    text=entry.get()
    qr=qrcode.make(text)
    qr.save("QRCode/" + str(name)+".png")
    global Image
    Image=PhotoImage(file="QRcode/"+ str(name)+ ".png")
    Image_view.config(image=Image)

Image_view = Label(ventana, bg = "#7C96AB")
Image_view.pack(padx=50, pady=10, side=RIGHT)


#frame1 = LabelFrame(ventana, text="Ingrese la información", pady=10)
#frame1.place(x=50, y=150)

label1 = Label(ventana, text ="Nombre Archivo QR" , fg = "White", bg="#7C96AB", font = ("Courier",15))
label1.place(x=50, y=170)

title = Entry(ventana, width=28, font=("Courier", 15))
title.place(x=50, y=200)

label2 = Label(ventana, text ="Inserte aquí el texto a codificar:" , fg = "White", bg="#7C96AB", font = ("Courier",15))
label2.place(x=50, y=250)

entry = Entry(ventana, width=28, font=("Courier", 15))
entry.place(x=50, y=280)

btn1 = Button(ventana, text="Generate", width =20 , height=2, bg="black", fg="white", font="Courier", command= generate)
btn1.place(x=50, y=350)

#Bucle infinito (Mantiene abierta la ventana/ aplicación)
ventana.mainloop()