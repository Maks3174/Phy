

#4
class Watch:
    def __init__(self, model_name, manufacturer, year, price, type_of_watch):
        self.model_name = model_name
        self.manufacturer = manufacturer
        self.year = year
        self.price = price
        self.type_of_watch = type_of_watch

    def __str__(self):
        return f"Модель: {self.model_name}, Виробник: {self.manufacturer}, Рік випуску: {self.year}, Ціна: {self.price}, Тип: {self.type_of_watch}"

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __ne__(self, other):
        return self.price != other.price

watch1 = Watch("G-Shock", "Casio", 2020, 150, "наручний")
watch2 = Watch("Oyster Perpetual", "Rolex", 2018, 5000, "наручний")

print(watch1 < watch2)
print(watch1 <= watch2)
print(watch1 == watch2)
print(watch1 != watch2)
print(watch1 > watch2)
print(watch1 >= watch2)

print(watch1)
print(watch2)


#5
class Website:
    def __init__(self, name, address, description):
        self.name = name
        self.address = address
        self.description = description

    def __str__(self):
        return f"Назва: {self.name}, Адреса: {self.address}, Опис: {self.description}"

    def __eq__(self, other):
        return self.name == other.name and self.address == other.address and self.description == other.description

    def __lt__(self, other):
        return self.name < other.name

    def __le__(self, other):
        return self.name <= other.name

    def __gt__(self, other):
        return self.name > other.name

    def __ge__(self, other):
        return self.name >= other.name

    def __ne__(self, other):
        return self.name != other.name

website1 = Website("Google", "https://www.google.com", "Пошукова система та інтернет-компанія")
website2 = Website("Facebook", "https://www.facebook.com", "Соціальна мережа")


print(website1 < website2)
print(website1 <= website2)
print(website1 == website2)
print(website1 != website2)
print(website1 > website2)
print(website1 >= website2)


print(website1)
print(website2)
