#1,2
import math
class Shape:
    def area(self):
        pass

    def __int__(self):
        return round(self.area())  # Округлення результату до цілого числа

    def __str__(self):
        return f"Figure: {self.__class__.__name__}"

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectangle: Length={self.length}, Width={self.width}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle: Radius={self.radius}"

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"Triangle: Base={self.base}, Height={self.height}"

class Trapezoid(Shape):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

    def __str__(self):
        return f"Trapezoid: Base1={self.base1}, Base2={self.base2}, Height={self.height}"

rectangle = Rectangle(4, 5)
print(int(rectangle))
print(str(rectangle))

circle = Circle(3)
print(int(circle))
print(str(circle))

triangle = Triangle(4, 6)
print(int(triangle))
print(str(triangle))

trapezoid = Trapezoid(3, 5, 4)
print(int(trapezoid))
print(str(trapezoid))


#3
class Shape:
    def Show(self):
        pass

    def Save(self, filename):
        pass

    @staticmethod
    def Load(filename):
        pass

class Square(Shape):
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def Show(self):
        print(f"Square: Left Top Corner ({self.x}, {self.y}), Side Length: {self.side}")

    def Save(self, filename):
        with open(filename, "a") as file:
            file.write(f"Square,{self.x},{self.y},{self.side}\n")

    @staticmethod
    def Load(filename):
        squares = []
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(",")
                if data[0] == "Square":
                    x, y, side = map(int, data[1:])
                    squares.append(Square(x, y, side))
        return squares

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def Show(self):
        print(f"Rectangle: Left Top Corner ({self.x}, {self.y}), Width: {self.width}, Height: {self.height}")

    def Save(self, filename):
        with open(filename, "a") as file:
            file.write(f"Rectangle,{self.x},{self.y},{self.width},{self.height}\n")

    @staticmethod
    def Load(filename):
        rectangles = []
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(",")
                if data[0] == "Rectangle":
                    x, y, width, height = map(int, data[1:])
                    rectangles.append(Rectangle(x, y, width, height))
        return rectangles


square = Square(0, 0, 5)
rectangle = Rectangle(1, 1, 4, 6)

square.Save("shapes.txt")
rectangle.Save("shapes.txt")

loaded_squares = Square.Load("shapes.txt")
loaded_rectangles = Rectangle.Load("shapes.txt")

for square in loaded_squares:
    square.Show()

for rectangle in loaded_rectangles:
    rectangle.Show()
