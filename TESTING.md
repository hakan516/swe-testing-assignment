# Testing Strategy for real-calculator

This document explains what was tested, what was intentionally not tested, and how the overall testing approach relates to core lecture concepts.

## What was tested

### Unit tests (calculation logic)
Unit tests cover the core arithmetic operations implemented:

- Addition, subtraction, multiplication, division and squareroot
- Edge cases: division by zero, negative values, decimal arithmetic, and large numbers
- Output formatting (normalizing decimals for display)

These tests treat the engine functions as isolated units and validate deterministic behavior.

### Integration tests
Integration tests cover the interaction between the input layer and the calculation engine:

- Simulated button sequences such as `5 + 3 =`
- Clear behavior after a completed calculation
- Division-by-zero tests

## What was not tested

- **Non-functional testing** such as performance, load, accessibility, or security. It is out of scope.
- **UI layout issues**. its just a simple command line program.

## How this relates to Lecture concepts

### Testing Pyramid
The program follows the testing pyramid: many unit tests for the engine and a small number of integration tests for the controller flow. Keeps feedback fast while ensuring components collaborate.

### Black-box vs White-box Testing
- **Unit tests** are closer to *white-box* testing because they target specific engine functions and expected behaviors, including edge cases.
- **Integration tests** are closer to *black-box* testing because they exercise the controller through public “button press” inputs and assert the visible output (display), without depending on internal implementation details.

### Functional vs Non-Functional Testing
- The program focuses on **functional correctness** (the calculator returns correct results and handles invalid operations like divide-by-zero).
- It intentionally ignores **non-functional testing** (performance, usability, etc.) because the program centers on core testing technique.

### Regression Testing
The test program can be run on every change. If a future update accidentally breaks an existing behavior (e.g divide-by-zero handling changes), the tests will fail and flag the regression immediately.

## Test Results Summary

| Test name | Type | Status |
|---|---|---|
| `test_addition_integers` | Unit | Pass |
| `test_subtraction_integers` | Unit | Pass |
| `test_multiplication_integers` | Unit | Pass |
| `test_division_integers` | Unit | Pass |
| `test_division_by_zero_raises` | Unit | Pass |
| `test_negative_numbers` | Unit | Pass |
| `test_decimal_multiplication` | Unit | Pass |
| `test_large_number_addition` | Unit | Pass |
| `test_format_decimal_normalizes` | Unit | Pass |
| `test_sqrt_perfect_square` | Unit | Pass |
| `test_sqrt_non_perfect_square_matches_decimal_context` | Unit | Pass |
| `test_sqrt_negative_raises` | Unit | Pass |
| `test_full_addition_flow` | Integration | Pass |
| `test_clear_resets_after_calculation` | Integration | Pass |
| `test_division_by_zero_shows_error` | Integration | Pass |
| `test_sqrt_on_display_then_addition` | Integration | Pass |
| `test_sqrt_of_negative_shows_error` | Integration | Pass |
