# bool contiene los valores True y False
# Tipos numericos, False para 0 y True demas valores

'''
Ocho formas de generar un bool False en Python
1. Comilla simple o doble ''/" (cadena vacía)
2. Lista vacia []
3. Tupla vacia ()
4. Diccionario vacio {}
5. Entero 0
6. Flotante 0.0
7. bool False
8. None
'''

valor = 0 
resultado = bool(valor) # Ya que es 0, transforma a Falso

print(f'Valor {valor}, resultado: {resultado}')

valor = 1
resultado = bool(valor) # Cualquier numero entero distinto de 0 regresa True

print(f'Valor {valor}, resultado: {resultado}')



# Tipo str, False para '', True para demas valores



valor = '' # False
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

valor = 'Hola Mundo!' # True
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')



# Tipo colecciones, False para colecciones vacias, True para todas las demas colecciones
# Lista

valor = [] # False
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')


valor = [1,2,3] # True
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')


# Tupla

valor = () # False
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')


valor = (1,2,3) # True
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

# Diccionario

valor = {} # False
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

valor = {"nombre":"Jorge"} # True
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

if '':
    print("Regreso verdadero")
else:
    print("Regreso falso")

    










