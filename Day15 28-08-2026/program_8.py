def factorial(number):
	if number < 0:
		raise ValueError("Factorial is not defined for negative numbers")

	result = 1
	for value in range(1, number + 1):
		result *= value
	return result


number = int(input("enter the nmber"))
print(f"Factorial of {number}: {factorial(number)}")
