from processing import add, subtract, multiply, divide

def test_add() -> None:
    assert add(2.0,2.0) == 4.0

def test_subtract() -> None:
    assert subtract(4.0,2.0) == 2.0

def test_multiply() -> None:
    assert multiply(2.0,5.0) == 10.0

def test_divide() -> None:
    assert divide(10.0,2.0) == 5.0