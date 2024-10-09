# Clase Carro
class Carro:
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def descripcion(self):
        print("Soy un Carro")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print("----------------------------------------------------------------------")

# Clase Moto
class Moto:
    def __init__(self, marca, modelo, año, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.cilindrada = cilindrada

    def descripcion(self):
        print("Soy una Moto")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Cilindrada: {self.cilindrada} cc")
        print("----------------------------------------------------------------------")

# Clase Bicicleta
class Bicicleta:
    def __init__(self, marca, tipo, num_velocidades):
        self.marca = marca
        self.tipo = tipo
        self.num_velocidades = num_velocidades

    def descripcion(self):
        print("Soy una Bicicleta")
        print(f"Marca: {self.marca}")
        print(f"Tipo: {self.tipo}")
        print(f"Velocidades: {self.num_velocidades}")
        print("----------------------------------------------------------------------")
# Función que muestra la descripción de cualquier tipo de vehículo
def mostrar_descripcion(vehiculo):
    vehiculo.descripcion()

# Instancias de cada clase
carro = Carro("Toyota", "Corolla", 2022, "Rojo")
moto = Moto("Yamaha", "MT-03", 2021, 321)
bicicleta = Bicicleta("Giant", "Montaña", 21)

# Llamado al método descripcion para cada vehículo
mostrar_descripcion(carro)
mostrar_descripcion(moto)
mostrar_descripcion(bicicleta)
