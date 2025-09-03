def add(a, b):
    """Складывает два числа"""
    return a + b


def div(a, b):
    """Делит a на b. Если b == 0, бросает ZeroDivisionError."""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль!")
    return a / b
