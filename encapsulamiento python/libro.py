#Clase Personas con atributos encapsulados o privados
class libros:
    #metodo constructor
    def __init__(self, titulo, autor,isbn,editorial):
        self.__titulo = titulo #privado
        self.__autor = autor #privado
        self.__isbn = isbn #privado
        self.editorial = editorial #público
        

    #metodo getter
    def obtener_titulo(self):
        return self.__titulo

    #metodo getter
    def obtener_autor(self):
        return self.__autor

    #metodo getter
    def obtener_isbn(self):
        return self.__isbn

    #metodo setter
    def establecer_titulo(self, buscar_titulo):
        self.__titulo = buscar_titulo

    #metodo setter
    def establecer_autor(self, buscar_autor):
        self.__autor= buscar_autor

    #metodo mostrar detalles del objeto
    def mostrar_detalles(self):
        print(f"\nTitulo: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"ISBN: {self.__isbn}")
        print(f"Editorial: {self.editorial}")

#objeto
libro = libros("El señor", "Mario marco", 1458867806, "Libertad", )

#imprimir atributos publicos y privados
libro.mostrar_detalles()

print("--------------------------")

#imprimir el atributo encapsulado modificando su acceso con getter y setter
libro.establecer_titulo("La sombra") #setter
print(f"Titulo: {libro.obtener_titulo()}") #getter
libro.establecer_autor("Kendamar Luz") #setter
print(f"Autor: {libro.obtener_autor()}") #getter
print(f"ISBN: {libro.obtener_isbn()}") #getter
print(f"Editorial: {libro.editorial}") #público

