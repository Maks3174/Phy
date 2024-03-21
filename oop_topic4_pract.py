import math
#1
class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1


    @staticmethod
    def get_count():
        return Person.count

person1 = Person("Maks", 20)
person1 = Person("Ivan", 30)
person1 = Person("Oleksiy", 25)

print("Кількість створених об'єктів класу 'Person'", Person.get_count())


#2
class GeometryCalculator:
    count = 0

    @staticmethod
    def triangle_area_by_base_height(base, height):
        GeometryCalculator.count += 1
        return 0.5 * base * height

    @staticmethod
    def triangl_area_by_three_sides(a, b, c):
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        GeometryCalculator.count += 1
        return area

    @staticmethod
    def triangl_area_by_two_sides_angle(side1, side2, angle):
        GeometryCalculator.count += 1
        return 0.5 * side1 * side2 * math.sin(math.radians(angle))

    @staticmethod
    def rectangle_area(width, height):
        GeometryCalculator.count += 1
        return width * height

    @staticmethod
    def square_area(side):
        GeometryCalculator.count += 1
        return side ** 2

    @staticmethod
    def rhombus_area(diagonal1, diagonal2):
        GeometryCalculator.count += 1
        return 0.5 * diagonal1 * diagonal2

    @staticmethod
    def get_calculation_count():
        return GeometryCalculator.count

area1 = GeometryCalculator.triangle_area_by_base_height(5, 4)
area2 = GeometryCalculator.triangl_area_by_three_sides(3, 4, 5)
area3 = GeometryCalculator.triangl_area_by_two_sides_angle(4, 5, 45)
area4 = GeometryCalculator.rectangle_area(6, 3)
area5 = GeometryCalculator.square_area(4)
area6 = GeometryCalculator.rhombus_area(6, 8)

print("Площа трикутника за допомогою основи та висоти:", area1)
print("Площа трикутника за допомогою трьох сторін (за формулою Герона):", area2)
print("Площа трикутника за допомогою двох сторін та кута між ними:", area3)
print("Площа прямокутника:", area4)
print("Площа квадрата:", area5)
print("Площа ромба:", area6)
print("Кількість підрахунків площі:", GeometryCalculator.get_calculation_count())

#3
class Calculator:
    @staticmethod
    def maximum(a, b, c, d):
        return max(a, b, c, d)

    @staticmethod
    def minimum(a, b, c, d):
        return min(a, b, c, d)

    @staticmethod
    def average(a, b, c, d):
        return sum([a, b, c, d]) / 4

    @staticmethod
    def factorial(n):
        if n < 0:
            raise ValueError("Факторіал не можна обчислити для від'ємного числа")
        return math.factorial(n)

a = 5
b = 6
c = 7
d = 8

print("Максимум з чотирьох аргументів:", Calculator.maximum(a, b, c, d))
print("Мінімум з чотирьох аргументів:", Calculator.minimum(a, b, c, d))
print("Середнє арифметичне з чотирьох аргументів:", Calculator.average(a, b, c, d))
print("Факторіал аргументу:", Calculator.factorial(5))