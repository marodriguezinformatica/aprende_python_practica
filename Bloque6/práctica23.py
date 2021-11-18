class Triangulo:

    def __init__(self,lado1,lado2,lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def ladoMayor(self):
        if self.lado1 >= self.lado2 and self.lado1 >= self.lado3:
            print (f"El lado mayor es {self.lado1}")
        elif self.lado2 > self.lado1 and self.lado2 >= self.lado3:
            print (f"El lado mayor es {self.lado2}")
        else:
            print (f"El lado mayor es {self.lado3}")

    def tipoTriangulo(self):
        if self.lado1 == self.lado2 and self.lado2 == self.lado3:
            print("Equilátero")
        elif self.lado1 != self.lado2 and self.lado2 != self.lado3:
            print("Escaleno")
        else:
            print("Isósceles")
    
    def __str__(self):
        return f"Triángulo de lados: {self.lado1}, {self.lado2}, {self.lado3}"


t1 = Triangulo(2,3,4)
t2 = Triangulo(2,2,8)

t1.ladoMayor()
t1.tipoTriangulo()
print(t1)
t2.ladoMayor()
t2.tipoTriangulo()
print(t2)