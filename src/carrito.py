class Carrito:
    def __init__(self):
        self._items = {}
        self._descuento = 0

    def agregar(self, nombre, precio, cantidad=1):
        if precio <= 0 or cantidad <= 0:
            raise ValueError("Precio y cantidad deben ser positivos")
        item = self._items.setdefault(nombre, {"precio": precio, "cantidad": 0})
        item["cantidad"] += cantidad

    def eliminar(self, nombre):
        if nombre not in self._items:
            raise KeyError(nombre)
        del self._items[nombre]

    def aplicar_descuento(self, porcentaje):
        if not 0 <= porcentaje <= 100:
            raise ValueError("El descuento debe estar entre 0 y 100")
        self._descuento = porcentaje

    def subtotal(self):
        return sum(i["precio"] * i["cantidad"] for i in self._items.values())

    def total(self):
        return round(self.subtotal() * (1 - self._descuento / 100), 2)
