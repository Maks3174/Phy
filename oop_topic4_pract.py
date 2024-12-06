import math
import os
#1
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
        print(f"{course} додано до списку курсів студента {self.name}.")

    def change_grade(self, new_grade):
        self.grade = new_grade
        print(f"Рівень студента {self.name} змінено на {self.grade}.")

    def change_age(self, new_age):
        self.age = new_age
        print(f"Вік студента {self.name} змінено на {self.age}.")

    def display_info(self):
        print(f"Ім'я: {self.name}, Вік: {self.age}, Рівень: {self.grade}, Курси: {', '.join(self.courses)}")

    @staticmethod
    def create_student():
        name = input("Введіть ім'я студента: ")
        while True:
            try:
                age = int(input("Введіть вік студента: "))
                if age <= 0:
                    raise ValueError("Вік повинен бути додатнім числом.")
                break
            except ValueError as e:
                print(e)
        while True:
            try:
                grade = int(input("Введіть клас студента: "))
                if grade <= 0:
                    raise ValueError("Рівень повинен бути додатнім числом.")
                break
            except ValueError as e:
                print(e)
        return Student(name, age, grade)

student1 = Student.create_student()
student1.add_course("Математика")
student1.add_course("Фізика")

student1.change_grade(12)
student1.change_age(19)

student1.display_info()

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

#4
class FileUtils:
    @staticmethod
    def count_lines(file_path):
        if not os.path.exists(file_path):
            print(f"Файл {file_path} не знайдено.")
            return 0

        with open(file_path, 'r') as file:
            lines = file.readlines()
            return len(lines)

file_path = "C:/Users/PC/Desktop/text.txt"
print("Кількість рядків у файлі:", FileUtils.count_lines(file_path))


#5
class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, target):
        print(f"{self.name} атакує {target.name} з уроном {self.damage}!")
        target.take_damage(self.damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} отримав {damage} урону і помер!")
        else:
            print(f"{self.name} отримав {damage} урону і залишився з {self.health} здоров'я.")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} відновив {amount} здоров'я. Тепер він має {self.health} здоров'я.")

    def display_info(self):
        print(f"Ім'я: {self.name}, Здоров'я: {self.health}, Урон: {self.damage}")

player = Character("Гравець", 100, 20)
enemy = Character("Ворог", 80, 15)

player.attack(enemy)
enemy.attack(player)

player.take_damage(10)
enemy.take_damage(25)

player.heal(15)

player.display_info()
enemy.display_info()

#6
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
        print(f"{course} додано до списку курсів студента {self.name}.")

student1 = Student("Іван", 18, 11)
student1.add_course("Математика")
student1.add_course("Фізика")

print(f"Курси студента {student1.name}: {student1.courses}")
