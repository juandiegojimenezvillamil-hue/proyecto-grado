class Envio:

    def __init__(self, id_envio, transportadora, guia):

        self.__id_envio = id_envio
        self.__transportadora = transportadora
        self.__guia = guia
        self.__estado = "En proceso"

    # GETTERS
    def get_transportadora(self):
        return self.__transportadora

    def get_estado(self):
        return self.__estado
    def get_guia(self):
        return self.__guia
    def get_id_envio(self):
        return self.__id_envio

    # SETTERS
    def set_guia(self, guia):
        self.__guia = guia
    def set_id_envio(self, id_envio):
        self.__id_envio = id_envio
    def set_estado(self, estado):
        self.__estado = estado

    def set_transportadora(self, transportadora):
        self.__transportadora = transportadora

    # MÉTODO
    def marcar_entregado(self):
        self.__estado = "Entregado"

    # STR
    def __str__(self):
        return f"Envío: {self.__transportadora} - {self.__estado}"