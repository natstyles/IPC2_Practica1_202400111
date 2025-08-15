from abc import ABC, abstractmethod

#Abstract

#Common Atributes
class MaterialBiblioteca(ABC):
    def __init__(self, titulo, autor, id, estado_prestamo): #ID = codigo_unico
        
        #Encapsulados
        self.__titulo = titulo
        self.__autor = autor
        self.__id = id
        self.__estadoPrestamo = estado_prestamo

    #GETS Y SETS
    def getTitulo(self):
        return self.__titulo
    
    def setTitulo(self, titulo):
        self.titulo = titulo

    def getAutor(self):
        return self.__autor
    
    def setAutor(self, autor):
        self.__autor = autor

    def getID(self):
        return self.__id
    
    def setID(self, id):
        self.__id = id

    def getEstadoPrestamo(self):
        return self.__estadoPrestamo
    
    def setEstadoPrestamo(self, estado_prestamo):
        self.__estadoPrestamo = estado_prestamo

    #Abstracción
    @abstractmethod
    def información(self):
        pass