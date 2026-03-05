from real_calculator.controller import realcalculatorController


def press_seq(controller: realcalculatorController, seq: list[str]) -> str:
    for key in seq:
        controller.press(key)
    return controller.display


def test_full_addition_flow():
    ctl = realcalculatorController()
    assert press_seq(ctl, ["5", "+", "3", "="]) == "8"


def test_clear_resets_after_calculation():
    ctl = realcalculatorController()
    assert press_seq(ctl, ["9", "*", "9", "="]) == "81"
    assert press_seq(ctl, ["C"]) == "0"


def test_division_by_zero_shows_error():
    ctl = realcalculatorController()
    assert press_seq(ctl, ["8", "/", "0", "="]) == "Error"
    # Next input should start fresh
    assert press_seq(ctl, ["1", "+", "1", "="]) == "2"
