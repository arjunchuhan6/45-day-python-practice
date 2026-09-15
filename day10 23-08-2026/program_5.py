# wap convert tuple to list

numbers_tuple = (10, 20, 30, 40)
numbers_list = list(numbers_tuple)

print("Tuple:", numbers_tuple)
print("List:", numbers_list)
print("Tuple type:", type(numbers_tuple))
print("List type:", type(numbers_list))

# The converted list can be changed.
numbers_list.append(50)
print("List after adding 50:", numbers_list)
