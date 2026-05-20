from modelo.log_emp import Persona

class Empleado(Persona):

    def __init__(self, id_persona, nombre, apellido,
                 email, telefono, direccion,
                 puesto, salario):

        super().__init__(id_persona, nombre, apellido,
                         email, telefono, direccion)

        self.__puesto = puesto
        self.__salario = salario

    # GETTERS
    def get_puesto(self):
        return self.__puesto

    def get_salario(self):
        return self.__salario

    # SETTERS
    def set_puesto(self, puesto):
        self.__puesto = puesto

    def set_salario(self, salario):
        self.__salario = salario

    # MÉTODO
    def calcular_salario(self):
        return self.__salario

    # STR
    def __str__(self):
        return f"Empleado: {self.get_nombre()} - {self.__puesto}"


