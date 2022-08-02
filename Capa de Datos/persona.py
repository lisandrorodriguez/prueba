from logger_base import log

class Persona:
    def __init__(self, id=None, nombre=None, apellido=None, email=None): #id esta en None ya que al guardarlo en una base de datos se autogenera el ID
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
    
    def __str__(self):
        return f"""
        Id persona: {self._id},
        Nombre: {self._nombre},
        Apellido: {self._apellido},
        Email: {self._email}

        """
    
    @property
    def id(self):
        return self._id

    @id.setter

    def id(self, otherId):
        self._id = otherId

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, otherName):
        self._nombre = otherName

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, otherApellido):
        self._apellido = otherApellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, otherEmail):
        self._email = otherEmail
 
    
if __name__ == '__main__':
    persona1 = Persona("1", "Marcos", "Pereyra", "mpereyra@mail.com")
    log.debug(persona1)
    # Simular un insert
    persona1 = Persona(nombre='Juan',apellido='Perez',email='jperez@mail.com')
    log.debug(persona1)