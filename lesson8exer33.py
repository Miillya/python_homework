class NonNumberListValueException(Exception):
    pass

def append_number(number_list: list):
    value = input("Enter number")

    try:
        number_list.append(float(value))
    except ValueError:
        raise NonNumberListValueException(f"you enter '{value}' instead of a number")

numbers = []

while True:
    try:
        append_number(numbers)
    except NonNumberListValueException as exception:
        print(exception)
    except KeyboardInterrupt:
        print(f"\nList number = {numbers}")
        break