from Computadora import Computadora
from Teclado import Teclado
from Mouse import Mouse
from Monitor import Monitor

class Orden:

    contador_ordenes = 0

    def __init__(self,computadora):
        Orden.contador_ordenes += 1
        self.id = Orden.contador_ordenes
        self.computadora = computadora

    def agregarComputadora(self, computadora):
        self.computadora.append(computadora)
    
    def __str__(self):
        computadoras_str = ''
        for computadora in self.computadora:
            computadoras_str += computadora.__str__()
        return f"""
        Orden: {self.id}
        Computadoras: {computadoras_str}
        """


teclado1 = Teclado("USB", "HP")
mouse1 = Mouse("USB","HP")
monitor1 = Monitor("SAMSUNG", 25)
computadora = Computadora("Dell", monitor1, teclado1, mouse1)
print(computadora)
et = [computadora]

orden1 = Orden(et)
print(orden1)
