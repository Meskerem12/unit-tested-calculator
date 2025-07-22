import calculator

def test_add():
    assert calculator.add(3, 4) == 7

def test_subtract():
    assert calculator.subtract(10, 5) == 5

def test_multiply():
    assert calculator.multiply(3, 3) == 9

def test_divide():
    assert calculator.divide(10, 2) == 5

def test_divide_by_zero():
    assert calculator.divide(10, 0) == "Error: Division by zero"

def test_power():
    assert calculator.power(2, 3) == 8

def test_modulo():
    assert calculator.modulo(10, 3) == 1
