# Pfind set difference

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Difference finds elements present in the first set but not the second.
difference_operator = set_a - set_b
difference_method = set_a.difference(set_b)

print("Set A:", set_a)
print("Set B:", set_b)
print("A - B:", difference_operator)
print("A.difference(B):", difference_method)
print("B - A:", set_b - set_a)