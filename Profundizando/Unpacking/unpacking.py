# Unpacking, del lado derecho se puede generar una lista o tuplas de valores

valores = 1,2,3 # Se genera una tupla de valores

# print(valores)
# print(type(valores))

valor1, valor2, valor3 = 1, 2, 3 # Se asignan one to one de forma independiente
# print(valor1, valor2, valor3)


valor1, _, valor3 = 1, 2, 3 # El segundo valor se asigna al guión bajo, pero queda inutilizada la variable
# print(valor1,valor3) 

valor1, valor2, *valor3 = 1,2,3,4,5,6,7,8,9 # Se asigna el resto de los valores como una lista al parametro pasado como args
# print(valor1, valor2, valor3)

valor1, valor2, *valor3, valor4, valor5 = 1,2,3,4,5,6,7,8

print(valor1, valor2, valor3, valor4, valor5)


def regresa_varios_datos():
    return 1,2,3

valor1, valor2, valor3 = regresa_varios_datos()
print(valor1,valor2,valor3)

valor1, *_ = regresa_varios_datos()
print(valor1)
