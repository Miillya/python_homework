use = int(input('введите секунды'))
print(use)
hours = use // 3600
minutes = (use % 3600) // 60
seconds = (use % 3600) % 60
result = f'{hours:02}:{minutes:02}:{seconds:02}'
print(result)