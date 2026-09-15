#find set intersection

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Intersection finds the elements common to both sets.
intersection_operator = set_a & set_b
intersection_method = set_a.intersection(set_b)

print("Set A:", set_a)
print("Set B:", set_b)
print("Intersection using &:", intersection_operator)
print("Intersection using intersection():", intersection_method)