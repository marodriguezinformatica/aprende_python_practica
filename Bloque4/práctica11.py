"""Escribir un programa que solicite la entrada de una oración al usuario 
y devuelva el número de espacios en blanco que contiene."""

oracion = input("Introduce una oración\n")
contador = 0

"""for caracter in oracion:
    if caracter == " ":
        contador += 1"""

for x in range(len(oracion)):
    if oracion[x] == " ":
        contador += 1


print(f"El número de espacios en blanco es: {contador}")
