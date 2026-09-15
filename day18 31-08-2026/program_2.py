# write text to it
file=open("example.txt", "a", encoding="utf-8")
file.write("This is additional text added to the file.\n")
print("Text written to file successfully!")
file.close()
