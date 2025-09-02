def percent(part: float, whole: float):
    """
    Возвращает, сколько процентов составляет part от whole.
    Если whole == 0 — возвращает None.
    """
    if whole == 0:
        return None
    return (part / whole) * 100


def clamp(x: float, low: float, high: float) -> float:
    """Ограничивает x в диапазоне [low, high]."""
    if low > high:
        raise ValueError("low must be <= high")
    if x < low:
        return low
    if x > high:
        return high
    return x
