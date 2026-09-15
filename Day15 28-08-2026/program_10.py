def calculator(first_number, operator, second_number):
	if operator == "+":
		return first_number + second_number
	elif operator == "-":
		return first_number - second_number
	elif operator == "*":
		return first_number * second_number
	elif operator == "/":
		if second_number == 0:
			return "Cannot divide by zero"
		return first_number / second_number
	else:
		return "Invalid operator"


first_number = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
second_number = float(input("Enter the second number: "))

result = calculator(first_number, operator, second_number)
print(f"Result: {result}")
