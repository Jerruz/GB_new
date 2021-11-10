END_OF_LINE = '\n'
NEW_LINE = '\n\t'


def array_to_string(array):
    return f"{END_OF_LINE}[{NEW_LINE}{NEW_LINE.join(f'{str(l)},' for l in array)}{END_OF_LINE}]{END_OF_LINE}"


class ListNumberError(Exception):
    def __init__(self, element: str):
        super().__init__(
            f"В массиве указан неверный элемент. Должно указываться число, а получено: '{element}'"
        )


try:
    print("Тестируем исключение")
    raise ListNumberError([1, 2, 3, 4, "erse"])
except ListNumberError as ln:
    print(ln)

print(
    "\nНачало основной программы.\nВведите пустую строку для формирования массива и вывода его на экран. \nВвод exit завершит работу скрипта.")
user_data = 1

while user_data != "exit":
    array_of_number = []
    user_data = 1
    while user_data != "" and user_data != "exit":
        try:
            try:
                user_data = input(">> ")
                array_of_number.append(int(user_data))
            except ValueError as ve:
                raise ListNumberError(user_data)
        except ListNumberError as lne:
            print(lne)
    print("\nВывод итогового массива:", array_to_string(array_of_number), sep='\n')
