class Producto:

    def __init__(self, id_producto, nombre,
                 descripcion, precio, stock):

        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio
        self.__stock = stock

    # GETTERS
    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.__stock

    # SETTERS
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_precio(self, precio):
        self.__precio = precio

    def set_stock(self, stock):
        self.__stock = stock

    # MÉTODO
    def hay_stock(self, cantidad):
        return self.__stock >= cantidad

    # STR
    def __str__(self):
        return f"{self.__nombre} - ${self.__precio}"