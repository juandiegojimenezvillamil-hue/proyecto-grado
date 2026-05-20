from modelo.log_per import Persona

class Cliente(Persona):

    def __init__(self, id_persona, nombre, apellido,
                 email, telefono, direccion):

        super().__init__(id_persona, nombre, apellido,
                         email, telefono, direccion)

        self.__historial = []

    # GETTERS
    def get_historial(self):
        return self.__historial

    # SETTERS
    def set_historial(self, historial):
        self.__historial = historial

    # MÉTODO
    def agregar_factura(self, factura):
        self.__historial.append(factura)

    # STR
    def __str__(self):
        return f"Cliente: {self.get_nombre()}"
