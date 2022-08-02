class Aritmetica:
    pass
    """ Doc String (triple comilla) es comentarios para clases 
        Clase Aritmetica para realizar las operaciones de sumar, restar, etc"""
    def __init__(self, operandoA,operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    
    def sumar(self):
        return self.operandoA + self.operandoB
    
    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB
    
    def dividir(self):
        return self.operandoA / self.operandoB


ar1 = Aritmetica(1,2)
print(f"Suma: {ar1.sumar()}")
print(f"Resta: {ar1.restar()}")
print(f"Multiplicación: {ar1.multiplicar()}")
print(f"División: {ar1.dividir():.2f}")
