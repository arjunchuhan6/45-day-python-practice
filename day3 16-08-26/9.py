#wap to count a particular character in a string without using built-in functions
s = input("Enter a string: ")
char = input("Enter a character to count: ")
count = 0
for c in s:
    if c == char:
        count += 1
print(f"The character '{char}' appears {count} times in the string.")