from time import sleep


class TrafficLight:
    __waits = {
        'red': 7,  # Переключение с красного на желтый
        'yellow': 2,  # Переключение с желтого
        'green': 5  # Переключение с зеленого на желтый
    }

    def __init__(self):
        self.__color = 'red'
        self.__previous = 'yellow'

    def _new_color(self, color):
        sleep(self.__waits[self.__color])
        self.__previous = self.__color
        self.__color = color
        print(f'Цвет световора изменился с {self.__previous} на {self.__color}.')

    def running(self, color: str):
        if (self.__color == 'red' or self.__color == 'green') and color == 'yellow':
            self._new_color(color)
            return self
        elif (color == 'red' or color == 'green') and self.__color == 'yellow':
            self._new_color(color)
            return self
        raise ValueError(f'Был передан некорректный цвет: {color}, в данный момент установлен {self.__color}')

    def switch(self):
        if (self.__color == 'red' or self.__color == 'green') and self.__previous == 'yellow':
            self._new_color('yellow')
            return self
        elif self.__previous == 'red':
            self._new_color('green')
            return self
        elif self.__previous == 'green':
            self._new_color('red')
            return self


traffic_light = TrafficLight()

traffic_light.switch().switch().switch().switch().switch().switch()

traffic_light.running('yellow').running('green').running('yellow').running('red')
traffic_light.running('green')
