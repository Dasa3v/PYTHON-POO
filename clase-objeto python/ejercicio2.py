# Defino la clase
class Perro:
    # Método constructor
    def __init__(self, raza, tamaño, color, pelaje , esperanza_de_vida):
        # Defino los atributos de instancia de la clase
        self.raza = raza
        self.tamaño = tamaño
        self.color = color
        self.pelaje = pelaje
        self.esperanza_de_vida = esperanza_de_vida

    # Método para mostrar detalles de perro
    def mostrar_detalles(self):
        print("Información de su perro:")
        print("Raza: " + self.raza)
        print("Tamaño: " + self.tamaño)
        print("Color: " + self.color)
        print("Pelaje: " + self.pelaje)
        print("Esperanza de vida: " + self.esperanza_de_vida)
        print("-------------------------------------------------------")

#Metodo para saber si su perro es feliz
    def feliz(self):
        #Defino el atributo privado "feliz" solo para el metodo raza
        self.feliz = int(input("Indique si su perro esta moviendo la cola con usted con un 1 para si o 0 para no: "))
        if self.feliz > 0:
            print("El perro " +self.raza+ " Esta feliz")
            print(f"Usted cuida bien de su  {self.feliz} y lo hace feliz")
            print("---------------------------------------------------")
        else:
            print("El perro "+self.raza+" no se encuentra feliz, por favor dele atencion")
            print("---------------------------------------------------")

# Creamos los objetos a partir de instanciar la clase de perro
perro1 = Perro("Golden retriever", "Dorado", "Mediano", "Ambundante", "10 a 12 años")
perro2 = Perro("Husky siberiano", "Negro con gris y blanco", "mediano", "Normal", "12 a 15 años")
perro3 = Perro("Pitcher", "Oscuro, marron o gris", "pequeño", "poco", "12 a 16 años")

# Mostrar los detalles de cada objeto
perro1.mostrar_detalles()
perro1.feliz()
perro2.mostrar_detalles()
perro2.feliz()
perro3.mostrar_detalles()
perro3.feliz()