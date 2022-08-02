from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas
import os


def consultarIngreso():
    return str(input("Desea usar el menú? Y/N: ".lower()))
    

def Menu():
    print("Agregar peliculas al catálogo".center(50,"-"))
    print("1. Agregar película")
    print("2. Listar peliculas")
    print("3. Eliminar archivo de películas")

def accionarMenu(valor):

    if valor == 1:
        nombre = str(input("Ingrese el nombre de la pelicula: "))
        pel1 = Pelicula(nombre)
        CatalogoPeliculas.agregarPelicula(pel1)

    elif valor == 2:
        CatalogoPeliculas.listarPeliculas()

    elif valor == 3:
        print("Eliminando archivo de peliculas...".center(50,"-"))
        CatalogoPeliculas.eliminar()
    
    else:
        print("Valor invalido.")

        

def main():
    ingreso = consultarIngreso()
    while ingreso == 'y':
        accion = input("Que acción desea realizar?: ")
        accionarMenu(accion)
        ingreso = str(input("Desea realizar otra acción? Y/N: ".lower()))
    else:
        print("Saliendo del programa...")


if __name__ == '__main__': 
    Menu()
    main()




