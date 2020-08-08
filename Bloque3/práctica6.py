"""Escribir un programa que pida las tres notas de un alumno. 
Si el promedio es mayor o igual a 5, mostrar un mensaje “Promocionado”."""

nota1 = float(input("Introduce la nota 1\n"))
nota2 = float(input("Introduce la nota 2\n"))
nota3 = float(input("Introduce la nota 3\n"))

promedio = (nota1 + nota2 + nota3)/3

if promedio >= 5:
    print("PROMOCIONADO")
else:
    print("NO PROMOCIONADO")