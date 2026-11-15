# Lesson 10: Python lists

Matches the current recorded lesson. Python 3; no third-party packages.

## Practice

Run `python practice.py` after writing your solution. Try the task before opening `worked_answer.py`.

- Start with Python basics, Strings and Numbers.
- Append Lists. Replace the first item with Python foundations.
- Pop the last item and save its returned value.
- Print the final list, its length and the removed item. Predict first.

## Examples and expected results

Run one file at a time, for example `python 01_example.py`. Each file is independent. The filenames below are the actual examples.

### 01_list_and_length.py

list and length.

Expected terminal output (including prompts for interactive examples):

```text
3
```

### 02_read_topics_0.py

read topics[0].

Expected terminal output (including prompts for interactive examples):

```text
Python
```

### 03_read_topics_1.py

read topics[1].

Expected terminal output (including prompts for interactive examples):

```text
Data
```

### 04_read_topics_1.py

read topics[-1].

Expected terminal output (including prompts for interactive examples):

```text
AI
```

### 05_read_ai_in_topics.py

read "AI" in topics.

Expected terminal output (including prompts for interactive examples):

```text
True
```

### 06_read_math_in_topics.py

read "Math" in topics.

Expected terminal output (including prompts for interactive examples):

```text
False
```

### 07_append_and_replace.py

append and replace.

Expected terminal output (including prompts for interactive examples):

```text
['Python', 'Data', 'AI', 'Projects']
['Python', 'Clean data', 'AI', 'Projects']
```

### 08_pop.py

pop.

Expected terminal output (including prompts for interactive examples):

```text
['Python', 'Clean data']
Removed: Projects
```

### 09_duplicate_remove.py

duplicate remove.

Expected terminal output (including prompts for interactive examples):

```text
['Python', 'AI']
```

### 10_index_error_intentional_error.py

index error.

Expected intentional error: `IndexError: list index out of range`.

### 11_fixed_index.py

fixed index.

Expected terminal output (including prompts for interactive examples):

```text
AI
```

### 12_empty_index_intentional_error.py

empty index.

Expected intentional error: `IndexError: list index out of range`.

### 13_missing_removal_intentional_error.py

missing removal.

Expected intentional error: `ValueError: list.remove(x): x not in list`.

### 14_answer.py

answer.

Expected terminal output (including prompts for interactive examples):

```text
['Python foundations', 'Strings', 'Numbers']
3
Removed: Lists
```

### 15_middle_data_change.py

middle data change.

Expected terminal output (including prompts for interactive examples):

```text
['Python foundations', 'Text', 'Numbers']
3
Removed: Lists
```

## Worked answer

[worked_answer.py](worked_answer.py) implements the practice task. Its matching example above lists the scripted inputs and expected output.

## Course repository

[All lessons](../../README.md)
