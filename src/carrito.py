class Carrito:
    def __init__(self):
        self._items = {}

    def agregar(self, nombre, precio, cantidad=1):
        self._items[nombre] = {"precio": precio, "cantidad": cantidad}

    def subtotal(self):
        return sum(i["precio"] * i["cantidad"] for i in self._items.values())
