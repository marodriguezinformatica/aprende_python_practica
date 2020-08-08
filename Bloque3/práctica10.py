"""Desarrolla un programa solicite constantemente la carga de un número al usuario. 
El programa finalizará cuando el usuario introduzca un 0, 
momento en el que se debe visualizar la suma y el promedio de todos los números introducidos."""

suma = 0
numero = -1
contador = 0
while numero != 0:
    numero = int(input("Introduce un número (0 para terminar)\n"))
    if numero != 0:
        suma = suma + numero
        contador += 1
promedio = round(suma / contador,2)

print(f"La suma de los números introducidos es {suma} y el promedio {promedio}")





