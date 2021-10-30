my_list = input('введите список').split(",")
print(my_list)
var = len(my_list) - 1
for el in range(0, var, 2):
    next_el = el + 1
    my_list[el], my_list[next_el] = my_list[next_el], my_list[el]
print(my_list)