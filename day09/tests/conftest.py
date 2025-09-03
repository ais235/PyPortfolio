import pytest

@pytest.fixture
def zero_divisor():
    """Фикстура для проверки деления на ноль"""
    return (5, 0)
