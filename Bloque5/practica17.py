"""Escribir una función que reciba como parámetros una lista y un número. 
La función debe multiplicar cada elemento de la lista por el número y devolver la lista resultante."""

def multiplica_lista_x_numero(lista,numero):
    for x in range(len(lista)):
        lista[x] = lista[x] * numero
    return lista

lista = [1,2,3,4,5,6]
numero = 7
resultado = multiplica_lista_x_numero(lista,numero)

print(resultado)
