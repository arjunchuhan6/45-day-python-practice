
def even_odd(number):
	if number % 2 == 0:
		return "Even"
	return "Odd"


number = int(input("enter the number "))
print(f"{number} is {even_odd(number)}")
