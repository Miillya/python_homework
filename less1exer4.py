number = int(input('введите положительное число'))
max_num = 0
while number >0:
    if number % 10 > max_num:
        max_num = number % 10
        if max_num == 9:
            break
    number //=10
print(max_num)