start = float(input('Укажите количество км за первый день'))
goal = float(input('Укажите конечное количество км'))
days = 1
while start < goal:
    days += 1
    start += 1.1
else:
    print(f'день = {days}')
