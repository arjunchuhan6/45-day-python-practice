#build a safe calculator using exception handling
def safe_calculator():
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ValueError("Division by zero is not allowed.")
            result = num1 / num2
        else:
            raise ValueError("Invalid operator. Please use +, -, *, or /.")

        print(f"The result of {num1} {operator} {num2} is: {result}")

    except ValueError as error:
        print("Error:", error)
    except Exception as e:
        print("An unexpected error occurred:", e)

# Call the function to run the calculator
safe_calculator()