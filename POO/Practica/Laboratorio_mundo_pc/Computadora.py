from Monitor import Monitor
from Mouse import Mouse
from Teclado import Teclado

class Computadora:

    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):

        Computadora.contador_computadoras += 1
        self.idcomputadora = Computadora.contador_computadoras
        self.nombre = nombre
        self.monitor = monitor
        self.raton = raton
        self.teclado = teclado

    def __str__(self):
        return f"Computadora ID: {self.idcomputadora} compuesta por:\n\t{self.monitor}\n\t{self.raton}\n\t{self.teclado}"


if __name__ == '__main__':
    teclado1 = Teclado("USB", "HP")
    mouse1 = Mouse("USB","HP")
    monitor1 = Monitor("SAMSUNG", 25)
    computadora = Computadora("Dell", monitor1, teclado1, mouse1)
    print(computadora)