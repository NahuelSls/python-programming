'''
From list to tuple
'''

my_list = [34, 82.6, "Darth Vader", 17, "Hanibal"]
my_tuple = (my_list[0], my_list[4], len(my_list))
print(my_tuple)

my_new_tuple = (my_list[0], my_list[-1], len(my_list))
print(my_new_tuple)