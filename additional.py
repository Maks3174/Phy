class ShoppingCart:
    def __init__(self):
        self.__items = {}

    def add_item(self, product, price, quantity=1):
        if product not in self.__items:
            self.__items[product] = {"price": price, "quantity": quantity}
        else:
            self.__items[product]["quantity"] += quantity

    def remove_item(self, product):
        if product in self.__items:
            self.__items[product]["quantity"] -= 1
            if self.__items[product]["quantity"] == 0:
                del self.__items[product]

    def total_price(self):
        total = 0
        for item in self.__items.values():
            total += item["price"] * item["quantity"]
        return total


cart = ShoppingCart()

cart.add_item("Молоко", 25, 2)
cart.add_item("Хліб", 15)
cart.add_item("Яйця", 10, 2)

cart.remove_item("Молоко")

print("Загальна вартість покупок:", cart.total_price())
