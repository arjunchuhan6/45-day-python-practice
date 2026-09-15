#tuple and sets
#create a tuple

numbers_tuple = (1, 2, 2, 3)
numbers_list = [1, 2, 2, 3]
numbers_set = {1, 2, 2, 3}

print("Tuple:", numbers_tuple)
print("List:", numbers_list)
print("Set:", numbers_set)

# Tuples and lists preserve order and allow duplicate values.
print("Tuple first item:", numbers_tuple[0])
numbers_list.append(4)
print("List after appending 4:", numbers_list)

# A set removes duplicates and does not support indexing.
numbers_set.add(4)
print("Set after adding 4:", numbers_set)

print("\nDifferences:")
print("Type       Ordered  Mutable  Duplicates  Syntax")
print("Tuple      Yes      No       Yes         (1, 2, 3)")
print("List       Yes      Yes      Yes         [1, 2, 3]")
print("Set        No       Yes      No          {1, 2, 3}")
