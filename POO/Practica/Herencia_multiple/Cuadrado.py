# El orgen en el cual se agregan las clases es importante.
from Color import Color
from FiguraGeometrica import FiguraGeometrica
# En caso de que queramos renmobrar la clase from FiguraGeometrica import FiguraGeometrica as NuevaClase

class Cuadrado(FiguraGeometrica, Color):
        # La variable de lado se utiliza para inicializar los atributos de figura geometrica
    def __init__(self, lado, color):
        # super().__init__(lado)
        # Ya que estamos en un cuadrado, el ancho y el alto son lo mismo
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcularArea(self):
        return self.alto * self.ancho

    def __str__(self):
        return f"{FiguraGeometrica.__str__(self)} + {Color.__str__(self)}"
    
