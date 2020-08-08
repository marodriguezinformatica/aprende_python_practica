"""Desarrollar un programa con interfaz gráfica destinado a la conversión de divisas. 
El usuario podrá insertar el número de euros que quiere convertir y, mediante un botón, 
proceder a su conversión a dólares y libras."""

from tkinter import *
from tkinter.messagebox import *

def convertir():
    try:
        euros = float(txtEuros.get())
        dolares = round(euros * 1.17,2)
        libras = round(euros * 0.9, 2)

        txtDolares.config(state="normal")
        txtDolares.delete(0,END)
        txtDolares.insert(0,dolares)
        txtDolares.config(state="disabled")
        txtLibras.config(state="normal")
        txtLibras.delete(0,END)
        txtLibras.insert(0,libras)
        txtLibras.config(state="disabled")
    except:
        print("Error, imposible realizar la conversión")
        showerror(message="Error, imposible realizar la conversión", title="Error")

ventana = Tk(className="Práctica 22")
ventana.geometry("500x200")

lblTitulo = Label(ventana, text="Conversor de monedas")
lblTitulo.place(x=80,y=10,in_=ventana)
lblTitulo.config(font=("Courier",22))

lblEuros = Label(ventana, text="Euros")
lblEuros.place(x=70, y=80, in_=ventana)

txtEuros = Entry(ventana, width=10)
txtEuros.place(x=60,y=100, in_=ventana)

lblDolares = Label(ventana, text="Dólares")
lblDolares.place(x=350,y=60, in_=ventana)

txtDolares = Entry(ventana, width=10)
txtDolares.place(x=340,y=80, in_=ventana)
txtDolares.config(state="disabled")

lblLibras = Label(ventana, text="Libras")
lblLibras.place(x=350,y=100)

txtLibras = Entry(ventana, width=10)
txtLibras.place(x=340,y=120,in_=ventana)
txtLibras.config(state="disabled")

btnConvertir = Button(ventana, text="Convertir", command=convertir, bg="red")
btnConvertir.place(x=180,y=95,in_=ventana)


ventana.mainloop()
