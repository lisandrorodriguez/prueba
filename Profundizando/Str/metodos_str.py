# Profundizando en el tipo str






# help(str.capitalize)

mensaje1 = 'hola mundo'
mensaje2 = mensaje1.capitalize()
print(f'mensaje1: {mensaje1}, id: {hex(id(mensaje1))}') # Estan en distintas direcciones de memoria, hex, para saber la direccion hexadecimal
print(f'mensaje2: {mensaje2}, id: {hex(id(mensaje2))}')



from mi_clase import MiClase

# help(MiClase) 
print(MiClase.__doc__) # Documentacion de la clase
print(MiClase.__init__.__doc__) # Documentacion de el metodo init

# Funcion help se usa para obtener información sobre alguna clase, metodo, constructor, etc...
help(str)# Imprime la clase de str y sus metodos
variable = "Hola"
print(variable.__len__())

help(str.capitalize) # Muestra informacion sobre como utilizar este modulo, no usar parentesis porque o si no estariamos llamando a la variable



