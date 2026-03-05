import pytest
from decimal import Decimal

from real_calculator.engine import CalculatorEngine, format_decimal
from real_calculator.errors import CalculatorError


def test_addition_integers():
    assert CalculatorEngine.add(5, 3) == Decimal(8)


def test_subtraction_integers():
    assert CalculatorEngine.subtract(10, 4) == Decimal(6)


def test_multiplication_integers():
    assert CalculatorEngine.multiply(6, 7) == Decimal(42)


def test_division_integers():
    assert CalculatorEngine.divide(8, 2) == Decimal(4)


def test_division_by_zero_raises():
    with pytest.raises(CalculatorError, match="Division by zero"):
        CalculatorEngine.divide(1, 0)


def test_negative_numbers():
    assert CalculatorEngine.add(-5, 2) == Decimal(-3)
    assert CalculatorEngine.subtract(-5, -2) == Decimal(-3)


def test_decimal_multiplication():
    # Using strings ensures exact Decimal input.
    assert CalculatorEngine.multiply("2.5", "4") == Decimal("10.0")


def test_large_number_addition():
    assert CalculatorEngine.add(10**18, 1) == Decimal("1000000000000000001")


def test_format_decimal_normalizes():
    assert format_decimal(Decimal("8.000")) == "8"
    assert format_decimal(Decimal("-0.0")) == "0"
    assert format_decimal(Decimal("3.1400")) == "3.14"
