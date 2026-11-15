# Lesson 12: While loops

Matches the current recorded lesson. Python 3; no third-party packages.

## Practice

Run `python practice.py` after writing your solution. Try the task before opening `worked_answer.py`.

- Count non-quit choices only.
- help → list → q must report 2 choices.
- q as the first input must report 0 choices.
- Keep the quit value out of the count.

## Examples and expected results

Run one file at a time, for example `python 01_example.py`. Each file is independent. The filenames below are the actual examples.

### 01_counter.py

counter.

Expected terminal output (including prompts for interactive examples):

```text
0
1
2
Finished
```

### 02_zero_iterations.py

zero iterations.

Expected terminal output (including prompts for interactive examples):

```text
Finished
```

### 03_menu.py

menu.

Enter these values, one per prompt:

```text
help
list
q
```

Expected terminal output (including prompts for interactive examples):

```text
Choose help, list, or q: You chose: help
Choose help, list, or q: You chose: list
Choose help, list, or q: Goodbye
```

### 04_count_actions.py

count actions.

Enter these values, one per prompt:

```text
help
list
q
```

Expected terminal output (including prompts for interactive examples):

```text
Choose help, list, or q: You chose: help
Choose help, list, or q: You chose: list
Choose help, list, or q: Choices handled: 2
```

## Worked answer

[worked_answer.py](worked_answer.py) implements the practice task. Its matching example above lists the scripted inputs and expected output.

The intentional missing-update loop is explained in the video but omitted as a runnable download because it does not terminate. Stop a stuck program with Ctrl+C, then restore the update.

## Course repository

[All lessons](../../README.md)
