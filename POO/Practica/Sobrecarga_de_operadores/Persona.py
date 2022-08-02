class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Método de suma
    def __add__(self, otroObjeto):
        return self.nombre + " " + otroObjeto.nombre

    # Método de resta
    def __sub__(self, otroObjeto):
        return self.edad - otroObjeto.edad


persona1 = Persona("Juan", 28)
persona2 = Persona("Carlos", 15)

print(persona1 + persona2)
print(persona1 - persona2)
# obj1 + obj2
# Es lo mismo que
# obj1.__ad__(obj2)