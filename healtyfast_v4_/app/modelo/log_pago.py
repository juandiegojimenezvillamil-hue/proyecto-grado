class Pago:

    def __init__(self, id_pago, metodo, monto):

        self.__id_pago = id_pago
        self.__metodo = metodo
        self.__monto = monto
        self.__estado = "Pendiente"

    # GETTERS
    def get_id_pago(self):
        return self.__id_pago

    def get_metodo(self):
        return self.__metodo

    def get_monto(self):
        return self.__monto

    def get_estado(self):
        return self.__estado

    # SETTERS
    def set_id_pago(self, id_pago):
        self.__id_pago = id_pago

    def set_metodo(self, metodo):
        self.__metodo = metodo

    def set_monto(self, monto):
        self.__monto = monto
    def set_estado(self, estado):
        self.__estado = estado

    # MÉTODO
    def confirmar_pago(self):
        self.__estado = "Confirmado"

    # STR
    def __str__(self):
        return f"Pago: {self.__metodo} - {self.__estado}"