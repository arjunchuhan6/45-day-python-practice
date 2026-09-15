# count words
file=open("example.txt", "r", encoding="utf-8")
content=file.read()
words=content.split()
print("Number of words in the file:", len(words))
file.close()