class Carrito:
    def __init__(self):
        self._items = {}

    def agregar(self, nombre, precio, cantidad=1):
        if precio <= 0 or cantidad <= 0:
            raise ValueError("Precio y cantidad deben ser positivos")
        if nombre in self._items:
            self._items[nombre]["cantidad"] += cantidad
        else:
            self._items[nombre] = {"precio": precio, "cantidad": cantidad}

    def subtotal(self):
        return sum(i["precio"] * i["cantidad"] for i in self._items.values())
