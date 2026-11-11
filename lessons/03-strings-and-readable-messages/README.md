# Class 3: Strings and readable messages

Strings hold text. Use matching single or double quotes, and choose the outer quotes so a quote inside the message remains valid. `+` joins strings. An f-string starts with `f` and inserts values using `{name}`. `\n` starts a new line.

Work through the numbered examples. `05_missing_f.py` compares literal braces with an actual f-string. `07_message_timing.py` shows that a message is built when the f-string expression runs; changing the name later does not rebuild an existing message.

**Deliberate error:** `intentional_errors/02_quote_repair_broken.py` has an unclosed quote and raises `SyntaxError`. Open it to spot the missing quote, then compare with `02_quote_repair.py`. Error wording varies by Python version. All other example files should run successfully.

Try `08_practice.py`: store a learner name and lesson title, build one f-string named `message` with two lines, and print it. Check `09_worked_answer.py` after completing your version.

## Files

- [01_quotes.py](01_quotes.py)
- [02_quote_repair.py](02_quote_repair.py)
- [03_join.py](03_join.py)
- [04_fstrings.py](04_fstrings.py)
- [05_missing_f.py](05_missing_f.py)
- [06_newline.py](06_newline.py)
- [07_message_timing.py](07_message_timing.py)
- [08_practice.py](08_practice.py)
- [09_worked_answer.py](09_worked_answer.py)
- [intentional_errors/02_quote_repair_broken.py](intentional_errors/02_quote_repair_broken.py)

## Run a file

Open this folder in VS Code and use **Run Python File in Terminal**, or run a file from a terminal in this folder:

```sh
python 01_quotes.py
```

On Windows, `py` may be available as an alternative to `python`. These lessons use Python 3 and require no third-party packages. Practice files intentionally produce no output until you add your code.

See [expected outputs](EXPECTED_OUTPUTS.md) to check a run.
