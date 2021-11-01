class Worker:
    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        if isinstance(income, dict) and 'wage' in income and 'bonus' in income:
            self._income = income
        else:
            raise ValueError(f"Переданы некорректные данные: {income}")


class Position(Worker):
    def __init__(self, name: str, surname: str, position: str, income: dict):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


test_position = Position("Иван", "Иванов", "Инженер", {'bonus': 2000, 'wage': 30000})
print(f"Полное имя позиции: {test_position.get_full_name()}")
print(f"Получит средств: {test_position.get_total_income()}")
