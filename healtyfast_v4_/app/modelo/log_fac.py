from modelo.log_pago import Pago
from modelo.log_envio import Envio

class Factura:

    def __init__(self, id_factura, cliente):

        self.__id_factura = id_factura
        self.__cliente = cliente
        self.__productos = []

        # COMPOSICIÓN
        self.__pago = None
        self.__envio = None

    # GETTERS
    def get_cliente(self):
        return self.__cliente

    def get_productos(self):
        return self.__productos

    def get_pago(self):
        return self.__pago

    def get_envio(self):
        return self.__envio

    # MÉTODOS

    def agregar_producto(self, producto, cantidad):

        subtotal = producto.get_precio() * cantidad

        self.__productos.append({
            "producto": producto.get_nombre(),
            "cantidad": cantidad,
            "subtotal": subtotal
        })

    # =========================
    # COMPOSICIÓN CON PAGO
    # =========================

    def crear_pago(self, id_pago, metodo):

        total = self.calcular_total()

        self.__pago = Pago(
            id_pago,
            metodo,
            total
        )

    # =========================
    # COMPOSICIÓN CON ENVÍO
    # =========================

    def crear_envio(self, id_envio,
                     transportadora, guia):

        self.__envio = Envio(
            id_envio,
            transportadora,
            guia
        )

    def calcular_total(self):

        total = 0

        for item in self.__productos:
            total += item["subtotal"]

        return total

    # STR
    def __str__(self):
        return f"Factura #{self.__id_factura}"