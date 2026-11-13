# Expected outputs

Run each file independently and type the answer shown after each prompt. These outputs were generated with Python 3.13. Practice solutions may use different names or values when the task allows them.

### 01_greeting.py

```text
Your name: Maya
Hello, Maya!
```

### 02_numeric_text.py

```text
Minutes today: 20
<class 'str'>
205
```

### 03_convert.py

```text
Minutes today: 20
After five more minutes: 25
```

### 04_float.py

```text
Hours studied: 1.5
Study time: 1.5 hours
```

With `1.75` the formatted display rounds to one decimal place:

```text
Hours studied: 1.75
Study time: 1.8 hours
```

### 05_invalid_number.py

Typing `10`:

```text
Minutes today: 10
10
```

Typing the word `ten` raises an error on purpose (the file path in your traceback will differ):

```text
Minutes today: ten
Traceback (most recent call last):
  File "05_invalid_number.py", line 3, in <module>
    minutes = int(minutes_text)
ValueError: invalid literal for int() with base 10: 'ten'
```

### 06_practice.py

No output until you add your solution.

### 07_worked_answer.py

Typing `Alex` and `4`:

```text
Your name: Alex
Lesson target: 4
Hello, Alex!
Next target: 5
```
