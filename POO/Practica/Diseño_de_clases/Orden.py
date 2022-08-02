from Producto import Producto

class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos) # Se hace la conversión para asegurarnos de que sea una lista

    def agregarProducto(self, producto):
        self._productos.append(producto)

    def calcularTotal(self):
        total = 0
        for producto in self._productos:
            total += producto._precio
        return total

    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += '| ' + producto.__str__()  #simbolo de pipe (paip)
        return f'Orden: {self._id_orden}, \nProductos: {productos_str}' # Alt + 92 slash invertido


if __name__ == '__main__':
    producto1 = Producto("Camisa", "$1200")
    producto2 = Producto("Pantalón", "$1500")
    productos = [producto1, producto2]
    orden1 = Orden(productos)
    print(orden1)