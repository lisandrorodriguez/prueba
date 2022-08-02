
class Persona:

    contador_personas = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"Persona {self.id_persona} {self.nombre} {self.edad}"

p1 = Persona("Juan", 28)
p2 = Persona("Samira", 15)
print(p1)
print(p2)
print(f"Valor contador persona: {Persona.contador_personas}")