class Stationery:
    def __init__(self, title: str):
        self._title = title

    def draw(self):
        print("Запуск отрисовки.")
        return self


class Pen(Stationery):
    def __init__(self):
        super().__init__("ручка")

    def draw(self):
        print("Рисуем ручкой.")
        return self


class Pencil(Stationery):
    def __init__(self):
        super().__init__("карандаш")

    def draw(self):
        print("Рисуем карандашом.")
        return self


class Handle(Stationery):
    def __init__(self):
        super().__init__("маркер")

    def draw(self):
        print("Рисуем маркером.")
        return self


test_stationery = Stationery("test")
test_pen = Pen()
test_pencil = Pencil()
test_handle = Handle()

test_stationery.draw()
test_pen.draw()
test_pencil.draw()
test_handle.draw()