'''
Kth maximum integer in a list
'''

list = [10, 30, 60, 20, 90, 40]
k = 2
list.sort()
kth_max = list[-k]
print(list)
print("El número k más grande de la lista:", kth_max, '\n')

new_list = sorted(list, reverse=True)
print(new_list)
k = 3
new_kth_max = new_list[k - 1]
print(new_kth_max)