# Defino la clase
class Celular:
    # Método constructor
    def __init__(self, nombre, marca, modelo, color, procesador):
        # Defino los atributos de instancia de la clase
        self.nombre = nombre
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.procesador = procesador

    # Método para mostrar detalles del celular
    def mostrar_detalles(self):
        print("Información del celular:")
        print("Nombre: " + self.nombre)
        print("Marca: " + self.marca)
        print("Modelo: " + self.modelo)
        print("Color: " + self.color)
        print("Procesador: " + self.procesador)
        print("---------------------------------------------------")

#Metodo para encender un celular
    def encender(self):
    #Defino el atributo privado "energia" solo para el metodo encender
        self.energia = int(input("digite el valor de la carga: "))
        if self.energia >0:
            print("El celular " +self.modelo+ " Se puede encender")
            print(f"|||||||||||||||||||| {self.energia} %  de carga")
            print("---------------------------------------------------")
        else:
            print("El celular "+self.modelo+" no se puede encender")
            print("---------------------------------------------------")

# Creamos los objetos a partir de instanciar la clase de celular
objeto1 = Celular("infinix", "smart", "smart8", "negro", "octa-core")
objeto2 = Celular("redmi", "xiaomi", "redmi 13", "blanco", "Mediatek Helio G91 ultra")
objeto3 = Celular("Galaxy", "samsung", "A25", "gris", "Exynos 1280")

# Mostrar los detalles de cada objeto
objeto1.mostrar_detalles()
objeto1.encender()
objeto2.mostrar_detalles()
objeto3.mostrar_detalles()


