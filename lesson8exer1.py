class Date:
    day: int
    month: int
    year: int

    def __init__(self, date_string: str):
        numbers = Date.extract_numbers(date_string)
        self.validate_numbers(numbers)

        self.day, self.month, self.year = numbers

    @classmethod
    def extract_numbers(cls, date_string: str) -> list:
        return [int(x) for x in date_string.split('-')]

    @staticmethod
    def validate_numbers(numbers: list):
        d, m, y = numbers

        assert 1 <= d <= 31, "wrong number format"
        assert 1 <= m <= 12, "wrong month format"
        assert 1970 <= y <= 2100, "wrong year format"

my_date = Date('19-11-2021')