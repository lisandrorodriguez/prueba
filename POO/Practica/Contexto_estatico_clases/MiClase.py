# En Python todas las clases son objetos

class MiClase:
    # Se asocia con la clase en si misma
    variables_clase = 'Michael Jackson'

    def __init__(self, variable_instancia):
        # Se asocia a cada uno de los objetos
        self.variables_instancia = variable_instancia

    # Método estatico, se asocia al metodo de una clase en si, asi como las variables de clase
    # Para indicar que un método es estático hay que llamar al decorador
    # Un metodo estatico no pueden acceder a las variables de instancia
    # No lleva self
    # Los objetos se crean una vez que la clase esta cargada en memoria, no antes
    # --- El método estático no tiene una relación definida con la clase ---
    @staticmethod
    def metodoEstatico():
        # self.variables_instancia <-- NO PUEDE ACCEDER.
        # Si se puede acceder a las variables de clases, pero de forma indirecta
        print(MiClase.variables_clase)

    # Un método de clase si recibe un contexto de clase
    # El parámetro de cls significa class, es para indicar que es un método que referencia a la clase
    # No se utiliza "class" específicamente, ya que esa palabra reservada ya esta asociada -> Class
    @classmethod
    def metodoClase(cls):
        print(cls.variables_clase)

    # A través de un método de instancia, se pueden acceder a los métodos estáticos.
    def metodoInstancia(self):
        self.metodoClase()
        self.metodoEstatico()

if 1 < 0:  
    # Se accede a la variable de clase
    #print(MiClase.variables_clase)
    # Se accede a la variable de instancia
    # Desde el objeto también se puede acceder a la variable de clase
    objDeInstancia = MiClase(100)
    #print(objDeInstancia.variables_instancia)
    #print(objDeInstancia.variables_clase)
    # Al vuelo, fuera de la clase, también podemos crear variables y asignarles un valor
    # Se accedió de forma dinámica
    MiClase.variable_clase2 = "Valor variable clase 2"
    #MiClase.metodoEstatico()
    print(MiClase.metodoClase())

Obj1 = MiClase("Una instancia... ")
print(Obj1.metodoInstancia())





    