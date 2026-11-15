# Lesson 9: Build a calculator that handles mistakes

Matches the current recorded lesson. Python 3; no third-party packages.

## Practice

Run `python practice.py` after writing your solution. Try the task before opening `worked_answer.py`.

- Add ** for exponentiation: 2 ** 3 → 8.0.
- Use small, nonnegative whole-number exponents.
- Update the prompt and unsupported-choice message.
- Keep the division-by-zero check. Test all three routes.

## Examples and expected results

Run one file at a time, for example `python 01_example.py`. Each file is independent. The filenames below are the actual examples.

### 01_decimal_addition.py

decimal addition.

Enter these values, one per prompt:

```text
2
3.5
```

Expected terminal output (including prompts for interactive examples):

```text
First number: Second number: Result: 5.5
```

### 02_route.py

route +.

Enter these values, one per prompt:

```text
2
+
3
```

Expected terminal output (including prompts for interactive examples):

```text
First number: Operation (+, -, *, /): Second number: Result: 5.0
```

### 03_power.py

power.

Enter these values, one per prompt:

```text
2
**
3
```

Expected terminal output (including prompts for interactive examples):

```text
First number: Operation (+, -, *, /, **): Second number: Power result: 8.0
```

### 04_intentional_raw_zero_intentional_error.py

intentional raw zero.

Expected intentional error: `ZeroDivisionError: division by zero`.

## Worked answer

[worked_answer.py](worked_answer.py) implements the practice task. Its matching example above lists the scripted inputs and expected output.

The lesson handles unsupported operators and division by zero. It expects numeric input for the two numbers; nonnumeric text still raises ValueError. Exception handling comes later.

## Course repository

[All lessons](../../README.md)
