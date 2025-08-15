#IMPORTS
from LibroDigital import LibroDigital
from LibroFisico import LibroFisico
import uuid

#PLIMORFISMO
def showInfo(MaterialBiblioteca):
    print(MaterialBiblioteca.informacion())

#MÉTODO PARA CREAR IDS UNICOS
def uuid_length(longitud):
    return uuid.uuid4().hex[:longitud]

#Interfaz inicial
if __name__ == "__main__":
    
    digital = None
    fisico = None

    #MÉTODO PARA REGISTRAR LIBROS
    def registrarLibro():
            print('\n------------Registrar un Libro--------------')
            print('|1. Registrar libro físico                 |')
            print('|2. Registrar libro digital                |')
            print('|3. Salir                                  |')
            print('--------------------------------------------')

            opcion2 = int(input("\nSelecciona una opción: "))

            #REGISTRANDO LIBRO FISICO
            if opcion2 == 1:
                titulo = input("Titulo: ")
                autor = input("Autor: ")
                no_ejemplar = input("Número de ejemplar: ")
                id = uuid_length(8)
                estado_prestamo = False
                fisico = LibroFisico(titulo, autor, id, estado_prestamo, no_ejemplar)
                guardar_libroFisico(fisico)
                print("\nLibro registrado exitosamente con el ID:", id)
                print(libreriaFisica)


            elif opcion2 == 2:
                titulo = input("Titulo: ")
                autor = input("Autor: ")
                tamaño_archivo = input("Tamaño de archivo: ")
                id = uuid_length(8)
                estado_prestamo = False
                digital = LibroDigital(titulo, autor, id, estado_prestamo, tamaño_archivo)
                guardar_libroDigital(digital)
                print("\nLibro registrado exitosamente con el ID:", id)
                print(libreriaDigital)


            elif opcion2 == 3:
                print("\nRegresando al menú principal...")
                return
            
            else:
                print("\nSelecciona una opción válida")

    #MÉTODO PARA GUARDAR LIBROS EN BIBLIOTECA
    libreriaFisica = {}
    def guardar_libroFisico(fisico):
        
        idLibro = fisico.getID()

        libreriaFisica[idLibro] = {
            "Titulo": fisico.getTitulo(),
            "Autor": fisico.getAutor(),
            "Estado de prestamo": fisico.getEstadoPrestamo(),
            "Número de ejemplar": fisico.getNoEjemplar()
        }

    libreriaDigital = {}
    def guardar_libroDigital(digital):

        idLibro = digital.getID()

        libreriaDigital[idLibro] = {
            "Titulo": digital.getTitulo(),
            "Autor": digital.getAutor(),
            "Estado de prestamo": digital.getEstadoPrestamo(),
            "Número de ejemplar": digital.getTamañoArchivo()
        }




    while True: 
        print('\n---------------Menu Biblioteca---------------')
        print('|1. Registrar nuevo material               |')
        print('|2. Gestionar Préstamo                     |')
        print('|3. Salir                                  |')
        print('--------------------------------------------')

        opcion = int(input("\nSelecciona una opción: "))

        if opcion == 1:
            registrarLibro()
        elif opcion == 2:
            #gestionLibro()
            print("gestion libro")
        elif opcion == 3:
            print("\nSaliendo del programa...")
            break
        else:
            print("\nSelecciona una opción válida")

    