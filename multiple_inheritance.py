# Завдання 2
class Wheels:
    def __init__(self, count):
        self.count = count


class Engine:
    def __init__(self, type):
        self.type = type


class Doors:
    def __init__(self, count):
        self.count = count


class Car(Wheels, Engine, Doors):
    def __init__(self, count_wheels, engine_type, count_doors):
        Wheels.__init__(self, count_wheels)
        Engine.__init__(self, engine_type)
        Doors.__init__(self, count_doors)


car = Car(4, "Electric", 2)
print("Number of wheels:", car.count)
print("Engine type:", car.type)
print("Number of doors:", car.count)


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
class Employer:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def print_info(self):
        print("This is Employer class")


class President(Employer):
    def print_info(self):
        print("This is President class")


class Manager(Employer):
    def print_info(self):
        print("This is Manager class")


class Worker(Employer):
    def print_info(self):
        print("This is Worker class")


president = President("John", "President")
president.print_info()

manager = Manager("Mike", "Manager")
manager.print_info()

worker = Worker("Bob", "Worker")
worker.print_info()


# Завдання 5
class Employer:
    def __init__(self, name, position, age):
        self.name = name
        self.position = position
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old, {self.position}"

    def __int__(self):
        return self.age


class President(Employer):
    def __str__(self):
        return f"President {self.name}, {self.age} years old"

    def __int__(self):
        return self.age


class Manager(Employer):
    def __str__(self):
        return f"Manager {self.name}, {self.age} years old"

    def __int__(self):
        return self.age


class Worker(Employer):
    def __str__(self):
        return f"Worker {self.name}, {self.age} years old"

    def __int__(self):
        return self.age


president = President("John Doe", "President", 50)
print(str(president))
print(int(president))
manager = Manager("Alice Smith", "Manager", 40)
print(str(manager))
print(int(manager))
worker = Worker("Bob Johnson", "Worker", 30)
print(str(worker))
print(int(worker))