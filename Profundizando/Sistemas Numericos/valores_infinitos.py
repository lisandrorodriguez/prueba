import math
from decimal import Decimal

# Manejo de valores infinitos

# UTILIZANDO EL CONSTRUCTOR FLOAT

# Valor positivo mas grande. el valor mas grande

"""

infinito_positivo = float("inf") # Esto representa el valor de infinito
print(f"Infinito positivo: {infinito_positivo}")
print(f"Es infinito: {math.isinf(infinito_positivo)}")

infinito_positivo = "inf" # No usamos el constructor float entonces no lo convierte en infinito

#print(f"Es infinito: {math.isinf(infinito_positivo)}") #TypeError

infinito_negativo = float("-inf")
print(f"Infinito negativo: {infinito_negativo}")
print(f"Es infinito?: {math.isinf(infinito_negativo)}")


# UTILIZANDO EL MODULO DE MATH

"""

"""
infinito_positivo = math.inf
print(f"Infinito positivo: {infinito_positivo}")
print(f"Es infinito: {math.isinf(infinito_positivo)}")

infinito_negativo = -math.inf
print(f"Infinito negativo: {infinito_negativo}")
print(f"Es infinito?: {math.isinf(infinito_negativo)}")

"""

# UTILIZANDO EL MODULO DECIMAL

infinito_positivo = Decimal("Infinity")
print(f"Infinito positivo: {infinito_positivo}")
print(f"Es infinito: {math.isinf(infinito_positivo)}")

infinito_negativo = Decimal("-Infinity")
print(f"Infinito negativo: {infinito_negativo}")
print(f"Es infinito?: {math.isinf(infinito_negativo)}")
