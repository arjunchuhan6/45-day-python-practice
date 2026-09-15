# copy one file to another
with open("example.txt", "r", encoding="utf-8") as file1:
    content = file1.read()

with open("copy_example.txt", "w", encoding="utf-8") as file2:
    file2.write(content)

print("File copied successfully!")

with open("copy_example.txt", "r", encoding="utf-8") as file2:
    print("file2 contents:", file2.read())