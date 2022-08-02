import os

class CatalogoPeliculas:

    ruta_archivo = "peliculas.txt"
    # Es conveniente usar classmethod, ya que necesito acceder a una variable de clase.
    @classmethod
    def agregarPelicula(cls,objetoPelicula):

        try:
            with open(cls.ruta_archivo, 'a', encoding="utf8") as archivo:
                archivo.write(f"{objetoPelicula.nombre}\n")

        except Exception as e:
            return f"Error {e}, la película {objetoPelicula.nombre} no pudo ser agregada."


    @classmethod
    def listarPeliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding="utf8") as archivo:
            print("Catálogo de Películas".center(50,"-"))
            print(archivo.read()) # Se manda a imprimir todo el listado de peliculas
        
    @classmethod
    def eliminar(cls):
        os.remove(cls.ruta_archivo)
        print(f"Archivo eliminado: {cls.ruta_archivo}")
    


        


