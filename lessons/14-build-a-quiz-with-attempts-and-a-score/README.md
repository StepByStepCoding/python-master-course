# Lesson 14: Build a quiz with attempts and a score

Matches the current recorded lesson. Python 3; no third-party packages.

## Practice

Run `python practice.py` after writing your solution. Try the task before opening `worked_answer.py`.

- Add: How many values does range(3) supply?
- Store the answer as the text "3". Update both lists.
- A perfect run should report 4/4.
- Test a wrong answer followed by a correct second attempt.

## Examples and expected results

Run one file at a time, for example `python 01_example.py`. Each file is independent. The filenames below are the actual examples.

### 01_cleaned_and_original.py

cleaned and original.

Expected terminal output (including prompts for interactive examples):

```text
python
  PYTHON
```

### 02_perfect.py

perfect.

Enter these values, one per prompt:

```text
  PYTHON  
if
5
```

Expected terminal output (including prompts for interactive examples):

```text
Language in this course?
Answer, or q to quit: Correct
Keyword for a condition?
Answer, or q to quit: Correct
What is 2 + 3?
Answer, or q to quit: Correct
Score: 3/3
```

### 03_four_questions_with_retry.py

four questions with retry.

Enter these values, one per prompt:

```text
python
if
5
2
3
```

Expected terminal output (including prompts for interactive examples):

```text
Language in this course?
Answer, or q to quit: Correct
Keyword for a condition?
Answer, or q to quit: Correct
What is 2 + 3?
Answer, or q to quit: Correct
How many values does range(3) supply?
Answer, or q to quit: Not correct
Answer, or q to quit: Correct
Score: 4/4
```

### 04_paired_list_mismatch_intentional_error.py

paired list mismatch.

Enter these values, one per prompt:

```text
python
if
5
3
```

Expected intentional error: `IndexError: list index out of range`.

## Worked answer

[worked_answer.py](worked_answer.py) implements the practice task. Its matching example above lists the scripted inputs and expected output.

## Course repository

[All lessons](../../README.md)
