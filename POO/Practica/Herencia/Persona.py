class Persona(object):
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    #Object ya tiene el metodo str, y como lo estoy volviendo a poner, estoy sobreescribiendo ese comportamiento.
    def __str__(self):
        return f" Nombre: {self._nombre} Edad: {self._edad}"

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad

class Empleado(Persona):
    #El método init esta siendo sobreescribida por la clase hija.
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self,sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f"{super().__str__()} Sueldo: {self._sueldo}"

if __name__ == '__main__':
    em1=Empleado("Juan", 30, 78000)
    print(em1.nombre)
    print(em1.edad)
    print(em1.sueldo)



