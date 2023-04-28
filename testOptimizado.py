import pytest
from optimizado import optimizadoclass

def test_add_arrayNumeros():
    optimizado = optimizadoclass()
    assert len(optimizado.arrayNumeros()) == 0
    optimizado.add(3)
    assert len(optimizado.arrayNumeros()) == 1

def test_media():
    optimizado = optimizadoclass()
    optimizado.arrayNumeros().clear()
    assert len(optimizado.arrayNumeros()) == 0
    optimizado.add(5)
    optimizado.add(5)
    optimizado.add(5)
    assert len(optimizado.arrayNumeros()) == 3
    assert optimizado.media() == 5.0
def test_add():
    optimizado = optimizadoclass()
    assert optimizado.arrayNumeros() == [5,5,5]