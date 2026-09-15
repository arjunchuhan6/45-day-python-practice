#wap to change an item in the list without knowing the index of the item
my_list = [1, 2, 3, 4, "Hacker hai bhai tu  "]
#change the item 3 to "Hacker hai bhai"    
my_list[my_list.index(3)] = "Hacker hai bhai"
print(my_list)