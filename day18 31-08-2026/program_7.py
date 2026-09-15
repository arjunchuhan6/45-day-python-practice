# count characters
file=open("example.txt", "r", encoding="utf-8")
content=file.read()
print("Number of characters in the file:", len(content))
file.close()
