import pytest
from day09.mymath import add, div


@pytest.fixture
def numbers():
    """Базовая пара чисел для тестов"""
    return (10, 5)


def test_add(numbers):
    a, b = numbers
    assert add(a, b) == 15


def test_div(numbers):
    a, b = numbers
    assert div(a, b) == 2


def test_div_zero(zero_divisor):
    a, b = zero_divisor
    with pytest.raises(ZeroDivisionError):
        div(a, b)
