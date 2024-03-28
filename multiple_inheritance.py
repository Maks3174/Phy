# Завдання 2
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car: {self.brand} {self.model}")


class Wheels:
    def __init__(self, size, material):
        self.size = size
        self.material = material

    def display_info(self):
        print(f"Wheels: Size - {self.size}, Material - {self.material}")


class Engine:
    def __init__(self, power, fuel_type):
        self.power = power
        self.fuel_type = fuel_type

    def display_info(self):
        print(f"Engine: Power - {self.power}, Fuel Type - {self.fuel_type}")


class Doors:
    def __init__(self, number, automatic):
        self.number = number
        self.automatic = automatic

    def display_info(self):
        print(f"Doors: Number - {self.number}, Automatic - {self.automatic}")


class CarWithFeatures(Car, Wheels, Engine, Doors):
    def __init__(self, brand, model, size, material, power, fuel_type, number, automatic):
        Car.__init__(self, brand, model)
        Wheels.__init__(self, size, material)
        Engine.__init__(self, power, fuel_type)
        Doors.__init__(self, number, automatic)


car_with_features = CarWithFeatures("Toyota", "Camry", "18 inch", "Alloy", "180 hp", "Petrol", 4, True)
car_with_features.display_info()

# Завдання 3
class DomesticAnimal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def sound(self):
        print("Sound: [undefined]")

    def show(self):
        print("Name:", self.name)

    def type(self):
        print("Breed:", self.breed)


class Dog(DomesticAnimal):
    def sound(self):
        print("Sound: Woof!")

    def type(self):
        print("Breed: Dog")


class Cat(DomesticAnimal):
    def sound(self):
        print("Sound: Meow!")

    def type(self):
        print("Breed: Cat")


class Parrot(DomesticAnimal):
    def sound(self):
        print("Sound: Squawk!")

    def type(self):
        print("Breed: Parrot")


class Hamster(DomesticAnimal):
    def sound(self):
        print("Sound: Squeak!")

    def type(self):
        print("Breed: Hamster")


dog = Dog("Mike", "Golden Retriever")
dog.show()
dog.type()
dog.sound()

cat = Cat("Dill", "Siamese")
cat.show()
cat.type()
cat.sound()

parrot = Parrot("Hidi", "African Grey")
parrot.show()
parrot.type()
parrot.sound()

hamster = Hamster("Nik", "Syrian")
hamster.show()
hamster.type()
hamster.sound()


# Завдання 4
from datetime import datetime

class Employer:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def print_info(self):
        print(f"This is {self.position} {self.name}")

    def __str__(self):
        return f"{self.position}: {self.name}"

    def age(self, birth_year):
        current_year = datetime.now().year
        return current_year - birth_year


class President(Employer):
    def __init__(self, name, country, birth_year):
        super().__init__(name, "President")
        self.country = country
        self.birth_year = birth_year

    def print_info(self):
        super().print_info()
        print(f"He is the president of {self.country}")

    def __str__(self):
        return f"President: {self.name}, Country: {self.country}"

    def age(self):
        return super().age(self.birth_year)


class Manager(Employer):
    def __init__(self, name, department, birth_year):
        super().__init__(name, "Manager")
        self.department = department
        self.birth_year = birth_year

    def print_info(self):
        super().print_info()
        print(f"He manages the {self.department} department")

    def __str__(self):
        return f"Manager: {self.name}, Department: {self.department}"

    def age(self):
        return super().age(self.birth_year)


class Worker(Employer):
    def __init__(self, name, role, birth_year):
        super().__init__(name, "Worker")
        self.role = role
        self.birth_year = birth_year

    def print_info(self):
        super().print_info()
        print(f"He works as a {self.role}")

    def __str__(self):
        return f"Worker: {self.name}, Role: {self.role}"

    def age(self):
        return super().age(self.birth_year)


president = President("Joe Biden", "USA", 1942)
manager = Manager("Alice Smith", "Marketing", 1985)
worker = Worker("Bob Johnson", "Technician", 1990)

print(president)
print(manager)
print(worker)

print(f"President's age: {president.age()}")
print(f"Manager's age: {manager.age()}")
print(f"Worker's age: {worker.age()}")
