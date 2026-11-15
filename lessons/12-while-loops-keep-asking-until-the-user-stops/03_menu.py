# menu
choice = ""
while choice != "q":
    choice = input("Choose help, list, or q: ")
    if choice != "q":
        print(f"You chose: {choice}")
print("Goodbye")
