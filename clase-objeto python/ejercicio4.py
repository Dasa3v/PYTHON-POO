# Defino la clase
class Empleado:
    # Método constructor
    def __init__(self, nombre, edad, cargo, experiencia , sueldo):
        # Defino los atributos de instancia de la clase
        self.nombre = nombre
        self.edad =  edad
        self.cargo = cargo
        self.experiencia = experiencia
        self.sueldo = sueldo

    # Método para mostrar detalles de empleado
    def mostrar_detalles(self):
        print("Información de el empleado:")
        print("Nombre: " + self.nombre)
        print("Edad: " + self.edad)
        print("Cargo: " + self.cargo)
        print("Experiencia: " + self.experiencia)
        print("Sueldo: " + self.sueldo)
        print("-------------------------------------------------------")

#Metodo para saber si el empleado declara "impuesto"
    def impuesto(self):
        #Defino el atributo privado "impuesto" solo para el metodo nombre
        self.impuesto = int(input("Indique si su empleado declara impuestos con su sueldo ganado: "))
        if self.impuesto > 1500000:
            print("El empleado: " +self.nombre+ ".")
            print(f"El Empleado:  {self.nombre} Declara impuestos con cada sueldo que gana")
            print("---------------------------------------------------")
        else:
            print("El empleado "+self.nombre+" no declara impuestos por su bajo sueldo")
            print("---------------------------------------------------")

# Creamos los objetos a partir de instanciar la clase de empleado
empleado1 = Empleado("Luis fernando", "38", "Constructor", "10 años", "1100000 de pesos")
empleado2 = Empleado("Maria mercado", "28", "Policia", "5 años", "3000000 de pesos")
empleado3 = Empleado("Jorge suarez", "30", "Abogado", "2 años", "5000000 de pesos")

# Mostrar los detalles de cada objeto
empleado1.mostrar_detalles()
empleado1.impuesto()
empleado2.mostrar_detalles()
empleado2.impuesto()
empleado3.mostrar_detalles()
empleado3.impuesto()