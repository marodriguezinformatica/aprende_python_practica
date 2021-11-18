class Agenda:

    def __init__(self):
        self.contactos = []

    def añadir(self):
        print("Añadiendo nuevo contacto")
        nombre = input("Introduzca el nombre: ")
        telefono = int(input("Introduzca el teléfono: "))
        email = input("Introduzca el email: ")
        
        self.contactos.append({'nombre':nombre,'telefono':telefono,'email':email})

    def listar(self):
        print("Listando los contactos de la agenda")

        if len(self.contactos) == 0:
            print("No hay ningún contacto en la agenda")
        else:
            for x in range(len(self.contactos)):
                print(self.contactos[x]['nombre'])

    def buscar(self):
        print("Buscando un contacto")
        nombre = input("Introduzca el nombre del contacto a buscar: ")
        for x in range(len(self.contactos)):
            if nombre == self.contactos[x]['nombre']:
                print("Contacto encontrado")
                print(f"Nombre: {self.contactos[x]['nombre']}")
                print(f"Teléfono: {self.contactos[x]['telefono']}")
                print(f"Email: {self.contactos[x]['email']}")

    
    def editar(self):
        print("Editando un contacto")
        nombre = input("Introduce el nombre del contacto a editar")
        for x in range(len(self.contactos)):
            if nombre == self.contactos[x]['nombre']:
                nuevo_nombre = input("Introduce el nuevo nombre del contado: ")
                nuevo_telefono = int(input("Introduce el nuevo teléfono del contado: "))
                nuevo_email = input("Introduce el nuevo email del contacto")
                self.contactos[x]['nombre'] = nuevo_nombre
                self.contactos[x]['telefono'] = nuevo_telefono
                self.contactos[x]['email'] = nuevo_email


agenda1 = Agenda()
agenda1.añadir()
agenda1.añadir()
agenda1.listar()
agenda1.buscar()
agenda1.editar()
agenda1.listar()