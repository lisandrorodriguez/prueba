class Vehiculo(object):
    def __init__(self, color, ruedas):
        self.color = str(color)
        self.ruedas = int(ruedas)

    def __str__(self):
        return f'Color: {self.color} Cantidad de Ruedas: {self.ruedas}'
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color,ruedas)
        self.velocidad = velocidad
    
    def __str__(self):
        return f"{super().__str__} Velocidad: {str(self.velocidad)}"

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return f"{super().__str__()} Tipo: {str(self.tipo)}"


amarok = Vehiculo("rojo",4)
golsito = Coche("blanco",4,120)
bmx = Bicicleta("Blanca", 2, "Todo terreno")
print(amarok, golsito, bmx) 

    
    
