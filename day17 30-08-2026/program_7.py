#filter numbers greater tha 50
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
greater_than_50 = list(filter(lambda x: x > 50, numbers))
print("Numbers greater than 50:", greater_than_50)
