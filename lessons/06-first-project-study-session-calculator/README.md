# Class 6: First project - a study-session calculator

This project combines `input()`, `int()`, and arithmetic.

- `01_fixed_values.py` plans a session with fixed numbers: 4 sessions of 25 study minutes plus a 5-minute break each.
- `02_interactive.py` asks for those numbers instead, converts each answer with `int()`, and calculates:
  - study-only minutes: `sessions * study_minutes`
  - total minutes including breaks: `sessions * (study_minutes + break_minutes)` (the rule here is that **every session includes a break, including the last one**)
  - hours and leftover minutes: `total // 60` and `total % 60`

Try `03_practice.py`: build the whole calculator yourself. For 4 sessions, 25 study minutes, and 5 break minutes you should get 100 study minutes, 120 total minutes, and 2 hours and 0 minutes. Work out the numbers by hand first, then test a second set of values. Compare with `04_worked_answer.py` afterward.

The output says `1 hours` for a single hour. That is a deliberate simple label in this class, not a bug in your code.

## Files

- [01_fixed_values.py](01_fixed_values.py)
- [02_interactive.py](02_interactive.py)
- [03_practice.py](03_practice.py)
- [04_worked_answer.py](04_worked_answer.py)

## Run a file

Open this folder in VS Code and use **Run Python File in Terminal**, or run a file from a terminal in this folder:

```sh
python 02_interactive.py
```

Type each answer at the prompt and press Enter. On Windows, `py` may be available as an alternative to `python`. These lessons use Python 3 and require no third-party packages. Practice files intentionally produce no output until you add your code.

See [expected outputs](EXPECTED_OUTPUTS.md) to check a run.
