# create a text file
file=open("example.txt", "w", encoding="utf-8")
file.write("This is an example text file.\n")
print("Text file created successfully!")
file.close()