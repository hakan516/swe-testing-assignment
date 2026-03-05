# Real-Calculator

Real-Calculator is a small, testable calculator application that supports addition, subtraction, multiplication, division, and a reset operation.  

## Requirements

- Python 3.10+ 

## Setup
```bash
python -m venv .venv
python -m pip install -U pip
pip install -r requirements.txt
```

## Run the application
```bash
python -m real_calculator
```
**_The inputs are expected to be entered one by one OR with spaces in between, including numbers with multiple digits_**

Examples:

- `5` `+` `3` `=` → shows `8`
- `9 * 9 =` → shows `81`. Clears by `C` → `0`
- `8` `/` `0` `=` → shows `Error`

Quit with `q`.

## How to run tests

```bash
pytest
```

## Testing framework research: Pytest vs Unittest

Python ships with unittest, which is a major advantage in environments that restrict dependencies. It provides a familiar structure with test cases via a built-in test runner. However, it tends to be more verbose, and mocking/fixtures often require more boilerplate to keep tests readable as the project grows.

Pytest is a widely used framework that focuses on concise, readable tests. Its assert produces clear failure messages without extra APIs, and its system makes test setup powerful. In practice, pytest often provides a lower test maintenance cost because tests stay short and expressive while still supporting advanced needs.

For real-calculator, pytest was chosen to keep the unit tests and integration tests readable while still supporting clean test organization and detailed assertions.
