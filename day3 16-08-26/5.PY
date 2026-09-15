#cconvert a string to upper case without function
s = input("Enter a string: ")
upper_string = ""
for char in s:
    if 'a' <= char <= 'z':
        upper_string += chr(ord(char) - 32)
    else:
        upper_string += char
print("Upper case string is:", upper_string)
