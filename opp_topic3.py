#1
class HotelManagementSystem:
    def __init__(self):
        self.__orders = {}

    def add_order(self, client, room_type, days, cost):
        order_id = len(self.__orders) + 1
        order = {"client": client, "room_type": room_type, "days": days, "cost": cost}
        self.__orders[order_id] = order

    def change_room_type(self, order_id, new_room_type):
        if order_id in self.__orders:
            self.__orders[order_id]["room_type"] = new_room_type
        else:
            print("Замовлення з вказаним ID не існує.")

    def change_days(self, order_id, new_days):
        if order_id in self.__orders:
            self.__orders[order_id]["days"] = new_days
        else:
            print("Замовлення з вказаним ID не існує.")

    def delete_order(self, order_id):
        if order_id in self.__orders:
            del self.__orders[order_id]
        else:
            print("Замовлення з вказаним ID не існує.")

    def display_orders(self):
        for order_id, order in self.__orders.items():
            print(f"Замовлення {order_id}:")
            print(f"Клієнт: {order['client']}")
            print(f"Тип кімнати: {order['room_type']}")
            print(f"Кількість днів: {order['days']}")
            print(f"Вартість: {order['cost']}\n")


hotel_system = HotelManagementSystem()

hotel_system.add_order("Іван", "Стандарт", 5, 1000)
hotel_system.add_order("Петро", "Люкс", 3, 2500)

hotel_system.change_room_type(1, "Полулюкс")
hotel_system.change_days(1, 7)

hotel_system.delete_order(2)

hotel_system.display_orders()


#2
class TaxiManagementSystem:
    def __init__(self):
        self.__orders = {}

    def add_order(self, client, address, car_type, cost):
        order_id = len(self.__orders) + 1
        order = {"client": client, "address": address, "car_type": car_type, "cost": cost}
        self.__orders[order_id] = order

    def change_address(self, order_id, new_address):
        if order_id in self.__orders:
            self.__orders[order_id]["address"] = new_address
        else:
            print("Замовлення з вказаним ID не існує.")

    def change_car_type(self, order_id, new_car_type):
        if order_id in self.__orders:
            self.__orders[order_id]["car_type"] = new_car_type
        else:
            print("Замовлення з вказаним ID не існує.")

    def delete_order(self, order_id):
        if order_id in self.__orders:
            del self.__orders[order_id]
        else:
            print("Замовлення з вказаним ID не існує.")

    def display_orders(self):
        for order_id, order in self.__orders.items():
            print(f"Замовлення {order_id}:")
            print(f"Клієнт: {order['client']}")
            print(f"Адреса: {order['address']}")
            print(f"Тип автомобіля: {order['car_type']}")
            print(f"Вартість: {order['cost']}\n")


taxi_system = TaxiManagementSystem()

taxi_system.add_order("Іван", "вул. Соборна, 10", "Легковий", 150)
taxi_system.add_order("Петро", "просп. Незалежності, 20", "Мінівен", 250)

taxi_system.change_address(1, "вул. Шевченка, 5")
taxi_system.change_car_type(1, "Мікроавтобус")

taxi_system.delete_order(2)

taxi_system.display_orders()
