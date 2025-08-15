#IMPORTS
from MaterialBiblioteca import MaterialBiblioteca

#Herencia
class LibroFisico(MaterialBiblioteca):
    
    def __init__(self, titulo, autor, id, estado_prestamo, no_ejemplar):

        #Constructor de clase base
        super().__init__(titulo, autor, id, estado_prestamo)
        self.__no_ejemplar = no_ejemplar

    #Encapsulamos
    def getNoEjemplar(self):
        return self.__no_ejemplar
    
    def setNoEjemplar(self, no_ejemplar):
        self.__no_ejemplar = no_ejemplar

    #Polimorfismo
    def informacion(self):
      return f"\nTitulo del libro: {self.getTitulo()}, \nAutor: {self.getAutor()}, \nCódigo único: {self.getID()}, \nEstado del prestamo: {self.getEstadoPrestamo()}, \nNúmero de ejemplar: {self.getNoEjemplar()}."
    