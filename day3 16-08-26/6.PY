#wap  convert a string to lower case without function
s = input("Enter a string: ")
lower_string = ""
for char in s:
    if 'A' <= char <= 'Z':
        lower_string += chr(ord(char) + 32)
    else:
        lower_string += char
print("Lower case string is:", lower_string)