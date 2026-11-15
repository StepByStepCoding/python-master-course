# stop first
numbers = [0, 5, -2, 7, 11]
total = 0
for number in numbers:
    if number < 0:
        continue
    if number == 0:
        break
    total = total + number
print(f"Total: {total}")
