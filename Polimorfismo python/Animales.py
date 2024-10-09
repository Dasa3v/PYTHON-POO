# Clase Animales
class Perro:
    def __init__(self, raza, tamaño, sonido, color):
        self.raza = raza
        self.tamaño = tamaño
        self.sonido = sonido
        self.color = color

    def descripcion(self):
        print("Soy un Perro")
        print(f"De raza: {self.raza}")
        print(f"Tamaño: {self.tamaño}")
        print(f"El sonido que hago es: {self.sonido}")
        print(f"De Color: {self.color}")
        print("----------------------------------------------------------------------")

# Clase Gato
class Gato:
    def __init__(self, raza,sonido, color):
        self.raza = raza
        self.sonido = sonido
        self.color = color

    def descripcion(self):
        print("Soy un Gato")
        print(f"De raza: {self.raza}")
        print(f"El sonido que hago es: {self.sonido}")
        print(f"De color: {self.color}")
        print("----------------------------------------------------------------------")

# Clase Pajaro
class Pajaro:
    def __init__(self, raza,voladora,color, sonido):
        self.raza = raza
        self.voladora = voladora
        self.color = color
        self.sonido = sonido

    def descripcion(self):
        print("Soy un Pajaro")
        print(f"De raza: {self.raza}")
        print(f"Puedo volar?: {self.voladora}")
        print(f"De color: {self.color}")   
        print(f"El sonido que hago es: {self.sonido}") 
        print("----------------------------------------------------------------------")
# Función que muestra la descripción de cualquier tipo de vehículo
def mostrar_descripcion(animal):
    animal.descripcion()

# Instancias de cada clase
perro = Perro("Labrador", "grande", "guau guau","cafe" )
gato = Gato("Siames", "miau miau","blanco" )
pajaro = Pajaro("pollito","No","amarillo","pio pio")

# Llamado al método descripcion para cada vehículo
mostrar_descripcion(perro)
mostrar_descripcion(gato)
mostrar_descripcion(pajaro)
