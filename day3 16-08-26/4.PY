#wap revser a string dont use function 
s = input("Enter a string: ")
reversed_string = ""
for i in range(len(s)-1, -1, -1):
    reversed_string += s[i]
print("Reversed string is:", reversed_string)