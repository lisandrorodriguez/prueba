from Empleado import Empleado
from Gerente import Gerente

# Polimorfismo, multiples formas en tiempo de ejecución

def imprimirDetalles(objeto):
    # print(objeto)
    print(type(objeto))
    print(objeto.mostrarDetalles())
    # isinstance -> sirve para preguntar si al objeto que estamos apuntando pertenece a cierta clase
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

empleado = Empleado("Juan", 5000)
imprimirDetalles(empleado)

gerente = Gerente("Karla", 9000, "Sistemas")
imprimirDetalles(gerente)