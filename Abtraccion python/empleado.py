# Crea una clase abstracta Empleado con un método abstracto calcular_salario(). Luego, crea dos clases concretas 
# EmpleadoTiempoCompleto y EmpleadoPorHoras que implementen calcular_salario() de manera distinta.

from abc import ABC, abstractmethod

class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass 

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, horas_de_trabajo, salario_hora):
        self.nombre = nombre
        self.horas_de_trabajo = horas_de_trabajo
        self.salario_hora = salario_hora

    def calcular_salario(self):
        # El salario de un empleado a tiempo completo es el producto de las horas trabajadas por el salario por hora
        return self.horas_de_trabajo * self.salario_hora

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, horas_de_trabajo, salario_hora):
        self.nombre = nombre
        self.horas_de_trabajo = horas_de_trabajo
        self.salario_hora = salario_hora

    def calcular_salario(self):
        # El salario por horas se calcula multiplicando las horas trabajadas por el salario por hora
        return self.horas_de_trabajo * self.salario_hora

# Uso de las clases
empleado_tc = EmpleadoTiempoCompleto("Juan", 40, 50)  # 40 horas a la semana, $20 por hora
print(f"Salario de {empleado_tc.nombre}: {empleado_tc.calcular_salario()}")

empleado_ph = EmpleadoPorHoras("Ana", 20, 25)  # 20 horas a la semana, $15 por hora
print(f"Salario de {empleado_ph.nombre}: {empleado_ph.calcular_salario()}")
