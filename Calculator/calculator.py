# I create this calculator using match statement



def calculator():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        match operator:
            case "+":
                result = num1 + num2
            case "-":
                result = num1 - num2
            case "*":
                result = num1 * num2
            case "/":
                result = num1 / num2 if num2 != 0 else "Error: Division by zero"
            case _:
                result = "Invalid operator!"

        print(f"Result: {result}")

    except ValueError:
        print("Error: Invalid number input!")

calculator()
