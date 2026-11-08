import pytest
from src.carrito import Carrito

def test_carrito_nuevo_esta_vacio():
    assert Carrito().subtotal() == 0

def test_agregar_producto_calcula_subtotal():
    c = Carrito()
    c.agregar("Laptop", 1000, 2)
    assert c.subtotal() == 2000

def test_agregar_mismo_producto_suma_cantidad():
    c = Carrito()
    c.agregar("Mouse", 50, 1)
    c.agregar("Mouse", 50, 2)
    assert c.subtotal() == 150

@pytest.mark.parametrize("precio,cantidad", [(0, 1), (-5, 1), (10, 0), (10, -1)])
def test_rechaza_valores_invalidos(precio, cantidad):
    with pytest.raises(ValueError):
        Carrito().agregar("X", precio, cantidad)

def test_eliminar_producto():
    c = Carrito()
    c.agregar("Teclado", 80)
    c.eliminar("Teclado")
    assert c.subtotal() == 0

def test_eliminar_inexistente_lanza_error():
    with pytest.raises(KeyError):
        Carrito().eliminar("Fantasma")

def test_descuento_del_10_por_ciento():
    c = Carrito()
    c.agregar("Monitor", 200)
    c.aplicar_descuento(10)
    assert c.total() == 180

@pytest.mark.parametrize("pct", [-1, 101])
def test_descuento_invalido(pct):
    with pytest.raises(ValueError):
        Carrito().aplicar_descuento(pct)
