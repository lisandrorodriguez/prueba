

# Convertir str a bytes

string = 'Programación en Python'
print('String original: {}'.format(string))
bytes = string.encode(('UTF-8')) # Se convierte de forma automatica a bytes
print(f'Bytes codificados: {bytes}')



# Convertir de bytes a Str

string2 = bytes.decode('UTF-8')
print(f'String decodificado: {string2}')
