import re

validate_date = re.compile(r'[0-9]{4}-[0-9]{2}-[0-9]{2}')
DATE_YEAR = 0
DATE_MONTH = 1
DATE_DAY = 2
DATE_MONTHS = [
    31,
    28,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31,
]
DATE_MONTH_STRING = [
    "в январе",
    "в феврале",
    "в марте",
    "в апреле",
    "в мае",
    "в июне",
    "в июле",
    "в августе",
    "в сентябре",
    "в октябре",
    "в ноябре",
    "в декабре",
]


class Date:
    def __init__(self, date):
        """
        date - YYYY-MM-DD
        """
        self.date = Date.validate_with_exception(date)

    @staticmethod
    def validate(date: str):
        if validate_date.match(date) is None:
            return False, f"Указанная дата {date} не совпадает с формой: YYYY-MM-DD."
        result = Date.get_date(date)
        if not (1 <= result[DATE_MONTH] <= 12):
            return False, f"Месяц в дате, должен указываться в пределах от 01 до 12. Указан: {result[DATE_MONTH]}"
        if not (1 <= result[DATE_DAY] <= 31):
            return False, f"Месяц в дате, должен указываться в пределах от 01 до 31. Указан: {result[DATE_DAY]}"
        if not (result[DATE_DAY] <= DATE_MONTHS[result[DATE_MONTH] - 1]):
            # Поправка на 29 февраля высокосного года
            if not (result[DATE_YEAR] % 4 == 0 and result[DATE_MONTH] == 1 and result[DATE_DAY] == 29):
                return False, f"Не может быть {result[DATE_DAY]} {DATE_MONTH_STRING[result[DATE_MONTH] - 1]}"
        return True, result

    @staticmethod
    def validate_with_exception(date: str):
        success, result = Date.validate(date)
        if not success:
            raise ValueError(result)
        else:
            return result

    @classmethod
    def get_date(date_class, date: str):
        return tuple(int(d) for d in date.split("-"))


test_list = [
    "2020-12-31",
    "2020.sw,22",
    "1099-41-12",
    "1230-02-30",
    "2020-04-20"
]

for test in test_list:
    try:
        print(f"\n\nТестовые данные: {test}")
        print("\tВалидация:")
        print("\t\t", {Date.validate(test)}, "\n")
        print("\tВызов get_date:")
        print("\t\t", Date.get_date(test), "\n")
        print("\tСоздание класса:")
        print("\t\t", Date(test).date, "\n")
    except ValueError as VE:
        print(f"\t\tБыло вызвано исключение: {VE}")
