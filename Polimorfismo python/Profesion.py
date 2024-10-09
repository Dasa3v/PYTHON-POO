# Clase Médico
class Medico:
    def __init__(self, nombre, especialidad, experiencia):
        self.nombre = nombre
        self.especialidad = especialidad
        self.experiencia = experiencia

    def trabajar(self):
        horas_trabajo = input("¿Cuantas horas de trabajo tiene?")
        print("Soy un Médico")
        print(f"Nombre: {self.nombre}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Años de experiencia: {self.experiencia}")
        print(f"Horas de trabajo son: {horas_trabajo}")
        print("----------------------------------------------------------------------")

# Clase Ingeniero
class Ingeniero:
    def __init__(self, nombre, especialidad, proyectos):
        self.nombre = nombre
        self.especialidad = especialidad
        self.proyectos = proyectos

    def trabajar(self):
        horas_trabajo = input("¿Cuantas horas de trabajo tiene?")
        print("Soy un Ingeniero")
        print(f"Nombre: {self.nombre}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Número de proyectos: {self.proyectos}")
        print(f"Horas de trabajo son: {horas_trabajo}")
        print("----------------------------------------------------------------------")

# Clase Docente
class Docente:
    def __init__(self, nombre, materia, años_experiencia):
        self.nombre = nombre
        self.materia = materia
        self.años_experiencia = años_experiencia

    def trabajar(self):
        horas_trabajo = input("¿Cuantas horas de trabajo tiene?")
        print("Soy un Docente")
        print(f"Nombre: {self.nombre}")
        print(f"Materia: {self.materia}")
        print(f"Años de experiencia: {self.años_experiencia}")
        print(f"Horas de trabajo son: {horas_trabajo}")
        print("----------------------------------------------------------------------")

# Función que permite trabajar cualquier tipo de profesional
def trabajar_profesional(profesional):
    profesional.trabajar()

# Instancias de cada clase
medico = Medico("Dr. Juan Pérez", "Cardiología", 10)
ingeniero = Ingeniero("Ing. María López", "Civil", 5)
docente = Docente("Profe Carlos Rodríguez", "Matemáticas", 8)

# Llamado al método trabajar para cada profesional
trabajar_profesional(medico)
trabajar_profesional(ingeniero)
trabajar_profesional(docente)
