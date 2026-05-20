from modelo.log_cli import Cliente
from modelo.log_cate import Categoria
from modelo.log_produc import Producto
from modelo.log_fac import Factura

# =========================
# CLIENTE
# =========================

cliente1 = Cliente(
    "1",
    "Juan",
    "Pérez",
    "juan@gmail.com",
    "300123456",
    "Bogotá"
)

# =========================
# CATEGORÍA
# =========================

categoria1 = Categoria(
    "1",
    "Tecnología"
)

# =========================
# PRODUCTOS
# =========================

producto1 = Producto(
    "1",
    "Laptop",
    "Laptop Gamer",
    3500,
    10
)

producto2 = Producto(
    "2",
    "Mouse",
    "Mouse RGB",
    150,
    20
)

categoria1.agregar_producto(producto1)
categoria1.agregar_producto(producto2)

# =========================
# FACTURA
# =========================

factura1 = Factura(
    "1001",
    cliente1
)

factura1.agregar_producto(producto1, 1)
factura1.agregar_producto(producto2, 2)

# =========================
# COMPOSICIÓN
# FACTURA CREA PAGO Y ENVÍO
# =========================

factura1.crear_pago(
    "1",
    "Tarjeta"
)

factura1.crear_envio(
    "1",
    "Servientrega",
    "GUIA123"
)

# =========================
# RESULTADOS
# =========================

print(factura1)

print("TOTAL:",
factura1.calcular_total())

print(factura1.get_pago())

print(factura1.get_envio())