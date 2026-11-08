import pytest
from src.carrito import Carrito

def test_carrito_nuevo_esta_vacio():
    assert Carrito().subtotal() == 0

def test_agregar_producto_calcula_subtotal():
    c = Carrito()
    c.agregar("Laptop", 1000, 2)
    assert c.subtotal() == 2000
