# source 1
numbers = [4, -1, 2, 0, 9]
for number in numbers:
    if number < 0:
        continue
    if number == 0:
        break
    print(number)
print("Finished")
