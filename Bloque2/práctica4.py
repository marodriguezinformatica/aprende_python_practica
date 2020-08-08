"""Escribe un programa que pida al usuario los grados centígrados que quiere convertir, y muestre por pantalla la equivalencia con grados kelvin y grados farenheit.
	ºK = 273 + ºC
	ºF = 1,8*ºC + 32"""

try:
	centigrados = int(input("Introduce los grados centígrados que quieres convertir\n"))
except:
	print("Los grados centígrados introducidos no son correctos. Se creará una cantidad de grados por defecto igual a 40")
	centigrados = 40
kelvin = 273 + centigrados
farenheit = 1.8 * centigrados + 32

print(f"{centigrados} grados centígrados equivalen a {kelvin} grados kelvin y a {farenheit} grados farenheit")
