# read the file
file=open("example.txt", "r", encoding="utf-8")
content=file.read()
print("Content of the file:")
print(content)
file.close()