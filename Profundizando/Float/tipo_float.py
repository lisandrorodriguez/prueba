# Profundizando tipo float

a = 3.0
# print(f"a: {a:.10f}") # Esto se llama interpolación
"""
# Constructor float puede recibir int y str
a = float(10) # El constructor flotante esta sobrecargado
a = float("10")
print(f"a: {a:.2f}") """

# Notacion exponencial
a = float("3e5")
# Valor Positivo
a = float(3e5)
print(f"a: {a}")

# Valor negativo
a = 3e-5
print(f"a: {a:.5f}")

# Cualquier cálculo que involucre un float, se promueve a float

a = 4.0 + 5
print(a)
print(type(a))