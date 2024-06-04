#1
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class CoffeeMachine(Device):
    def __init__(self, brand, model, cups):
        super().__init__(brand, model)
        self.cups = cups

    def make_coffee(self):
        print(f"Making coffee with {self.brand} {self.model}. Please wait...")

class Blender(Device):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model)
        self.speed = speed

    def blend(self):
        print(f"Blending with {self.brand} {self.model} at speed {self.speed}. Please wait...")

class MeatGrinder(Device):
    def __init__(self, brand, model, power):
        super().__init__(brand, model)
        self.power = power

    def grind_meat(self):
        print(f"Grinding meat with {self.brand} {self.model} using {self.power}W power. Please wait...")

coffee_machine = CoffeeMachine("Jura ", "E8 Piano", 2)
blender = Blender("Gorenje ", "HBC807QB", "High")
meat_grinder = MeatGrinder("Panasonic", "MK-MG1300WTQ", 1300)

coffee_machine.make_coffee()
blender.blend()
meat_grinder.grind_meat()


#2
class Ship:
    def __init__(self, name, displacement):
        self.name = name
        self.displacement = displacement

    def display_info(self):
        print(f"Ship Name: {self.name}")
        print(f"Displacement: {self.displacement} tons")


class Frigate(Ship):
    def __init__(self, name, displacement, missile_count):
        super().__init__(name, displacement)
        self.missile_count = missile_count

    def display_info(self):
        super().display_info()
        print(f"Missile Count: {self.missile_count}")


class Destroyer(Ship):
    def __init__(self, name, displacement, gun_count):
        super().__init__(name, displacement)
        self.gun_count = gun_count

    def display_info(self):
        super().display_info()
        print(f"Gun Count: {self.gun_count}")


class Cruiser(Ship):
    def __init__(self, name, displacement, missile_count, gun_count, aircraft_count):
        super().__init__(name, displacement)
        self.missile_count = missile_count
        self.gun_count = gun_count
        self.aircraft_count = aircraft_count

    def display_info(self):
        super().display_info()
        print(f"Missile Count: {self.missile_count}")
        print(f"Gun Count: {self.gun_count}")
        print(f"Aircraft Count: {self.aircraft_count}")


frigate = Frigate("Frigate 1", 1500, 24)
destroyer = Destroyer("Destroyer 1", 2000, 56)
cruiser = Cruiser("Cruiser 1", 3000, 32, 64, 12)

frigate.display_info()
print()
destroyer.display_info()
print()
cruiser.display_info()


#3
class Money:
    def __init__(self, dollars, cents):
        self._dollars = dollars
        self._cents = cents

    def display_amount(self):
        print(f"${self._dollars}.{self._cents}")

    def decrease_amount(self, amount):
        total_cents = self._dollars * 100 + self._cents
        amount_cents = amount._dollars * 100 + amount._cents

        if total_cents < amount_cents:
            print("Error: Insufficient funds.")
            return

        remaining_cents = total_cents - amount_cents
        self._dollars = remaining_cents // 100
        self._cents = remaining_cents % 100


class Product(Money):
    def __init__(self, name, dollars, cents):
        super().__init__(dollars, cents)
        self._name = name

    def display_product(self):
        print(f"Product: {self._name}")
        print("Price:", end=" ")
        self.display_amount()


wallet = Money(50, 75)
wallet.display_amount()

product = Product("Phone", 20, 50)
product.display_product()

print("\nBuying the product...")
product_price = Money(20, 50)
wallet.decrease_amount(product_price)
wallet.display_amount()
