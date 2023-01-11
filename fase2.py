class Cliente:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def registrar(self):
        #método con el que registraremos al cliente en el sistema
        pass

class Producto:
    def __init__(self, nombre, precio, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

class Pedido:
    def __init__(self, productos, cantidades, fecha_entrega, numero_pedido):
        self.productos = productos
        self.cantidades = cantidades
        self.fecha_entrega = fecha_entrega
        self.numero_pedido = numero_pedido
        self.costo_total = 0

    
    def imprimir_factura(self):
        # Lógica para imprimir la factura
        print("La factura se ha impreso en pdf.")