"""Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float). 
Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio 
y cuántas más bajas."""

alturas = []
suma = 0
for i in range(5):
    altura = float(input(f"Introduce la altura de la persona {i+1}"))
    alturas.append(altura)
    suma += altura

promedio = round(suma / 5,2)

contador_mayor_promedio = 0
contador_menor_promedio = 0
for altura in alturas:
    if altura >= promedio:
        contador_mayor_promedio += 1
    else:
        contador_menor_promedio += 1


print(f"Hay {contador_mayor_promedio} personas con altura mayor que el promedio y {contador_menor_promedio} con altura menor que el promedio")


