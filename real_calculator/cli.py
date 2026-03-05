from __future__ import annotations

from .controller import realcalculatorController


def main() -> None:
    ctl = realcalculatorController()
    print("real-calculator (type calculator keys separated by spaces; 'q' to quit)")
    print("Supported keys: 0-9  .  +  -  *  /  sqrt  =  C")
    print(f"Display: {ctl.display}")

    while True:
        raw = input("> ").strip()
        if raw.lower() in {"q", "quit", "exit"}:
            break
        if not raw:
            continue

        for token in raw.split():
            try:
                ctl.press(token)
            except Exception as e:  # keep CLI forgiving
                print(f"Error: {e}")
                ctl.press("C")
                break

        print(f"Display: {ctl.display}")
