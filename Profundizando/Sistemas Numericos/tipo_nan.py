import math # Contiene un metodo para preguntar a una variable si es not a number
from decimal import Decimal

# Not a Number - NaN
# Es un tipo de dato numerico indefinido
# Puede ser el resultado de una operacion matematica similar al infinito

# METODO FLOAT

a = float("NaN") # No es sensible a mayusculas

print(f"a: {a}")

print(f"Es NaN (not a number)?: {math.isnan(a)}")

# METODO DECIMAL

a = Decimal('NaN')

print(f"Es NaN (not a number)?: {math.isnan(a)}")

