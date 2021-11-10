from math import atan, sin, cos


class Complex:
    def __init__(self, real, imagine):
        self.real = (real)
        self.imagine = (imagine)

    @property
    def radius(self):
        return ((self.real ** 2 + self.imagine ** 2) ** 0.5)

    @property
    def angle(self):
        return (atan(self.imagine / self.real))

    def __add__(self, other):
        return Complex(self.real + other.real, self.imagine + other.imagine)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imagine - other.imagine)

    def __mul__(self, other):
        temp_r = (self.radius * other.radius)
        temp_a = (self.angle + other.angle)
        return Complex(temp_r * cos(temp_a), temp_r * sin(temp_a))

    def __div__(self, other):
        temp_r = (self.radius / other.radius)
        temp_a = (self.angle - other.angle)
        return Complex(temp_r * cos(temp_a), temp_r * sin(temp_a))

    __truediv__ = __div__

    def __pow__(self, power):
        temp_r = (self.radius * power)
        temp_a = (self.angle * power)
        return Complex(temp_r * cos(temp_a), temp_r * sin(temp_a))

    def __str__(self):
        return f"{self.real} + {self.imagine} i"


complex1 = Complex(1, 3)
complex2 = Complex(3, 6)

print(f"""Исходные данные:
complex1: {complex1}
complex2: {complex2}

""")

test = {
    "complex1 + complex2": complex1 + complex2,
    "complex1 - complex2": complex1 - complex2,
    "complex1 / complex2": complex1 / complex2,
    "complex1 * complex2": complex1 * complex2,
    "complex1 ** 2": complex1 ** 2,
}

for name, result in test.items():
    print(f"Тест: {name}, Результат: {result}")
