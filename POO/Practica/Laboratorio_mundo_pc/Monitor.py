from DispositivoEntrada import DispositivoEntrada

class Monitor:

    contador_monitores = 0

    def __init__(self, marca, tamaño):

        Monitor.contador_monitores += 1
        self._id_monitor = Monitor.contador_monitores
        self._marca = str(marca)
        self._tamaño = tamaño

    def __str__(self):
        return f" Id Monitor: {self._id_monitor} | Marca: {self._marca} | Tamaño: {self._tamaño}"
    
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, otramarca):
        self._marca = otramarca
    
    @property
    def tamaño(self):
        return self._tamaño
    
    @tamaño.setter
    def tamaño(self, otrotamaño):
        self._tamaño = otrotamaño

    @property
    def id_monitor(self):
        return self._id_monitor
    
    @id_monitor.setter
    def id_monitor(self, otromonitor):
        self._id_monitor = otromonitor





    
