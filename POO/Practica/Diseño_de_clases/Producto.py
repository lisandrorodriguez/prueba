class Producto:

    contador_productos = 0

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio
    
    @property
    def id_producto(self):
        return self._id_producto
    
    @id_producto.setter
    def id_producto(self, id):
        self._id_producto = id
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, precio):
        self._precio = precio


    def __str__(self):
        return f"Id Producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}"


if __name__ == '__main__':
    producto1 = Producto("Camisa", "$1200")
    producto2 = Producto("Pantalón", "$1500")
    print(producto1)
    print(producto2)
    producto1.precio = "$500"
    print(producto1)
    