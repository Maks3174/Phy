class User:
    def __init__(self, name, age, email):
        self.__name = name
        self.__age = age
        self.__email = email

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_email(self):
        return self.__email


user1 = User("Maks", 20, "Maks@example.com")

print("Ім'я:", user1.get_name())
print("Вік:", user1.get_age())
print("Email:", user1.get_email())

#2
class ShoppingCart:
    def __init__(self):
        self.__items = {}

    def add_item(self, product, price, quantity=1):
        if product not in self.__items:
            self.__items[product] = {"price": price, "quantity": quantity}
        else:
            self.__items[product]["quantity"] += quantity

    def total_price(self):
        total = 0
        for item in self.__items.values():
            total += item["price"] * item["quantity"]
        return total


cart = ShoppingCart()

cart.add_item("Молоко", 25, 2)
cart.add_item("Хліб", 15)
cart.add_item("Яйця", 10, 2)

print("Загальна вартість покупок:", cart.total_price())

#3
class ElectronicWallet:
    def __init__(self):
        self.__balance = 0

    def add_money(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Гроші у сумі {amount} було додано до гаманця.")
        else:
            print("Сума для додавання має бути більше 0.")

    def remove_money(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Гроші у сумі {amount} було видалено з гаманця.")
        elif amount > self.__balance:
            print("Недостатньо грошей на рахунку.")
        else:
            print("Неприпустима сума для видалення.")

    def check_balance(self):
        return self.__balance


wallet = ElectronicWallet()

wallet.add_money(100)

print("Поточний баланс:", wallet.check_balance())

wallet.remove_money(25)

print("Поточний баланс:", wallet.check_balance())

wallet.remove_money(100)

#4
class Computer:
    def __init__(self, processor, ram, graphics_card):
        self.__processor = processor
        self.__ram = ram
        self.__graphics_card = graphics_card

    def get_processor(self):
        return self.__processor

    def get_ram(self):
        return self.__ram

    def get_graphics_card(self):
        return self.__graphics_card


computer = Computer("Intel Core i7", "16GB", "NVIDIA GeForce RTX 3080")

print("Процесор:", computer.get_processor())
print("ОЗУ:", computer.get_ram())
print("Відеокарта:", computer.get_graphics_card())
