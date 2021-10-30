my_list = input('введите несколько слов').split()
for ind, el in enumerate(my_list, 1):
    print(f'{ind} {el[:10]}')