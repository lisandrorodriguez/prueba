class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcularArea(self):
        return self.base * self.altura

base = int(input("Ingrese la medida de la base: "))
altura = int(input("Ingrese la medida de la altura: "))

r1 = Rectangulo(base,altura)
print("El area es:",r1.calcularArea())
