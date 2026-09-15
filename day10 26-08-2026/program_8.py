# fin set union

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union combines all unique elements from both sets.
union_operator = set_a | set_b
union_method = set_a.union(set_b)

print("Set A:", set_a)
print("Set B:", set_b)
print("Union using |:", union_operator)
print("Union using union():", union_method)