# Defino la clase
class Figuras:
    # Método constructor
    def __init__(self, lados, nombre, calcular_area, color , forma):
        # Defino los atributos de instancia de la clase
        self.lados = lados
        self.nombre =  nombre
        self.calcular_area = calcular_area
        self.color = color
        self.forma = forma

    # Método para mostrar detalles de figuras
    def mostrar_detalles(self):
        print("Información de el empleado:")
        print("Lados: " + self.lados)
        print("Nombre: " + self.nombre)
        print("Calcular el area: " + self.calcular_area)
        print("Color: " + self.color)
        print("Forma: " + self.forma)
        print("-------------------------------------------------------")

#Metodo para saber si la figura se puede "medir"
    def medir(self):
        #Defino el atributo privado "medir" solo para el metodo nombre
        self.medir = int(input("Indique cuantos lados tiene la figura: "))
        if self.medir > 0:
            print("La figura: " +self.nombre+ ":")
            print(f"Tiene un total de :  {self.medir} Por lo que se puede medir y calcular")
            print("---------------------------------------------------")
        else:
            print("La figura "+self.nombre+" no tiene lados que se puedan medir")
            print("---------------------------------------------------")

# Creamos los objetos a partir de instanciar la clase de figura
figura1 = Figuras("4 lados", "Rectangulo", "A = largo x ancho", "verde", "Rectangular")
figura2 = Figuras("3 lados", "Triangulo", "A = 0,5 (base x altura)", "Amarillo", "Triangular")
figura3 = Figuras("6 lados", "Hexagono", "A = (3√3S2)/2", "Rojo", "Hexagonal")

# Mostrar los detalles de cada objeto
figura1.mostrar_detalles()
figura1.medir()
figura2.mostrar_detalles()
figura2.medir()
figura3.mostrar_detalles()
figura3.medir()