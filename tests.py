from functions import *

def test_func():
    assert func(3) == 4

def test_multiplication():
    assert multiplication(4, 8) == 32

def test_price_calculation():
    assert price_calculation(19) == 100
    assert price_calculation(20) == 120
    assert price_calculation(40) == 150
    assert price_calculation(65) == 200
    assert price_calculation(68) == 200
    assert price_calculation(-1) == None

def test_if_exists():
    assert if_exists("Kacper") == True
    assert if_exists(0) == False
    assert if_exists(125) == True
    assert if_exists(False) == False
