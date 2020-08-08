"""Escribir un programa que solicite dos fechas al usuario con el formato dd/mm/yyyy. 
A continuación debe crear dos tuplas y almacenar el día, mes y año de las fechas en dichas tuplas. 
Por último, tiene que mostrar cual de las fechas es la más reciente."""

fecha1 = input("Introduce la primera fecha con formato dd/mm/yyyy\n")
fecha2 = input("Introduce la segunda fecha con formato dd/mm/yyyy\n")

lista_fecha1 = fecha1.split("/")
tupla1 = tuple(lista_fecha1)
tupla2 = tuple(fecha2.split("/"))

dia1 = int(tupla1[0])
mes1 = int(tupla1[1])
año1 = int(tupla1[2])

dia2 = int(tupla2[0])
mes2 = int(tupla2[1])
año2 = int(tupla2[2])

if año1 > año2:
    print("Fecha más reciente: " + fecha1)
elif año2 > año1:
    print("Fecha más reciente: " + fecha2)
else:
    if mes1 > mes2:
        print("Fecha más reciente: " + fecha1)
    elif mes2 > mes1:
        print("Fecha más reciente: " + fecha2)
    else:
        if dia1 > dia2:
            print("Fecha más reciente: " + fecha1)
        elif dia2 > dia1:
            print("Fecha más reciente: " + fecha2)
        else:
            print("Las fechas son iguales")



