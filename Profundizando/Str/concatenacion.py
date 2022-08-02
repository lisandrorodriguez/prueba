# Profundizando en el tipo str


# Concatenacion automatica en python
# No es necesario el simbolo de mas para concatenar dos cadenas


mensaje = 'Hola' + 'Mundo'
print(mensaje)

mensaje = 'Hola' 'Mundo'
print(mensaje)

# Pero si queremos aplicar este segundo metodo si es necesario aplicar el signo +
variable = 'Hola'
mensaje = 'Hola' 'Mundo'
print(mensaje)

variable = 'Hola'
mensaje = 'Hola' 'Mundo' + variable
print(mensaje)

# Concatenar mas elementos

mensaje += 'Universidad' 'Python'

print(mensaje)

