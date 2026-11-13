# Class 5: Ask the user with input() and interactive programs

Work through examples 01–05 in order:

- `input("prompt")` shows the prompt, waits for the learner to type, and returns what they typed.
- `input()` **always returns text** (a `str`), even when the learner types digits. `"20" + "5"` joins the text into `"205"`.
- `int()` converts whole-number text to an integer, so you can calculate with it. `float()` does the same for decimals.
- `f"{hours:.1f}"` shows one decimal place. It changes the display only, not the stored value.
- Text that is not a number, such as `ten`, makes `int()` raise a `ValueError`. `05_invalid_number.py` fails **on purpose** when you type a word. Run it once with `10` and once with `ten`.

Try `06_practice.py`: ask for a name and a whole-number lesson target, greet the learner, and print the target plus one. Run it twice with different answers; the code should not need to change. Compare with `07_worked_answer.py` afterward.

## Files

- [01_greeting.py](01_greeting.py)
- [02_numeric_text.py](02_numeric_text.py)
- [03_convert.py](03_convert.py)
- [04_float.py](04_float.py)
- [05_invalid_number.py](05_invalid_number.py) (intentional error when you type a word)
- [06_practice.py](06_practice.py)
- [07_worked_answer.py](07_worked_answer.py)

## Run a file

Open this folder in VS Code and use **Run Python File in Terminal**, or run a file from a terminal in this folder:

```sh
python 01_greeting.py
```

Each program waits for you to type at the prompt, then press Enter. On Windows, `py` may be available as an alternative to `python`. These lessons use Python 3 and require no third-party packages. Practice files intentionally produce no output until you add your code.

See [expected outputs](EXPECTED_OUTPUTS.md) to check a run.
