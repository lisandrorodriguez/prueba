class Persona:
    #init metodo constructor o inicializador

    #necesario para crear objetos en Python 

    #Self: referencia al objeto que se va a crear

    #Doble guion bajo, double underscond or dunder 

    #Atributos que son de los objetos, dentro del init, atributos de la clase, fuera del init

    #Self se conoce tambien como operador dis en otros lenguajes de programacion 

    #*args tuplas de valores **kwargs diccionarios de valores


    def __init__(self,nombre,apellido,edad, *valores, **terminos):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self.valores = valores
        self.terminos = terminos
    
    #Decorador, encapsula el atributo don el metodo
    @property #Se accede al metodo como si fuera un atributo
    def nombre(self):
        print("Llamando método get nombre")
        return self._nombre
    
    #Si solo tuvieramos get, y no el método get de abajo, seria un tipo de código como variables de solo lectura.
    @nombre.setter #De esta manera modificamos el atributo privado usando el metodo, que lo toma como atributo
    def nombre(self,nombre):
        print("Llamando método set nombre")
        self._nombre = nombre
    
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self,apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad


    def mostrarDetalle(self):
        print(f"Nombre: {self._nombre}")
        print(f"Apellido: {self._apellido}")
        print(f"Edad: {self._edad}")
        print(f"Valores pasados como args, tuplas: {self.valores}")
        print(f"Valores pasados como dicc, terminos: {self.terminos}")
    
    def __del__(self):
        print(f"Persona: {self._nombre} {self._apellido}")




#El parentesis... manda a llamar de forma indirecta el metodo init
p1 = Persona("Carlos", "Mohamed", 36, '445522', 2, 3, 4)
#p2 = Persona("Maria", "Fernandez", 29, None, True, False, 1, 3, m="manzana", p="pera")
#p2.mostrarDetalle()

# Persona.mostrarDetalle(p1) llama desde la clase, no es lo comun- 
#p1.telefono = "3624297532" #Crea un nuevo atributo al objeto, pero no se comparte con otros, ejemplo con p2
#print(p1.telefono)
# print(p2.telefono) It'is imposiblle

# Con esto hacemos que solo cuando estemos sobre este modulo se ejecute el codigo
# Sirve para meter código de prueba
if __name__ == '__main__':
    print(p1.nombre)
    p1.nombre = "Lisandro"
    print(p1.nombre)
    print(p1.edad)
    p1.edad = 40
    print(p1.edad)
    p1.mostrarDetalle()


# Se visualiza que archivo se esta ejecutando
print(__name__)
# Si es el mismo, printea como mensaje "__main__"




