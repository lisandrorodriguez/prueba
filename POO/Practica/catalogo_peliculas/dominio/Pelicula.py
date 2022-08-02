


class Pelicula:

    def __init__(self,nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,otronombre):
        self._nombre = otronombre
    
    def __str__(self):
        return f"Pelicula: {self._nombre}"
