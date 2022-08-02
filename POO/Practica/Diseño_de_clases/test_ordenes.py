from Orden import Orden
from Producto import Producto

producto1 = Producto("Camisa", 1200)
producto2 = Producto("Pantalón", 1500)
producto3 = Producto("Medias", 120)
producto4 = Producto("Gorra", 700)

productos1 = [producto1, producto2]
productos2 = [producto3, producto4]
orden1 = Orden(productos1)
print(orden1)
print(f"El precio total es: {orden1.calcularTotal()}")
orden2 = Orden(productos2)
print(orden2)
orden1.agregarProducto(producto3)
orden1.agregarProducto(producto4)
print(orden1)