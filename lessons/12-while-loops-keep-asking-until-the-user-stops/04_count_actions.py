# count actions
choice = ""
handled = 0
while choice != "q":
    choice = input("Choose help, list, or q: ")
    if choice != "q":
        handled = handled + 1
        print(f"You chose: {choice}")
print(f"Choices handled: {handled}")
