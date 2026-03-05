from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

from .engine import CalculatorEngine, format_decimal, to_decimal
from .errors import CalculatorError


@dataclass
class realcalculatorController:
    """A small, test-friendly input/controller layer.

    It simulates button presses and maintains calculator state (display, pending operator, etc.).
    This provides a stable seam for integration tests without needing a GUI toolkit.
    """

    display: str = "0"
    _accumulator: Optional[Decimal] = None
    _pending_op: Optional[str] = None
    _new_input: bool = True
    _error: bool = False

    def clear(self) -> None:
        self.display = "0"
        self._accumulator = None
        self._pending_op = None
        self._new_input = True
        self._error = False

    def press(self, key: str) -> str:
        """Press a calculator 'button' and return the updated display."""
        key = key.strip()

        if key.upper() == "C":
            self.clear()
            return self.display

        if self._error:
            # Any key after an error starts fresh (except Clear which we already handled).
            self.clear()

        if key in "0123456789":
            self._press_digit(key)
            return self.display

        if key == ".":
            self._press_decimal_point()
            return self.display

        if key in {"+", "-", "*", "/"}:
            self._press_operator(key)
            return self.display

        if key == "=":
            self._press_equals()
            return self.display

        if key.lower() in {"sqrt"}:
            self._press_sqrt()
            return self.display

        raise ValueError(f"Unsupported key: {key!r}")

    def _press_digit(self, digit: str) -> None:
        if self._new_input or self.display == "0":
            self.display = digit
        else:
            self.display += digit
        self._new_input = False

    def _press_decimal_point(self) -> None:
        if self._new_input:
            self.display = "0."
            self._new_input = False
            return
        if "." not in self.display:
            self.display += "."

    def _press_operator(self, op: str) -> None:
        current = to_decimal(self.display)

        if self._pending_op is not None and not self._new_input:
            # Chain operations like 2 + 3 + 4 =
            self._accumulator = self._apply(self._pending_op, self._accumulator, current)
            self.display = format_decimal(self._accumulator)
        elif self._accumulator is None:
            self._accumulator = current

        self._pending_op = op
        self._new_input = True

    def _press_equals(self) -> None:
        if self._pending_op is None or self._accumulator is None:
            # Nothing to compute
            return

        current = to_decimal(self.display)
        result = self._apply(self._pending_op, self._accumulator, current)

        self.display = format_decimal(result)
        self._accumulator = result
        self._pending_op = None
        self._new_input = True


    def _press_sqrt(self) -> None:
        """Apply square root to the current display (unary operator)."""
        try:
            current = to_decimal(self.display)
            result = CalculatorEngine.sqrt(current)
            self.display = format_decimal(result)
            # After a unary op, treat the display as a completed value.
            self._new_input = True
        except CalculatorError:
            self.display = "Error"
            self._error = True
            self._accumulator = None
            self._pending_op = None
            self._new_input = True

    def _apply(self, op: str, a: Optional[Decimal], b: Decimal) -> Decimal:
        if a is None:
            a = Decimal(0)
        try:
            if op == "+":
                return CalculatorEngine.add(a, b)
            if op == "-":
                return CalculatorEngine.subtract(a, b)
            if op == "*":
                return CalculatorEngine.multiply(a, b)
            if op == "/":
                return CalculatorEngine.divide(a, b)
        except CalculatorError:
            self.display = "Error"
            self._error = True
            self._accumulator = None
            self._pending_op = None
            self._new_input = True
            return Decimal("NaN")

        raise ValueError(f"Unsupported operator: {op!r}")
