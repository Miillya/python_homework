class CustomZeroDivisionError(Exception):
    pass

def get_numerator() -> int:
    return int(input("enter numerator"))

def get_denominator() -> int:
    value = int(input("enter denominator"))

    if value == 0:
        raise CustomZeroDivisionError

    return value

while True:
    try:
        numerator = get_numerator()
        denominator = get_denominator()

        print(f"Result = {numerator / denominator}")
    except CustomZeroDivisionError:
        print("You entered 0 as the denominator, this will not work")
    except KeyboardInterrupt:
        break