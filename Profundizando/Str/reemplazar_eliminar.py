# Remplazar contenido de un string

titulo = '10/05/2000'

print(titulo.replace('/', ' '))

# Eliminar cararacteres al inicio y al final de un str

cadena1 = '  *** I have string knowledge\'s ***  '
# print(f'Cadena original: {cadena1}')
cadena2 = cadena1.strip() #Quita los espacios en blancos al final y al inicio de una cadena
# print(f'Cadena sin espacios en blanco: {cadena2}')
# print(len(cadena1),len(cadena2))

print(cadena1.strip('*')) 

print('***holamundo***'.strip('*'))# Elimina todos los caracteres seleccionados
print('***holamundo***'.lstrip('*')) # Elimina los caracteres que coinciden del lado izquier
print('***holamundo***'.rstrip('*')) # Elimina los caracteres que coinciden del lado derecho

print(cadena1.strip().strip('*').strip()) # Elimina los espacios en blanco y asteriscos, clean str

