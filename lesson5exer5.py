from random import randrange

random_numbers = [randrange(1, 200) for _ in range(50)]

with open('task05.txt', 'w') as output_data:
    output_data.write(" ".join(map(str, random_numbers)))

with open('task05.txt') as input_data:
    numbers = input_data.read().split()

    print(sum(float(x) for x in numbers))