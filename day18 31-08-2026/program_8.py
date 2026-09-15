# search for  a word
file=open("example.txt", "r", encoding="utf-8")
content=file.read()
word_to_search="Arjun Rajput"
if word_to_search in content:
    print(f"The word '{word_to_search}' is found in the file.")
else:
    print(f"The word '{word_to_search}' is not found in the file.")
file.close()