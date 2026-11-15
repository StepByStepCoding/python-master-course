# source 3
numbers = [5, -2, 7, 0, 11]
total = 0
for number in numbers:
    if number < 0:
        continue
    if number == 0:
        break
    total = total + number
print(f"Total: {total}")
