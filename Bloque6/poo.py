class Persona:

    def __init__(self,nombre,edad,email):
        self.nombre = nombre
        self.edad = edad
        self.email = email
    
    def saludar(self):
        print(f"Soy una persona de nombre {self.nombre}")

    def esMayorEdad(self):
        if self.edad > 18:
            return True
        else:
            return False

    def diferencia_edad(self,edad):
        return self.edad - edad

    def __str__(self):
        return f"Persona de nombre: {self.nombre}, edad: {self.edad} y email: {self.email}"

class Trabajador(Persona):

    def __init__(self,nombre,edad,email,horas,tarifa):
        super().__init__(nombre,edad,email)
        self.horas = horas
        self.tarifa = tarifa

    def __str__(self):
        return super().__str__() + f"-Horas semanales: {self.horas} con tarifa por hora: {self.tarifa}"

    def saludoTrabajador(self):
        print("Soy un trabajador")

    def calcularTarifaSemanal(self):
        return self.horas * self.tarifa



p1 = Persona("pepe",25,"pepe@gmail.com")
#p1.saludar()
p2 = Persona("juan",30,"juan@gmail.com")
#p2.saludar()

#mayorEdad = p1.esMayorEdad()

#diferencia = p1.diferencia_edad(20)

#print(mayorEdad)
#print(diferencia)

#print(p1)
#print(p2)

t1 = Trabajador("ana",25,"ana@gmail.com",30,12)
t1.saludoTrabajador()
print(t1.esMayorEdad())
print(t1.calcularTarifaSemanal())
print(t1)



