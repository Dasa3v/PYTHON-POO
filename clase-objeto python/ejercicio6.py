# Defino la clase
class Motos:
    # Método constructor
    def __init__(self, marca, modelo, año_fabrica, tipo , cilindraje):
        # Defino los atributos de instancia de la clase
        self.marca = marca
        self.modelo =  modelo
        self.año_fabrica = año_fabrica
        self.tipo = tipo
        self.cilindraje = cilindraje

    # Método para mostrar detalles de motos
    def mostrar_detalles(self):
        print("Información de el empleado:")
        print("Marca: " + self.marca)
        print("Modelo: " + self.modelo)
        print("Año de fabrica: " + self.año_fabrica)
        print("Tipo: " + self.tipo)
        print("Cilindraje: " + self.cilindraje)
        print("-------------------------------------------------------")

#Metodo para saber si la figura se puede "combustible"
    def combustible(self):
        #Defino el atributo privado "combustible" solo para el metodo tipo
        self.combustible = int(input("Indique que tipo de  gasolina una su moto, 0: electrica, 1: Normal, 2: Diesel: "))
        if self.combustible > 0:
            print("Su moto tipo: " +self.tipo+ "quema combustible")
            print(f"Su moto:  {self.nombre} requiere tanquearse cada cierto tiempo o distancia recorrida")
            print("---------------------------------------------------")
        else:
            print("Su moto "+self.nombre+" requiere recargarse en una instalacion electrica cada cierto tiempo o distancia")
            print("---------------------------------------------------")

# Creamos los objetos a partir de instanciar la clase de motos
moto1 = Motos("Honda", "Invicta 150", "2017", "deportiva", "150 Cc")
moto2 = Motos("Victory", "life 125", "2023", "scooter", "125Cc")
moto3 = Motos("Yamaha", "Xtz 250", "2014", "Enduro", "250 Cc")

# Mostrar los detalles de cada objeto
moto1.mostrar_detalles()
moto1.combustible()
moto2.mostrar_detalles()
moto2.combustible()
moto3.mostrar_detalles()
moto3.combustible()