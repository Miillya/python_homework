proceeds = int(input('введите выручку'))
costs = int (input('введите издержки'))
profit = proceeds - costs
print(profit)
if profit > 0:
    profitability = profit / proceeds
    print(profitability)
    employees = int(input('введите количество сотрудников'))
    print(employees)
    per_employees = profit / employees
    print(per_employees)
elif profit == 0:
    print('zero')
else:
    print('убыток')
