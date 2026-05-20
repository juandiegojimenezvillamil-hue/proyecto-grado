class Categoria:

    def __init__(self, id_categoria, nombre):

        self.__id_categoria = id_categoria
        self.__nombre = nombre
        self.__productos = []

    # GETTERS
    def get_id_categoria(self):
        return self.__id_categoria
    def get_nombre(self):
        return self.__nombre

    def get_productos(self):
        return self.__productos

    # SETTERS
    def set_id_categoria(self,id_categoria):
        self.__id_categoria=id_categoria
    def set_nombre(self, nombre):
        self.__nombre = nombre

    # MÉTODO
    def agregar_producto(self, producto):
        self.__productos.append(producto)

    # STR
    def __str__(self):
        return f"Categoría: {self.__nombre}"