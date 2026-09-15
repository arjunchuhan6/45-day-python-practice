#solve five mixed functional-programming questions using map, filter, zip, and enumerate functions in Python
#question 1: Use the map() function to square each number in a list of numbers.
numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared_numbers)

#question 2: Use the filter() function to get all even numbers from a list of numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

#question 3: Use the zip() function to combine two lists into a list of tuples.
names = ['Alice', 'Bob', 'Charlie', 'David']
ages = [25, 30, 35, 40]

combined = list(zip(names, ages))
print("Combined list of tuples:", combined)

#question 4: Use the enumerate() function to get the index and value of each element in a list.
names = ['Alice', 'Bob', 'Charlie', 'David']

for i, name in enumerate(names):
    print(f"Index: {i}, Name: {name}")

#question 5: Use the map() function to convert all strings in a list to uppercase.
strings = ['hello', 'world', 'python', 'programming']

uppercase_strings = list(map(lambda x: x.upper(), strings))
print("Uppercase strings:", uppercase_strings)