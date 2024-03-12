class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print("Двигун запущено.")


car1 = Car("Mercedes-Benz", "W220", 2005)
car1.start_engine()