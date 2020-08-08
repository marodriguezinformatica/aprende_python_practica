CREATE DATABASE proyecto_final;
USE proyecto_final;
CREATE TABLE cliente (dni VARCHAR(10), nombre VARCHAR(100), dirección VARCHAR(255), telefono INT(9), PRIMARY KEY (dni));
CREATE TABLE producto (idProducto SMALLINT, nombre VARCHAR(100), precio FLOAT, PRIMARY KEY (idProducto));
CREATE TABLE pedido (idPedido VARCHAR(255), dni_cliente VARCHAR(10), PRIMARY KEY (idPedido, dni_cliente), 
FOREIGN KEY (dni_cliente) REFERENCES cliente(dni));
CREATE TABLE lineaPedido (idPedido VARCHAR(255), idLinea SMALLINT, idProducto SMALLINT, cantidad smallint, 
PRIMARY KEY (idPedido,idLinea), FOREIGN KEY (idProducto) REFERENCES producto(idProducto));

INSERT INTO cliente (dni,nombre,dirección,telefono) 
VALUES ("46993520N","Miguel Rodríguez García","Calle Veracruz 3, Madrid","605441123");
INSERT INTO cliente (dni,nombre,dirección,telefono) 
VALUES ("56152518L","Sara Álamo Ruiz","Calle Espronceda 21 1B, Getafe","612005018");
INSERT INTO cliente (dni,nombre,dirección,telefono) 
VALUES ("93400868F","Fernando Giner Ríos","Calle Venenciadores 6 Bajo, Fuenlabrada","646225881");
INSERT INTO cliente (dni,nombre,dirección,telefono) 
VALUES ("14302538B","Alejandra Palacios Sillera","Calle Cerro del Águila 42 3A, Madrid","620633671");

INSERT INTO producto(idProducto,nombre,precio) VALUES(1,"Coca-Cola 33cl",0.45);
INSERT INTO producto(idProducto,nombre,precio) VALUES(2,"Cerveza Mahou 1l",1.2);
INSERT INTO producto(idProducto,nombre,precio) VALUES(3,"Aquarius 1l",1.25);
INSERT INTO producto(idProducto,nombre,precio) VALUES(4,"Cerveza Cruzcampo 33cl",0.75);
INSERT INTO producto(idProducto,nombre,precio) VALUES(5,"Cerveza Cruzcampo 1l",1.3);
INSERT INTO producto(idProducto,nombre,precio) VALUES(6,"Coca-Cola 2l",1.75);
INSERT INTO producto(idProducto,nombre,precio) VALUES(7,"Fanta Naranja 2l",1.6);
INSERT INTO producto(idProducto,nombre,precio) VALUES(8,"Sprite 2l",1.75);
INSERT INTO producto(idProducto,nombre,precio) VALUES(9,"Cerveza Heineken 1l",1.5);
INSERT INTO producto(idProducto,nombre,precio) VALUES(10,"Fantal limón 2l",1.6);
INSERT INTO producto(idProducto,nombre,precio) VALUES(11,"Agua Fontvella 1l",0.75);
INSERT INTO producto(idProducto,nombre,precio) VALUES(12,"Agua Solán de Cabras 1l",0.9);