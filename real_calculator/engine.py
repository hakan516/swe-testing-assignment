from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation, getcontext
from typing import Any, Union

from .errors import CalculatorError

# High precision to keep Decimal math stable for typical calculator use.
getcontext().prec = 28

NumberLike = Union[int, float, str, Decimal]


def to_decimal(value: NumberLike) -> Decimal:
    """Convert supported numeric inputs to Decimal.

    Notes:
    - For floats, we use str(value) to avoid exposing binary float artifacts as much as possible.
    - For user input, controller passes strings, which are ideal for Decimal.
    """
    if isinstance(value, Decimal):
        return value
    if isinstance(value, int):
        return Decimal(value)
    if isinstance(value, float):
        return Decimal(str(value))
    if isinstance(value, str):
        try:
            # Allow leading/trailing whitespace and common user patterns.
            value = value.strip()
            if value == "":
                return Decimal(0)
            return Decimal(value)
        except InvalidOperation as e:
            raise CalculatorError(f"Invalid number: {value!r}") from e
    raise TypeError(f"Unsupported number type: {type(value).__name__}")


def format_decimal(value: Decimal) -> str:
    """Format a Decimal for calculator display.

    - Avoid scientific notation for normal-sized values
    - Remove trailing zeros
    - Normalize -0 to 0
    """
    if value.is_nan():
        return "Error"

    # Normalize -0 to 0
    if value == 0:
        return "0"

    # Use quantize-ish normalization without forcing a specific scale.
    normalized = value.normalize()

    # For values like 1E+3, normalize() may produce exponent form; format with 'f' where reasonable.
    # We keep exponent form only if it is extremely large/small.
    exp = normalized.as_tuple().exponent
    if exp <= -12 or exp >= 12:
        # Very small/large: fall back to engineering-like string
        return format(normalized, "f").rstrip("0").rstrip(".") if exp < 0 else str(normalized)

    s = format(normalized, "f")
    s = s.rstrip("0").rstrip(".")
    return s or "0"


@dataclass(frozen=True)
class CalculatorEngine:
    """Core calculation logic (pure functions)."""

    @staticmethod
    def add(a: NumberLike, b: NumberLike) -> Decimal:
        return to_decimal(a) + to_decimal(b)

    @staticmethod
    def subtract(a: NumberLike, b: NumberLike) -> Decimal:
        return to_decimal(a) - to_decimal(b)

    @staticmethod
    def multiply(a: NumberLike, b: NumberLike) -> Decimal:
        return to_decimal(a) * to_decimal(b)

    @staticmethod
    def divide(a: NumberLike, b: NumberLike) -> Decimal:
        divisor = to_decimal(b)
        if divisor == 0:
            raise CalculatorError("Division by zero")
        return to_decimal(a) / divisor
