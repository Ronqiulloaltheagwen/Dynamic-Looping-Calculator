# Simple looping calculator

while True:
    a = float(input("First number: "))
    b = float(input("Second number: "))
    op = input("Operation (+ - * /): ")

    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print("Error" if b == 0 else a / b)
    else:
        print("Invalid")

    if input("Again? (y/n): ") != "y":
        break
