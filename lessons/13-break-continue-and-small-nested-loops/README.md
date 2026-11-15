# Lesson 13: Break, continue and nested loops

Matches the current recorded lesson. Python 3; no third-party packages.

## Practice

Run `python practice.py` after writing your solution. Try the task before opening `worked_answer.py`.

- Use [5, -2, 7, 0, 11].
- Skip negative values. Stop at zero.
- Total only the values processed before the stop.
- Expected total: 12. Explain why 11 is excluded.

## Examples and expected results

Run one file at a time, for example `python 01_example.py`. Each file is independent. The filenames below are the actual examples.

### 01_source_0.py

source 0.

Expected terminal output (including prompts for interactive examples):

```text
4
2
0
9
```

### 02_source_1.py

source 1.

Expected terminal output (including prompts for interactive examples):

```text
4
2
Finished
```

### 03_source_2.py

source 2.

Expected terminal output (including prompts for interactive examples):

```text
1 1
1 2
1 3
2 1
2 2
2 3
```

### 04_source_3.py

source 3.

Expected terminal output (including prompts for interactive examples):

```text
Total: 12
```

### 05_print_before_break.py

print before break.

Expected terminal output (including prompts for interactive examples):

```text
4
2
0
Finished
```

### 06_inner_break.py

inner break.

Expected terminal output (including prompts for interactive examples):

```text
1 1
2 1
```

### 07_safe_continue_update.py

safe continue update.

Expected terminal output (including prompts for interactive examples):

```text
1
3
```

### 08_stop_first.py

stop first.

Expected terminal output (including prompts for interactive examples):

```text
Total: 0
```

## Worked answer

[worked_answer.py](worked_answer.py) implements the practice task. Its matching example above lists the scripted inputs and expected output.

The repaired while-loop example updates count before continue. Moving the update below continue can leave count unchanged and produce an infinite loop.

## Course repository

[All lessons](../../README.md)
