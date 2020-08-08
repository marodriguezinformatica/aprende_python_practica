"""Desarrolla un programa que solicite la carga de un número al usuario. 
A continuación, deberá pedir las notas de ese número de alumnos, 
y mostrar por pantalla el número de alumnos aprobados y suspensos."""

numero = int(input("Introduce el número de alumnos\n"))

contador_aprobados=0
contador_suspensos=0
for x in range(1,numero+1):
    nota = float(input(f"Introduce la nota del alumno {x}\n"))
    if nota >= 5:
        contador_aprobados += 1
    else:
        contador_suspensos += 1
print(f"El número de aprobados ha sido {contador_aprobados} y el número de suspensos {contador_suspensos}")

