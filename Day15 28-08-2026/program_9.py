def prime_or_composite(number):
	if number < 2:
		return "Neither prime nor composite"

	for divisor in range(2, int(number ** 0.5) + 1):
		if number % divisor == 0:
			return "Composite"
	return "Prime"


number = int(input("Enter a number: "))
print(f"{number} is {prime_or_composite(number)}")
