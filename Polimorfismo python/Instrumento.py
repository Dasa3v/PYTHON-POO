# Clase Guitarra
class Guitarra:
    def __init__(self, marca, modelo, tipo_sonido):
        self.marca = marca
        self.modelo = modelo
        self.tipo_sonido = tipo_sonido

    def tocar(self):
        puede_tocar = input("¿Puedes tocar la guitarra? (sí/no): ")
        print("Soy una Guitarra")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Tipo de sonido: {self.tipo_sonido}")
        print(f"¿Puedes tocarla?: {puede_tocar}")
        print("----------------------------------------------------------------------")

# Clase Piano
class Piano:
    def __init__(self, marca, modelo, tipo_sonido):
        self.marca = marca
        self.modelo = modelo
        self.tipo_sonido = tipo_sonido

    def tocar(self):
        puede_tocar = input("¿Puedes tocar el piano? (sí/no): ")
        print("Soy un Piano")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Tipo de sonido: {self.tipo_sonido}")
        print(f"¿Puedes tocarlo?: {puede_tocar}")
        print("----------------------------------------------------------------------")

# Clase Trompeta
class Trompeta:
    def __init__(self, marca, modelo, tipo_sonido):
        self.marca = marca
        self.modelo = modelo
        self.tipo_sonido = tipo_sonido

    def tocar(self):
        puede_tocar = input("¿Puedes tocar la trompeta? (sí/no): ")
        print("Soy una Trompeta")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Tipo de sonido: {self.tipo_sonido}")
        print(f"¿Puedes tocarla?: {puede_tocar}")
        print("----------------------------------------------------------------------")

# Función que permite tocar cualquier tipo de instrumento
def tocar_instrumento(instrumento):
    instrumento.tocar()

# Instancias de cada clase
guitarra = Guitarra("Fender", "Stratocaster", "Cuerda")
piano = Piano("Yamaha", "U1", "Teclas")
trompeta = Trompeta("Bach", "Stradivarius", "Viento")

# Llamado al método tocar para cada instrumento
tocar_instrumento(guitarra)
tocar_instrumento(piano)
tocar_instrumento(trompeta)
