# print before break
numbers = [4, -1, 2, 0, 9]
for number in numbers:
    if number < 0:
        continue
    print(number)
    if number == 0:
        break
print("Finished")
