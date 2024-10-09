#Clase Personas con atributos encapsulados o privados
class Producto:
    #metodo constructor
    def __init__(self, nombre, precio,cantidad,categoria):
        self.__nombre = nombre #privado
        self.__precio = precio #privado
        self.cantidad = cantidad #publico
        self.categoria = categoria #público

    #metodo getter
    def obtener_nombre(self):
        return self.__nombre

    #metodo getter
    def obtener_precio(self):
        return self.__precio

    #metodo setter
    def establecer_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    #metodo setter
    def establecer_precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    #metodo mostrar detalles del objeto
    def mostrar_detalles(self):
        print(f"\nNombre del producto: {self.__nombre}")
        print(f"Precio del producto: {self.__precio}")
        print(f"Cantidad en almacen: {self.cantidad}")
        print(f"Categoria del producto: {self.categoria}")

#objeto
Jabon = Producto("Avon", 1500, 200, "Humectante")

#imprimir atributos publicos y privados
Jabon.mostrar_detalles()

print("--------------------------")

#imprimir el atributo encapsulado modificando su acceso con getter y setter
Jabon.establecer_nombre("Milagro") #setter
print(f"Nombre del producto: {Jabon.obtener_nombre()}") #getter
Jabon.establecer_precio("3250") #setter
print(f"Precio del producto: {Jabon.obtener_precio()}") #getter
print(f"Cantidad en almacen: {Jabon.cantidad}") #publico
print(f"Categoria del producto: {Jabon.categoria}") #público

