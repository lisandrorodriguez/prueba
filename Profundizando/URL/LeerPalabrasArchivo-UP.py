# Leer contenido online
import urllib
from urllib.request import urlopen

palabras = []
# Debido a cambios en la libreria se deben hacer los siguientes cambios:
peticion = urllib.request.Request(
    'http://globalmentoring.com.mx/recursos/GlobalMentoring.txt',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
with urlopen(peticion) as mensaje:
    for linea in mensaje:
        palabras_por_linea = linea.decode('utf-8').split()
        for palabra in palabras_por_linea:
            palabras.append(palabra)

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