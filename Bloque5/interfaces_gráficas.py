from tkinter import *
from tkinter.ttk import *

def saludar():
    lbl.configure(text="Botón pulsado")
    txt.delete(0,END)
    txt.insert(0,listbox.get(ACTIVE))

ventana = Tk(className="Interfaz gráfica")
ventana.geometry("400x300")

#Etiqueta
lbl = Label(ventana,text="Hola mundo tKinter!")
lbl.place(x=100,y=0,in_=ventana)

#Botón
btn = Button(ventana,text="Saludar",command=saludar)
btn.place(x=100,y=50,in_=ventana)

#Caja de texto
txt = Entry(ventana,width=30)
txt.place(x=100,y=100,in_=ventana)

#Combobox
combo = Combobox(ventana,width=30)
combo.place(x=100,y=150,in_=ventana)
combo["values"] = (1,2,3,4,5,"Text")
combo.current(1)

#Listbox
listbox = Listbox(ventana,height=4)
listbox.insert(0,"valor1")
listbox.insert(1,"valor2")
listbox.insert(2,"valor3")
listbox.place(x=100,y=200,in_=ventana)

ventana.mainloop()



