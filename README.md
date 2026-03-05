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
**_The inputs are expected to be entered one by one, including numbers with multiple digits_**

Examples:

- `5` `+` `3` `=` → shows `8`
- `9` `*` `9` `=` → shows `81`. Clears by `C` → `0`
- `8` `/` `0` `=` → shows `Error`

Quit with `q`.
