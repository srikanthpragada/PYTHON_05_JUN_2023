import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return super().__str__() + f", {self.radius}"


class Square(Shape):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.side = side

    def area(self):
        return self.side * self.side

    def __str__(self):
        return super().__str__() + f", {self.side}"


c = Circle(10, 10, 30)
print(c)
print(c.area())
