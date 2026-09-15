# wap to remove duplicate number

numbers = [10, 20, 10, 30, 20, 40, 30]
unique_numbers = []
seen_numbers = set()

for number in numbers:
	if number not in seen_numbers:
		unique_numbers.append(number)
		seen_numbers.add(number)

print("Original numbers:", numbers)
print("Numbers without duplicates:", unique_numbers)