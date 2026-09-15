#wap to replace one word with another word in a string
string = input("Enter a string: ")
old_word = input("Enter the word to be replaced: ")
new_word = input("Enter the new word: ")
result = string.replace(old_word, new_word)
print("The new string is:", result)
