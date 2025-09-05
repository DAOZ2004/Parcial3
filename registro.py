class RegistroVentas:
    def __init__(self):
        self.ventas = {}  # {producto: {"cantidad": x, "precio": y, "ingreso": z}}

    def agregar_venta(self, producto, cantidad, precio):
        if producto in self.ventas:
            self.ventas[producto]["cantidad"] += cantidad
            self.ventas[producto]["ingreso"] += cantidad * precio
        else:
            self.ventas[producto] = {
                "cantidad": cantidad,
                "precio": precio,
                "ingreso": cantidad * precio
            }