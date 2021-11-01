WEIGHT = 25  # масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна


class Road:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def calculate_coverage(self, depth=5):  # depth - толщина полотна в см
        print(
            f'{self._width} м*{self._length} м*{WEIGHT} кг*{depth} см = {self._width * self._length * WEIGHT * depth // 1000} т.')
        return


street_lenina = Road(20, 5000)

street_lenina.calculate_coverage(5)
