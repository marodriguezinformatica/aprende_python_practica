"""Escribir un programa que cree un diccionario simulando una cesta de la compra. 
El programa debe preguntar el artículo y su precio y añadir el par al diccionario, 
hasta que el usuario decida terminar (pulse tecla f). 
Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato:"""

producto = ""
cesta = {}
while producto.upper() != "F":
    producto = input("Indica el producto a comprar, o pulsa la tecla f para salir\n")
    
    if producto.upper() != "F":
        precio = float(input(f"Introduce el precio del producto {producto}\n"))
        cesta[producto] = precio

print("Lista de la compra")
suma = 0

for producto in cesta:
    precio = cesta[producto]
    suma = suma + precio
    print(f"{producto}      {precio}")

print(f"Total       {suma}")


