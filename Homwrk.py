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
