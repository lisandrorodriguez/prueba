


# caracteres en bytes
caracteres_en_bytes = b'Hola Mundo' # con el prefijo en b indicamos que contiene bytes
print(caracteres_en_bytes) 

mensaje = b'Universidad Python'
print(mensaje[0]) # ASCII 85 = U
print(chr(mensaje[0]))

lista_caracteres = mensaje.split()
print(lista_caracteres)