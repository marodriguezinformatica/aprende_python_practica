#Escribe un programa que pida al usuario el radio de un círculo y calcule su área, sabiendo que: Área = πr2
radio = float(input("Introduce el radio del círculo"))
pi = 3.14
area = round(pi * pow(radio,2),2)
print(f"El área del círculo de radio {radio} es {area}")
