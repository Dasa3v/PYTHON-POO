from abc import ABC, abstractmethod

class TareaEmpleado(ABC):
    @abstractmethod
    def realizar_tarea(self):
        pass

class Ingeniero(TareaEmpleado):
    def __init__(self, nombre, especialidad, sueldo):
        self.nombre = nombre
        self.especialidad = especialidad
        self.sueldo = sueldo

    def realizar_tarea(self):
        # Implementación específica para la tarea del Ingeniero
        return f"Ingeniero {self.nombre} está trabajando en un proyecto de {self.especialidad}."

class Doctor(TareaEmpleado):
    def __init__(self, nombre, especialidad, sueldo):
        self.nombre = nombre
        self.especialidad = especialidad
        self.sueldo = sueldo

    def realizar_tarea(self):
        # Implementación específica para la tarea del Doctor
        return f"Doctor {self.nombre} está tratando a pacientes en el área de {self.especialidad}."

# Uso de las clases
ingeniero = Ingeniero("Carlos", "Ingeniería Civil", 3200000)
print(f"Tarea: {ingeniero.realizar_tarea()}")

doctor = Doctor("María", "Cirugia", 4550000)
print(f"Tarea: {doctor.realizar_tarea()}")
