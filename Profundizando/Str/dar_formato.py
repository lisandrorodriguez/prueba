# Profundizando en el tipo str

# Dar formato a un str


# MÉTODO 1

nombre = 'Juan'
edad = 28
mensaje_con_formato = 'Mi nombre es %s y tengo %d'%(nombre,edad) 

# print(mensaje_con_formato)
persona = ('Karla','Gomez',5000.00)

mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f'%persona
# print(mensaje_con_formato)

mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f'
# print(mensaje_con_formato%persona)

# MÉTODO 2

nombre = 'Juan'
edad = 28
sueldo = 3000
mensaje_con_formato = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre,edad,sueldo)
#print(mensaje_con_formato)


# MÉTODO 3 - Por indices

mensaje = 'Nombre {2} Edad {1}, Sueldo {0}'.format(sueldo, edad, nombre)
# print(mensaje)


# MÉTODO 4 - Por variables

mensaje = 'Nombre {n} Edad {e} Sueldo {s:.2f}'.format(n=nombre, e=edad, s=sueldo)
# print(mensaje)


diccionario = {'nombre':'Ivan', 'edad':35, 'sueldo':8000.00}
mensaje = 'Nombre: {persona[nombre]}'.format(persona=diccionario)
# print(mensaje)

diccionario = {'nombre':'Ivan', 'edad':35, 'sueldo':8000.00}
mensaje = 'Nombre: {dic[nombre]}, Edad: {dic[edad]}, Sueldo: {dic[sueldo]:.2f}'.format(dic=diccionario)
# print(mensaje)

# MÉTODO 5 - Template Literal, F String.

mensaje = f'Nombre {nombre} Edad {edad} Sueldo {sueldo:.2f}' # Insertar la variable literal se le conoce como interpolación
print(mensaje)

# MÉTODO Print

print(nombre,edad,sueldo, sep=', ')


