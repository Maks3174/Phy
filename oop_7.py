#1
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divine by zero"

    def __call__(self, operation, x, y):
        if operation == 'add':
            return self.add(x, y)
        elif operation == 'subtract':
            return self.subtract(x, y)
        elif operation == 'multiply':
            return self.multiply(x, y)
        elif operation == 'divine':
            return self.divide(x, y)
        else:
            return "Invalid operation"

calc = Calculator()
print(calc('add', 5, 3))
print(calc('subtract', 5, 3))
print(calc('multiply', 5, 3))
print(calc('divide', 10, 2))
print(calc('divide', 5, 0))


#2
class File:
    def __init__(self, name, size):
        self.name = name
        self._size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("File size must be a number.")
        if value < 0:
            raise ValueError("File size cannot be negative.")
        self._size = value

    def get_readable_size(self):
        kb_size = self.size / 1024
        if kb_size < 1:
            return f"{self.size} bytes"
        mb_size = kb_size / 1024
        if mb_size < 1:
            return f"{kb_size:.2f} KB"
        return f"{mb_size:.2f} MB"

file = File("document.txt", 2048)
print(file.get_readable_size())
#4
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if 0 <= value <= 120:
            self._age = value
        else:
            raise ValueError("Age must be between 0 and 120")

user1 = User("Mike", 25)
print(user1.age)
user1.age = 130


