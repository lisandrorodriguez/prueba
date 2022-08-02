from DispositivoEntrada import DispositivoEntrada 

class Teclado(DispositivoEntrada):

    contador_teclados = 0

    def __init__(self, tipoentrada, marca):
        super().__init__(tipoentrada,marca)
        Teclado.contador_teclados +=1
        self.id_teclado = Teclado.contador_teclados

    def __str__(self):
        return f"Teclado | {DispositivoEntrada.__str__(self)} | Id: {self.id_teclado}"

