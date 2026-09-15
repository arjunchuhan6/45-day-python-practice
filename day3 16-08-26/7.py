# wap to removes spaces from the beginning and end of a string without using built-in functions
s = input("Enter a string: ")
start = 0
while start < len(s) and s[start] == ' ':
    start += 1
end = len(s) - 1
while end >= 0 and s[end] == ' ':
    end -= 1
print("String after removing spaces:", s[start:end+1])
