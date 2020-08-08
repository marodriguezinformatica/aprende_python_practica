"""Desarrollar una aplicación para la gestión de empleados de una empresa. La aplicación mostrará un menú con las siguientes opciones:
1- Inicializar: Creará la base de datos y la tabla (si no existen) donde almacenar los empleados.
2- Insertar empleado: Pedirá dni, nombre y apellidos, edad y departamento, y realizará la inserción del empleado en la base de datos.
3- Consultar: Pedirá el dni del empleado y mostrará sus datos.
4- Finalizar: Saldrá de la aplicación."""

import pymysql

def inicializar():
    conexion = pymysql.connect(host="localhost",user="root",passwd="pass")

    cursor= conexion.cursor()

    sql = "CREATE database if not exists práctica21"
    cursor.execute(sql)

    sql = "USE práctica21"
    cursor.execute(sql)

    sql = "CREATE table if not exists empleados(dni varchar(10), nombre varchar(255), edad smallint, departamento varchar(255))"
    cursor.execute(sql)

    conexion.close()

def insertar_empleado(dni,nombre,edad,departamento):
    conexion = pymysql.connect(host="localhost",user="root",passwd="pass",database="práctica21")

    cursor = conexion.cursor()

    sql = "INSERT into empleados(dni,nombre,edad,departamento) values('" + dni + "', '" + nombre + "'," + str(edad) + ",'" + departamento + "')"
    cursor.execute(sql)

    conexion.commit()
    conexion.close()

def consultar_empleado(dni):
    conexion = pymysql.connect(host="localhost",user="root",passwd="pass",database="práctica21")

    cursor = conexion.cursor()

    sql = "SELECT * from empleados where dni = '" + dni + "'"

    cursor.execute(sql)
    filas = cursor.fetchall()

    if len(filas) == 0:
        print("Empleado no encontrado")
    else:
        for fila in filas:
            print(f"Empleado con dni {fila[0]}, de nombre {fila[1]} y edad {fila[2]}. Trabaja en el departamento {fila[3]}")

    conexion.close()

opcion = -1

while opcion != 4:
    opcion = int(input("Introduce alguna de las opciones siguientes:\n1-Inicializar base de datos\n2-Insertar empleado\n3-Consultar empleado\n4-Salir\n"))

    if opcion == 1:
        inicializar()
    elif opcion == 2:
        dni = input("Introduce dni\n")
        nombre= input("Introduce nombre y apellidos\n")
        edad = int(input("Introduce edad\n"))
        departamento = input("Introduce departamento\n")
        insertar_empleado(dni,nombre,edad,departamento)
    elif opcion == 3:
        dni = input("Introduce dni\n")
        consultar_empleado(dni)
    elif opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4:
        print("Opción seleccionada no válida")