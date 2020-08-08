import pymysql

def seleccionar_clientes():

    conexion = pymysql.connect(host="localhost", user="root", passwd="pass", database="proyecto_final")

    cursor = conexion.cursor()
    sql = "SELECT * from cliente order by dni"

    cursor.execute(sql)
    clientes = cursor.fetchall()

    conexion.close()

    return clientes

def seleccionar_productos():
    conexion = pymysql.connect(host="localhost", user="root", passwd="pass", database="proyecto_final")

    cursor= conexion.cursor()
    sql = "SELECT * from producto order by nombre"

    cursor.execute(sql)
    productos = cursor.fetchall()

    conexion.close()
    return productos

def insertar_pedido(idPedido,dniCliente):
    conexion = pymysql.connect(host="localhost", user="root", passwd="pass", database="proyecto_final")

    cursor= conexion.cursor()
    sql = "INSERT into pedido(idPedido,dni_cliente) values('" + idPedido + "','" + dniCliente + "')"

    cursor.execute(sql)
    conexion.commit()
    conexion.close()

def insertar_lineas_pedido(idPedido,carrito):
    conexion = pymysql.connect(host="localhost", user="root", passwd="pass", database="proyecto_final")

    cursor= conexion.cursor()

    index = 1
    for elemento in carrito:
        sql = "INSERT into lineaPedido(idPedido,idLinea,idProducto,cantidad) values ('" + idPedido + "'," + str(index) + "," + str(elemento[0]) + "," + str(elemento[3]) + ")"
        cursor.execute(sql)
        conexion.commit()
        index += 1
        
    conexion.close()

        