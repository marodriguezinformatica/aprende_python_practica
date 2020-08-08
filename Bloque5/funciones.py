def suma(op1,op2):
    res = op1 + op2
    return res
    


print("Bienvenidos al programa que realiza sumas")
operando1 = int(input("Introduce el primer operando\n"))
operando2 = int(input("Introduce el segundo operando\n"))
resultado = suma(operando1,operando2)
print(f"El resultado de sumar {operando1} y {operando2} es {resultado}")

