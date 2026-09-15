# append text
file=open("example.txt", "a", encoding="utf-8")
file.write("This is additional text added to the file program 4.\n")
print("Text appended to file successfully!")
file.close()

with open("example.txt", "a", encoding="utf-8") as file:
    file.write("This is additional text added to the file with 'with' statement.\n")
    print("Text appended to file successfully!")
