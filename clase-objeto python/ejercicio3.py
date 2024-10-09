# Defino la clase
class Carro:
    # Método constructor
    def __init__(self, marca, modelo, color, año_fabrica , tipo_carro):
        # Defino los atributos de instancia de la clase
        self.marca = marca
        self.modelo =  modelo
        self.color = color
        self.año_fabrica = año_fabrica
        self.tipo_carro = tipo_carro

    # Método para mostrar detalles de carro
    def mostrar_detalles(self):
        print("Información de su carro:")
        print("Marca: " + self.marca)
        print("Modelo: " + self.modelo)
        print("Color: " + self.color)
        print("Año de fabrica: " + self.año_fabrica)
        print("Tipo de carro: " + self.tipo_carro)
        print("-------------------------------------------------------")

#Metodo para saber si su carro abre sus "puertas"
    def puerta(self):
        #Defino el atributo privado "puerta solo para el metodo tipo_carro
        self.puerta = int(input("Indique si su carro puede abrir sus puertas use 1 para si o 0 para no: "))
        if self.puerta > 0:
            print("El carro es de tipo: " +self.tipo_carro+ " ")
            print(f"Su carro  {self.tipo_carro} tiene puertas que se pueden abrir")
            print("---------------------------------------------------")
        else:
            print("Su carro "+self.tipo_carro+" no es un tipo de carro que pueda abrir puertas")
            print("---------------------------------------------------")

# Creamos los objetos a partir de instanciar la clase de carro
carro1 = Carro("Ford", "Diecast", "Azul con blanco", "2005", "Carreras")
carro2 = Carro("Hyundai", "i10-GImt", "rojo", "2013", "Familiar")
carro3 = Carro("Toyota", "Prado 4.0 Tx-l Fl", "Blanco", "2022", "Todo terreno")

# Mostrar los detalles de cada objeto
carro1.mostrar_detalles()
carro1.puerta()
carro2.mostrar_detalles()
carro2.puerta()
carro3.mostrar_detalles()
carro3.puerta()