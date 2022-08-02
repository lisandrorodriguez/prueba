from URL.leer_contenido_online import *

# print(palabras)
# print(palabras.count('Universidad')) # Cuantas veces aparece una palabra

# print('Python' in palabras) # Para saber si se encuentra esta cadena en el contenido

cadena = " ".join(palabras)
cadena = cadena.lower()
# print('python'.lower() in cadena.lower()) # Existe python en cadena?
# print(cadena)

# startswith - inicia con
print(cadena.startswith('en globalmentoring.com.mx')) # Para preguntar si el archivo inicia con esta cadena

# endswith - termina con
print(cadena.endswith('globalmentoring.com.mx'))