#IMPORTS
from MaterialBiblioteca import MaterialBiblioteca

#Herencia
class libroFisico(MaterialBiblioteca):
    def __init__(self, titulo, autor, id, estado_prestamo, tamaño_archivo):

        #Constructor de clase base
        super().__init__(titulo, autor, id, estado_prestamo)
        self.__tamaño_archivo = tamaño_archivo

    #Encapsulamos
    def getTamañoArchivo(self):
        return self.__tamaño_archivo
    
    def setTamañoArchivo(self, tamaño_archivo):
        self.__tamaño_archivo = tamaño_archivo

    #Polimorfismo
    def informacion(self):
      return f"Titulo del libro: {self.getTitulo()}, \nAutor: {self.getAutor()}, \nCódigo único: {self.getID()}, \nEstado del prestamo: {self.getEstadoPrestamo()}, \nTamaño de Archivo: {self.getTamañoArchivo()}."