# count lines
file=open("example.txt", "r", encoding="utf-8")
lines=file.readlines()
print("Number of lines in the file:", len(lines))
file.close()
