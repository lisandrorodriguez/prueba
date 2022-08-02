from Persona import Persona



if __name__ == '__main__':
    print('Creación de objetos'.center(30,'-'))
    persona1 = Persona("Ether", "Undesvik", 30)
    persona1.mostrarDetalle()

    print("Eliminación de objetos".center(30,'-'))
    del persona1
    #Por tener el método destructor en la clase, se muestra un detalle en pantalla.... q copado

print(__name__)

#Este archivo seria un modulo nuevo que se esta importando una clase del módulo principal