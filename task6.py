a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
symbol = input("Enter a symbol (+, -, *, /, %, **,//): ")
if symbol == "+":
    result = a + b
    print("The result of addition is:", result) 
elif symbol == "-":
    result = a - b
    print("The result of subtraction is:", result)          
elif symbol == "*":
    result = a * b
    print("The result of multiplication is:", result)
elif symbol == "/":
    if b != 0:
        result = a / b
        print("The result of division is:", result)
    else:
        print("Error: Division by zero is not allowed.")
elif symbol == "%":
    result = a % b
    print("The result of modulo is:", result)
elif symbol == "**":
    result = a ** b
    print("The result of exponentiation is:", result)
elif symbol == "//":
    if b != 0:
        result = a // b
        print("The result of floor division is:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid symbol. Please enter a valid symbol (+, -, *, /, %, **).")   