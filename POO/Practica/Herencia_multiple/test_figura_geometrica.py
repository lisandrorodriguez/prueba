from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from FiguraGeometrica import FiguraGeometrica



if __name__ == '__main__':
    print("Creacion objeto cuadrado".center(50,"-"))
    cuadrado1 = Cuadrado(5, "rojo")
    print(cuadrado1)
    print("Creacion objeto rectangulo".center(50,"-"))
    obj1=Rectangulo(20,3,"Rojo")
    #print(Rectangulo.mro())
    print(obj1)
    # No se puede instanciar una clase abstracta
    # figura = FiguraGeometrica(9,5)
    print(Cuadrado.mro()) # Se modifica la orden de resolución por la clase abstracta de Figura Geometrica

    
    

#MRO - Method Resolution Order
# Orden en los cuales se ejecutan los metodos
# print(Cuadrado.mro())