# ABC = Abstract Base Class 
# Clase para convertir clases en clases abstractas
from abc import ABC, abstractclassmethod, abstractmethod #abstractclassmethod es un decorador



class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        #Validación
        if self._validar_valor(ancho):
            self._ancho = ancho
        
        else:
            self._ancho = 0
            print("No paso la validación ",{ancho})

        if self._validar_valor(alto):
            self._alto = alto
        
        else:
            self._alto = 0
            print("No paso la validación", {alto})
    
    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f"Valor erróneo de ancho: {ancho}")
    
    @property
    def alto(self):
        return self._alto
    
    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f"Valor erróneo de alto: {alto}")

    @abstractmethod
    def calcularArea(self):
        pass

    def __str__(self):
        return f"Figura Geometrica [Ancho: {self.ancho} Alto: {self.alto}]"

    #Método Encapsulado solo para uso de la clase y no externo.
    def _validar_valor(self,valor):
        #Notación simplificada
        return True if 0 < valor < 10 else False

    # De una clase abstracta no se pueden instanciar objetos
    
