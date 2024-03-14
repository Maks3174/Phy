class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print("Двигун запущено.")

    def __str__(self):
        return f"Марка: {self.brand}, Модель: {self.model}, Рік: {self.year}"

    def __eq__(self, other):
        return self.year == other.year

    def __lt__(self, other):
        return self.year < other.year

    def __le__(self, other):
        return self.year <= other.year

    def __gt__(self, other):
        return self.year > other.year

    def __ge__(self, other):
        return self.year >= other.year

car1 = Car("Mercedes-Benz", "W220", 2005)
car2 = Car("BMW", "X5", 2010)

print(car1 < car2)
print(car1 == car2)

print(car1)
print(car2)