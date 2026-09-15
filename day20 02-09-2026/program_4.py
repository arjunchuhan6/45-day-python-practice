#wap handle invalid list index exception without try and except block
my_list = [1, 2, 3,5,6,7,5,6,12,3,45,321,5,12,3,45,3,15,21,51,31,5,13651,5,3541,54,6541,351,351,53413,5135,135,135,1]
index = int(input("Enter an index to access the list: "))
if 0 <= index < len(my_list):
    print("The value at index", index, "is:", my_list[index])
else:
    print("Error: Index out of range. Please enter a valid index.")
