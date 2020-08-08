"""Escribir una función que pida un número entero entre 1 y 10 
y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, 
donde n es el número introducido."""

numero = int(input("Introduce un número entre 1 y 10"))

if numero >= 1 and numero <= 10:
    nombre_fichero = "tabla-"+str(numero)+".txt"
    fichero = open(nombre_fichero,"w")
    for i in range(1,11):
        x = numero * i
        fichero.write(str(x)+"\n")
    fichero.close()
else:
    print("Número introducido incorrecto")
