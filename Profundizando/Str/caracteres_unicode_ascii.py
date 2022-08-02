# Profundizando en el tipo str

# Caracteres UNICODE - todos los caracteres en python se representan en el sistema Unicode

print('Hola\u0020Mundo') # Indicamos que estamos manejando un caracter unicode. Se ponen 4 caracteres en hexadecimal
print('Notación simple:', '\u0041') # A en unicode
print('Notación extendida:','\U00000041') # Notación extendida
print('Notación hexadecimal','\x41') # Representar A en hexadecimal


# Ventaja de caracter UNICODE, podemos utilizar también Iconos

print('Corazón', '\u2665')

# ASCII Code  caracteres 128 - 2**7 - 7 bits - 1 bit de paridad

caracter = chr(65) # Método char - 65 corresponde al valor decimal de la letra A
print('A mayúscula: ',caracter)

caracter = chr(64) # Arroba
print('Arroba: ',caracter)
