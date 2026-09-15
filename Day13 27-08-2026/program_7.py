number_squares = {number: number ** 2 for number in range(1, 11)}

print("Numbers and their squares:")
for number, square in number_squares.items():
    print(f"{number}: {square}")