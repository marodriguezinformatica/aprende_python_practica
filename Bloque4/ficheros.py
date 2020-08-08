#Abrir fichero
fichero = open("prueba.txt","a")

#Escribir fichero
fichero.writelines("Nueva línea")

fichero.close()

fichero = open("prueba.txt","r")

#Lectura del contenido
contenido = fichero.read()

print(contenido)

#Cerrar fichero
fichero.close()

