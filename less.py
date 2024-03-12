import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


circle1 = Circle(4)
print("Площа кола з радіусом 4:", circle1.area())
