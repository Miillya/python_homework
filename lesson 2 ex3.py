month = int(input('напишите номер месяц'))
my_dict = {'Winter': (12, 1, 2),
           'Spring': (3, 4, 5),
           'Summer': (6, 7, 8),
           'Autumn': (9, 10, 11)
}
for season, months in my_dict.items():
    if month in months:
        print(f'{season}')
        break

