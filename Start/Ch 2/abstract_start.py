# Python Object-Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to enforce class constraints
from abc import ABC, abstractmethod
from math import pi
import math


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calc_area(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def calc_area(self):
        return round(pi * self.radius ** 2, 2)

    def __str__(self):
        return f" Class {self.__module__.title()} \n radius = {self.radius}"


class Square(GraphicShape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def calc_area(self):
        return self.side * self.side


# g = GraphicShape()

if __name__ == "__main__":
    c = Circle(10)
    print(c.calc_area())
    s = Square(12)
    print(s.calc_area())
    print(type(Circle))
    print(Circle.__str__(c))
    print(Circle.__mro__)
