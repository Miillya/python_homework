class Worker:
    def __init__(self, name, surname, position, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"salary": salary, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
       return f"{self.name } {self.surname}"

    def get_total_income(self):
       return self._income["salary"] + self._income["bonus"]


employee = Position("John", "Dou", "developer", 10000, 8000)
print(employee.name)
print(employee.surname)
print(employee._income)
print(employee.get_full_name())
print(employee.get_total_income())
