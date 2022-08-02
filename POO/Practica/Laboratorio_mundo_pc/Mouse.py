from DispositivoEntrada import DispositivoEntrada 

class Mouse(DispositivoEntrada):

    contador_ratones = 0

    def __init__(self, tipoentrada, marca):
        super().__init__(tipoentrada,marca)
        Mouse.contador_ratones +=1
        self.id_raton = Mouse.contador_ratones

    def __str__(self):
        return f"Mouse | {DispositivoEntrada.__str__(self)} | Id: {self.id_raton}"

if __name__ == '__main__':
    raton = Mouse("USB", "HP")
    print(raton)
    raton2 = Mouse("Inalambrica", "Razer")
    print(raton2)

