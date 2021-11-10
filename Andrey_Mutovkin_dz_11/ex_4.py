from enum import Enum
from prettytable import PrettyTable


class InventoryCollision(Exception):
    def __init__(self, storage_model, inventory_number):
        super().__init__(
            f"В складе {storage_model} уже присутствует техника с инвентаризационным номером: {inventory_number}.")


class EquipmentTypes(Enum):
    printer = 1
    scaner = 2
    xerox = 3
    computer = 4
    monitor = 5


class Equipment:
    """
    Компонент, который можно разместить на складе.

    inventory_number - Инвентаризационный номер.
    model - модель.
    description - описание.
    type - тип компонента
    parametres - параметры компонента.
    """
    location = None

    def __init__(self, inventory_number: str, model: str, description: str, equipment_type: str, parametres: dict = {}):
        self.__inventory_number = inventory_number
        self.__model = model
        self.__description = description
        self.__type = equipment_type
        self.__parametres = parametres

    @property
    def inventory_number(self):
        return self.__inventory_number

    @property
    def model(self):
        return self.__model

    @property
    def description(self):
        return self.__description

    @property
    def type(self):
        return self.__type  # .name

    @property
    def parametres(self):
        return self.__parametres


class Storage:
    def __init__(self, name, location):
        """
        Создает склад с местоположением {location}.
        """
        self.__name = name
        self.__location = location
        self.__storage = {}

    @property
    def location(self):
        return self.__location

    @property
    def name(self):
        return self.__name

    def place(self, equipment: Equipment):
        self.__storage[equipment.inventory_number] = equipment
        self.__storage[equipment.inventory_number].location = self
        return self

    def take(self, inventory_number: str):
        equipment = self.__storage[inventory_number]
        equipment.location = None
        del (self.__storage[inventory_number])
        return equipment

    def get_storage_list(self, equipment_type: str = None):
        return {
            inventory_number: equipment
            for inventory_number, equipment in self.__storage.items()
            if equipment.type == equipment_type or equipment_type is None
        }

    def get_equipments_types(self):
        equipments_types = set()
        for equipment in self.__storage.values():
            equipments_types.add(equipment.type)
        return equipments_types


class PrinterTypes(Enum):
    laser = 1
    led = 2
    jet = 3


class Printer(Equipment):
    """
    printer_type - Тип принтера, определяется классом PrinterTypes
    """

    def __init__(self, inventory_number: str, model: str, description: str, printer_type: PrinterTypes):
        super().__init__(inventory_number, model, description, EquipmentTypes.printer, {"printer_type": printer_type})


class Scaner(Equipment):
    def __init__(self, inventory_number: str, model: str, description: str):
        super().__init__(inventory_number, model, description, EquipmentTypes.scaner)


class Xerox(Equipment):
    def __init__(self, inventory_number: str, model: str, description: str):
        super().__init__(inventory_number, model, description, EquipmentTypes.xerox)


class Computer(Equipment):
    """
    internal_components - внутренние компоненты.
    """

    def __init__(self, inventory_number: str, model: str, description: str, internal_components: list):
        super().__init__(inventory_number, model, description, EquipmentTypes.computer,
                         {"internal_components": internal_components})


class MonitorTypes(Enum):
    crt = 1
    lcd = 2
    les = 3
    plasma = 4


class Monitor(Equipment):
    def __init__(self, inventory_number: str, model: str, description: str, monitor_type: MonitorTypes,
                 frame_rate: int = 60):
        super().__init__(inventory_number, model, description, EquipmentTypes.monitor)
        self.__species = monitor_type
        self.__frame_rate = frame_rate

    @property
    def species(self):
        return self.__species

    @property
    def frame_rate(self):
        return self.__frame_rate


MENU_STORAGE = """
Выбери один из следующих вариантов:
    1. Посмотреть существующие склады (отделы)
    2. Добавить склад
    3. Удалить склад
    4. Работать с конкретным складом

    0. Выход

Ваш выбор: """

MENU_COMPONENT = """
    1. Посмотреть доступную на складе технику
    2. Добавить на склад компонент
    3. Убрать со склада компонент
    4. Передать на другой склад

    0. Вернуться к выбору складов

Ваш выбор: """

CHOOSE_STORAGE = """
Вебирите, по какому параметру нужно выбрать склад:
    1. По номеру склада
    2. По имени склада

Ващ выбор: """

sep = "=================================================================\n"

MENU_CHOOSE_ERROR = f"{sep}Введите число, которое указано напротив нужного вам пункта меню!\n{sep}"


def show_storages(storages):
    """
    Выводит список складов.
    """
    table = PrettyTable()
    table.field_names = ["Номер склада", "Имя склада", "Местоположение"]
    for num in range(len(storages)):
        table.add_row([num, storages[num].name, storages[num].location])
    print(f'{table}\n')


def add_storage(storages):
    """
    Добавляет склад.
    """
    print("Добавление склада.")
    name = input("Введите имя склада: ")
    location = input("Введите месторасположение склада: ")
    storages.append(Storage(name, location))
    print("Склад добавлен!")


def choose_storage(storages):
    """
    Выбирает конкретный склад и возвращает его экземпляр.
    """
    submenu = int(input(CHOOSE_STORAGE))
    if submenu == 1:
        num = int(input("Укажите номер склада: "))
        try:
            return storages[num]
        except:
            raise IndexError(f"Склад с номером {num} не найден!")
    elif submenu == 2:
        name = input("Укажите имя склада: ")
        for storage in storages:
            if storage.name == name:
                return storage
        raise IndexError(f"Склад с именем {name} не найден!")
    else:
        raise ValueError("Не выбран корректный пункт меню!")


def del_storage(storages):
    try:
        submenu = int(input(CHOOSE_STORAGE))
        if submenu == 1:
            num = int(input("Укажите номер удаляемого склада: "))
            storages.pop(num)
            print(f"Склад с номером {num} удален! Номера складов были обновлены!")
        elif submenu == 2:
            name = input("Введите имя удаляемого склада: ")
            for num in range(len(storages) - 1, -1, -1):
                if storages[num].name == name:
                    storages.pop(num)
                    print(f"Склад с номером {num} удален!")
            print("Номера складов были обновлены!")
        else:
            raise ValueError("Не выбран корректный пункт меню!")
    except ValueError as ve:
        raise ve
    except IndexError:
        raise IndexError("Указан несуществующий номер склада!")


def show_components(storage):
    """
    Выводит список техники.
    """
    table = PrettyTable()
    table.field_names = ["Инвентаризационный номер", "Модель", "Тип", "Описание", "Параметры"]
    for inventory_number, equipment in storage.get_storage_list().items():
        table.add_row([inventory_number, equipment.model, equipment.type, equipment.description, equipment.parametres])
    print(f'{table}\n')


def input_inventory_number():
    return input("Введите инвентаризационный номер: ")


def input_parametres():
    print("Введите параметры в виде: имя_параметра=значение. Оставьте строку пустой, для окончания ввода. ")
    parametres = {}
    parametres_input = -1
    while parametres_input != "":
        try:
            parametres_input = input("> ")
            if parametres_input != "":
                temp = parametres_input.split('=')
                parametres[temp[0].strip()] = temp[1].strip()
        except Exception as e:
            print(f"Параметр задан неверно. Error: {e}")
    return parametres


def add_component(storage):
    """
    Добавляет компонент.
    """
    storage.place(Equipment(
        input("Введите инвентаризационный номер: "),
        input("Введите модель: "),
        input("Введите описание компонента: "),
        input("Введите тип компонента: "),
        input_parametres()
    ))


def del_component(storage):
    print("Удаление компонента. ")
    storage.take(input_inventory_number())


def transfer_component(storage, to_storage):
    print("Перемещение компонента. ")
    to_storage.place(storage.take(input_inventory_number()))
    print(f"Компонент перемещен со склада {storage.name} на {to_storage.name}")


def working_with_storage(storage):
    print(f"Вы вошли в управление складом {storage.name}! Его месторасположение: {storage.location}")
    menu = -1
    while menu != 0:
        try:
            menu = int(input(MENU_COMPONENT))
            if menu == 1:
                show_components(storage)
            elif menu == 2:
                add_component(storage)
            elif menu == 3:
                del_component(storage)
            elif menu == 4:
                transfer_component(storage, choose_storage(storages))
            elif menu != 0:
                raise ValueError("Введен некорректный пункт меню!")
        except Exception as e:
            print(f"Ошибка: {e}")
            print(MENU_CHOOSE_ERROR)


if __name__ == '__main__':
    print('Добро пожаловать в складской учет!')
    menu = -1
    storages = []
    while menu != 0:
        try:
            menu = int(input(MENU_STORAGE))
            if menu == 1:
                show_storages(storages)
            elif menu == 2:
                add_storage(storages)
            elif menu == 3:
                del_storage(storages)
            elif menu == 4:
                working_with_storage(choose_storage(storages))
            elif menu != 0:
                raise ValueError("Введен некорректный пункт меню!")
        except Exception as e:
            print(f"Ошибка: {e}")
            print(MENU_CHOOSE_ERROR)
