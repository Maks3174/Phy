#1
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Builder(Human):
    def __init__(self, name, age, specialty):
        super().__init__(name, age)
        self.specialty = specialty


    def build(self):
        print(f"{self.name} is building")

class Sailor(Human):
    def __init__(self, name, age, ship):
        super().__init__(name, age)
        self.ship = ship

    def cargo(self):
        print(f"{self.name} deals with cargo")

class Pilot(Human):
    def __init__(self, name, age, aircraft):
        super().__init__(name, age)
        self.aircraft = aircraft


    def flight(self):
        print(f"{self.name} is flying")


builder = Builder("John", 35, "Carpenter")
sailor = Sailor("Mike", 40, "Ship1")
pilot = Pilot("Emily", 30, "Plane1")

builder.build()
sailor.cargo()
pilot.flight()

#2
class Passport:
    def __init__(self, name, nationality, passport_number):
        self.name = name
        self.nationality = nationality
        self.passport_number = passport_number

    @staticmethod
    def display_passport_info(name, nationality, passport_number):
        print("Passport Information:")
        print(f"Name: {name}")
        print(f"Nationality: {nationality}")
        print(f"Passport Number: {passport_number}")


class ForeignPassport(Passport):
    def __init__(self, name, nationality, passport_number, visa_info, foreign_passport_number):
        super().__init__(name, nationality, passport_number)
        self.visa_info = visa_info
        self.foreign_passport_number = foreign_passport_number

    @staticmethod
    def display_foreign_passport_info(name, nationality, passport_number, visa_info, foreign_passport_number):
        Passport.display_passport_info(name, nationality, passport_number)
        print("Foreign Passport Information:")
        print(f"Visa Info: {visa_info}")
        print(f"Foreign Passport Number: {foreign_passport_number}")


Passport.display_passport_info("Mike", "USA", "123456789")
print()
ForeignPassport.display_foreign_passport_info("Mike", "USA", "123456789", "Valid", "987654321")


#3
class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

class Lion(Animal):
    def __init__(self, name, habitat, main_prey):
        super().__init__(name, habitat)
        self.main_prey = main_prey

class Crocodile(Animal):
    def __init__(self, name, habitat, size):
        super().__init__(name, habitat)
        self.size = size

class Kangaroo(Animal):
    def __init__(self, name, habitat, jump_height):
        super().__init__(name, habitat)
        self.jump_height = jump_height

lion = Lion("Leo", "Savannah", "Antelope")
crocodile = Crocodile("Snappy", "Swamp", "Large")
kangaroo = Kangaroo("Hoppy", "Outback", "High")

print("Lion:")
print(f"Name: {lion.name}")
print(f"Habitat: {lion.habitat}")
print(f"Main Prey: {lion.main_prey}")

print("Crocodile:")
print(f"Name: {crocodile.name}")
print(f"Habitat: {crocodile.habitat}")
print(f"Size: {crocodile.size}")

print("Kangaroo:")
print(f"Name: {kangaroo.name}")
print(f"Habitat: {kangaroo.habitat}")
print(f"Jump Height: {kangaroo.jump_height}")
