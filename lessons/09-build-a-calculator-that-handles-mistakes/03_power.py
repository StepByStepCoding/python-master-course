# power
left = float(input("First number: "))
operator = input("Operation (+, -, *, /, **): ")
right = float(input("Second number: "))

if operator == "+":
    print(f"Result: {left + right}")
elif operator == "-":
    print(f"Result: {left - right}")
elif operator == "*":
    print(f"Result: {left * right}")
elif operator == "/":
    if right == 0:
        print("Cannot divide by zero.")
    else:
        print(f"Result: {left / right}")
elif operator == "**":
    print(f"Power result: {left ** right}")
else:
    print("Choose +, -, *, /, or **.")
