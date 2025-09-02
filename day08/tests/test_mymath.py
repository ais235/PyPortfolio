import pytest
from day08.tests.mymath import percent, clamp

# --- Тесты для percent ---

def test_percent_basic():
    assert percent(50, 200) == 25.0
    assert percent(0, 10) == 0.0
    assert percent(30, 120) == 25.0

def test_percent_zero_whole_returns_none():
    assert percent(5, 0) is None

@pytest.mark.parametrize(
    "part,whole,expected",
    [
        (1, 4, 25.0),
        (2, 8, 25.0),
        (3, 12, 25.0),
        (12.5, 50, 25.0),
    ],
)
def test_percent_parametrized(part, whole, expected):
    assert percent(part, whole) == expected

# --- Тесты для clamp ---

def test_clamp_inside_range():
    assert clamp(5, 0, 10) == 5

def test_clamp_below_low():
    assert clamp(-3, 0, 10) == 0

def test_clamp_above_high():
    assert clamp(999, 0, 10) == 10

def test_clamp_invalid_range_raises():
    with pytest.raises(ValueError):
        clamp(1, 10, 0)
