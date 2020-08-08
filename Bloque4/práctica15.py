"""Desarrollar un programa que simule un traductor inglés-español. Al iniciar el programa, aparecerá un menú con las siguientes opciones:
1- Insertar palabra: Solicitará al usuario una palabra en inglés y su traducción en español, y la añadirá al diccionario.
2- Traducir texto: Solicitará al usuario un texto, y mostrará por pantalla la traducción del mismo. Las palabras que no se encuentren en el diccionario, las traducirá como X.
3- Salir: La aplicación finalizará."""

opcion = -1
diccionario = {}

while opcion != "3":
    opcion = input("Introduce alguna de las opciones\n1-Insertar palabra\n2-Traducir texto\n3-Salir\n")
    if opcion == "1":
       palabra = input("Introduce palabra en inglés\n") 
       traduccion = input(f"Introduce la traducción a español de la palabra {palabra}\n")
       diccionario[palabra] = traduccion
    elif opcion == "2":
        texto = input("Introduce el texto que desea traducir\n")
        texto_traducido = ""
        lista_palabras = texto.split()
        for palabra in lista_palabras:
            if palabra in diccionario:
                traduccion = diccionario[palabra]
                texto_traducido += traduccion + " "
            else:
                texto_traducido += "X" + " "
        print(texto_traducido) 
    elif opcion != "1" and opcion != "2" and opcion != "3":
        print("Opción incorrecta")

print("TRADUCTOR FINALIZADO")


