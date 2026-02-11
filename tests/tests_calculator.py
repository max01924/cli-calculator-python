import pytest
from calculator import calculate

@pytest.mark.parametrize("expr, expected", [
    ("1 + 2", 3),
    ("3 - 5", -2),
    ("4 * 5", 20),
    ("10 / 2", 5.0),
    ("2 ** 3", 8),
    ("-5 + 2", -3),
    ("-(3 + 2)", -5),
    ("3 + 4 * 2", 11),         # Reihenfolge der Operationen
    ("(3 + 4) * 2", 14),       # Klammern
])
def test_basic_operations(expr, expected):
    assert calculate(expr) == expected

@pytest.mark.parametrize("expr", [
    "10 / 0",
    "abc + 1",
    "3 $ 4",
    "",
])
def test_errors(expr):
    result = calculate(expr)
    assert "Fehler" in result
