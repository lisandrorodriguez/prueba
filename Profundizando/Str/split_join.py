# Profundizando en el tipo str


# help(str.split)

cursos = 'Java Python JavaScript Angular Spring Excel'
lista_cursos = cursos.split()
# print(f"lista cursos: {lista_cursos}")

cursos_separados_coma = 'Java,Python,JavaScript,Angular,Spring,Excel'
lista_cursos = cursos_separados_coma.split(sep=",", maxsplit=2) # Max Split, separa los primeros elementos indicados, el resto los deja en la misma cadena de caracteres
# print(f"lista cursos: {lista_cursos}")


"""

"""
# help(str.join)

tupla_str = ('Hola','Mundo','Universidad','Python') 
mensaje = ' '.join(tupla_str) # Pone un elemento en cada terminacion de elementos
# print(f'mensaje: {mensaje}')

lista_cursos = ['Java', 'Python', 'Angular', 'Spring']
mensaje = ', '.join(lista_cursos)
# print(f'mensaje: {mensaje}')

cadena='HolaMundo'
mensaje = '.'.join(cadena)
# print(f'mensaje: {mensaje}')


diccionario = {'nombre':'Juan', 'apellido':'Perez', 'edad':'18'}
llaves = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
# print(f'llaves: {llaves}, type: {type(llaves)}')
# print(f'valores: {valores}, type: {type(valores)}')
