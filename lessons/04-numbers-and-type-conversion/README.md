# Class 4: Numbers, calculations, and type conversion

Work through examples 01–07 in order:

- Arithmetic follows precedence; parentheses change the order. `**` means exponentiation.
- `/` divides, `//` uses floor division, and `%` gives the remainder.
- Floor division rounds toward negative infinity: `-7 // 2` is `-4`. `int(-3.5)` truncates toward zero to `-3`.
- `int()` and `float()` convert valid numeric text; `str()` converts a value to text. Adding strings joins them; adding numbers calculates a sum.
- `f"{value:.2f}"` formats a display with two decimal places. It does not change the stored value. `round()` returns a rounded number; `int()` truncates.

The cost examples use **fictional teaching rates, not real provider prices**. Try `08_practice.py` with 250 requests at a fictional cost of 0.004 each. Calculate the estimate and display two decimal places. Compare with `09_worked_answer.py` afterward.

## Files

- [01_order.py](01_order.py)
- [02_division.py](02_division.py)
- [03_negative.py](03_negative.py)
- [04_conversion.py](04_conversion.py)
- [05_precision.py](05_precision.py)
- [06_estimate.py](06_estimate.py)
- [07_decimal_estimate.py](07_decimal_estimate.py)
- [08_practice.py](08_practice.py)
- [09_worked_answer.py](09_worked_answer.py)

## Run a file

Open this folder in VS Code and use **Run Python File in Terminal**, or run a file from a terminal in this folder:

```sh
python 01_order.py
```

On Windows, `py` may be available as an alternative to `python`. These lessons use Python 3 and require no third-party packages. Practice files intentionally produce no output until you add your code.

See [expected outputs](EXPECTED_OUTPUTS.md) to check a run.
