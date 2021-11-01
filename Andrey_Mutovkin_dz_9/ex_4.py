MAX_TOWNCAR_SPEED = 60
MAX_WORKCAR_SPEED = 40


class Car:
    def __init__(self, speed: float, color: str, name: str, is_police: bool = False):
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police

    def go(self, speed=None):
        """
        Изменяет скорость движения автомобиля.
        Если не передать параметр скорости, то будет использоваться предустановленная при инициализации класса.
        """
        if speed is not None:
            self._speed = speed
        print(f"Машина {self._name} цвета {self._color} едет со скоростью {self._speed}.")
        return self

    def stop(self):
        """
        Выставляет скорость машины в 0.
        """
        self._speed = 0
        print(f"Машина {self._name} цвета {self._color} остановилась.")
        return self

    def turn(self, direction: str):
        """
        Поворот машины.
        """
        print(f"Машина {self._name} цвета {self._color} повернула на {direction}.")
        return self

    def show_speed(self):
        """
        Выводит текущую скорость автомобиля.
        """
        print(f"Машина {self._name} цвета {self._color} едет со скоростью {self._speed}.")
        return self


class TownCar(Car):
    def __init__(self, speed: float, color: str, name: str):
        super().__init__(speed, color, name)

    def show_speed(self):
        """
        Выводит текущую скорость автомобиля.
        """
        if self._speed <= MAX_TOWNCAR_SPEED:
            print(f"Машина {self._name} цвета {self._color} едет со скоростью {self._speed}.")
        else:
            print(
                f"Машина {self._name} цвета {self._color} едет со скоростью {self._speed}. Внимание, машина превысила скорость!")
        return self


class WorkCar(Car):
    def __init__(self, speed: float, color: str, name: str):
        super().__init__(speed, color, name)

    def show_speed(self):
        """
        Выводит текущую скорость автомобиля.
        """
        if self._speed <= MAX_WORKCAR_SPEED:
            print(f"Машина {self._name} цвета {self._color} едет со скоростью {self._speed}.")
        else:
            print(
                f"Машина {self._name} цвета {self._color} едет со скоростью {self._speed}. Внимание, машина превысила скорость!")
        return self


class SportCar(Car):
    def __init__(self, speed: float, color: str, name: str):
        super().__init__(speed, color, name)


class PoliceCar(Car):
    def __init__(self, speed: float, color: str, name: str):
        super().__init__(speed, color, name, is_police=True)


car = Car(70, 'красная', 'test1', is_police=False)
town_car = TownCar(30, 'желтая', 'test2')
work_car = WorkCar(40, 'белая', 'test3')
sport_car = SportCar(30, 'черная', 'test4')
police_car = PoliceCar(30, 'голубая', 'test5')

car.show_speed().turn("лево").stop().go(40).show_speed().turn('право')
town_car.show_speed().turn("лево").stop().go(80).show_speed().turn('право')
work_car.show_speed().turn("лево").stop().go(50).show_speed().turn('право')
sport_car.show_speed().turn("лево").stop().go(120).show_speed().turn('право')
police_car.show_speed().turn("лево").stop().go(90).show_speed().turn('право')
