my_list = [1, 2, 3, 4, 5, 6]

# Identity operators
a = my_list
b = [1, 2, 3, 4, 5]

is_same_object = a is my_list
is_not_same_object = b is not my_list

# Membership operators
element_in_list = 3 in my_list
element_not_in_list = 6 not in my_list

print("a is my_list:", is_same_object)            # a is my_list: This will print True because a is assigned directly to my_list, making them the same object in memory.
print("b is not my_list:", is_not_same_object)    # b is not my_list: This will print True because b is a new list with the same elements as my_list, but it's a different object in memory.
print("3 in my_list:", element_in_list)           # 3 in my_list: This will print True since 3 is indeed an element of my_list.
print("6 not in my_list:", element_not_in_list)   # 6 not in my_list: This will print False since 6 is an element of my_list