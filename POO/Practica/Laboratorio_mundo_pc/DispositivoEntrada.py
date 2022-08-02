class DispositivoEntrada():

    def __init__(self, tipoentrada, marca):
        self._tipoentrada = tipoentrada
        self._marca = marca
    
    def __str__(self):
        return f"Tipo de entrada: {self._tipoentrada} | Marca: {self._marca}"

    @property
    def tipoentrada(self):
        return self._tipoentrada
    
    @tipoentrada.setter
    def tipoentrada(self, otraentrada):
        self._tipoentrada = otraentrada
    
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, otramarca):
        self._marca= otramarca


    

