"""Desarrolla una calculadora de enteros. El programa deberá pedir los dos operandos al usuario y realizar las operaciones básicas: suma, resta, multiplicación y división.
Controlar las excepciones que se puedan  producir."""

try:
    operando1 = int(input("Introduce el primer operando\n"))
    operando2 = int(input("Introduce el segundo operando\n"))
except:
    print("Los operandos introducidos no son válidos. Se establecerán valores por defecto para los operandos")
    operando1 = 1
    operando2 = 1

suma = operando1 + operando2
resta = operando1 + operando2
multiplicacion = operando1 * operando2
try:
    division = round(operando1 / operando2,2)
except:
    print("Error en la división")
    division = "ERROR"


print(f"El resultado de sumar {operando1} y {operando2} es {suma}")
print(f"El resultado de restar {operando1} y {operando2} es {resta}")
print(f"El resultado de multiplicar {operando1} y {operando2} es {multiplicacion}")
print(f"El resultado de dividir {operando1} y {operando2} es {division}")


