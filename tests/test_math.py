import pytest

@pytest.mark.math
def test_one_plus_one():
    assert  1 + 1 == 2

@pytest.mark.math
def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert  a + b == c

@pytest.mark.math
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)

'''Mutiplication test ideias
- two positive integers
- identify: multiply by 1
- zero: multiply by 0
- positive by negative
- negative by positive
- floats
'''

products = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (2, -4, -8),
    (-5,  -5, 25),
    (2.5, 6.7, 16.75),
    (1.5, 0, 0.0),
    (2.5, -3.7, -9.25),
]

@pytest.mark.math
@pytest.mark.parametrize("a, b, product", products)
def test_multiplication(a, b, product):
    assert a * b == product