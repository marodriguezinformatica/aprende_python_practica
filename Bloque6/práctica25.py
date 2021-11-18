class Vehiculo():

    def __init__(self,num_bastidor,peso):
        self.num_bastidor = num_bastidor
        self.peso = peso

    def __str__(self):
        return f"Coche con bastidor: {self.num_bastidor} y peso: {self.peso}"

    def impuesto_base(self):
        return 0.45*self.peso

class Electrico(Vehiculo):

    def __init__(self,num_bastidor,peso,precio):
        super().__init__(num_bastidor,peso)
        self.precio = precio

    def impuesto_total(self):
        return 0.09*self.precio + super().impuesto_base()

    def __str__(self):
        return super().__str__() + f"-Vehículo eléctrico de precio: {self.precio}"

class Combustion(Vehiculo):

    def __init__(self,num_bastidor,peso,cilindrada):
        super().__init__(num_bastidor,peso)
        self.cilindrada = cilindrada

    def impuesto_total(self):
        return 3*self.cilindrada + super().impuesto_base()

    def __str__(self):
        return super().__str__() + f"-Vehículo combustión de cilindrada: {self.cilindrada}"

e1 = Electrico(34566,250,23000)
e2 = Electrico(11111,300,25000)
c1 = Combustion(22222,500,20000)
c2 = Combustion(33333,550,18000)

coches = [e1,e2,c1,c2]

for x in range(len(coches)):
    print(f"Coche en la posicion {x}")
    print(coches[x])
    print(coches[x].impuesto_total())