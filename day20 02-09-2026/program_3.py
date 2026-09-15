#wap handle missing file exception without try and except block
import os
file_name = "test.txt"
if os.path.exists(file_name):
    with open(file_name, "r") as file:
        content = file.read()
    print(content)
else:
    print("The file does not exist. Please check the file name and try again.")
    