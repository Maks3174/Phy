import random
import threading
import time

#1
class RequestQueue:
    def __init__(self):
        self.queue = []

    def add_request(self, client_name, priority):
        self.queue.append((client_name, priority))

    def process_request(self):
        if self.queue:
            client_name, _ = self.queue.pop(0)
            return client_name
        else:
            return None

    def display_requests(self):
        if self.queue:
            print("Черга запитів:")
            for client_name, priority in self.queue:
                print(f"Клієнт: {client_name}, Пріоритет: {priority}")
        else:
            print("Черга запитів порожня.")

class StatisticsQueue:
    def __init__(self):
        self.queue = []

    def add_stat(self, client_name):
        self.queue.append((client_name, time.strftime("%Y-%m-%d %H:%M:%S")))

    def display_stats(self):
        if self.queue:
            print("Статистика запитів:")
            for client_name, time_processed in self.queue:
                print(f"Клієнт: {client_name}, Час обробки: {time_processed}")
        else:
            print("Статистика запитів порожня.")

def main():
    request_queue = RequestQueue()
    stats_queue = StatisticsQueue()

    while True:
        print("\nМеню:")
        print("1. Додати новий запит")
        print("2. Обробити наступний запит")
        print("3. Вивести чергу запитів")
        print("4. Вивести статистику запитів")
        print("5. Вийти")
        choice = input("Оберіть операцію: ")

        if choice == '1':
            client_name = input("Введіть ім'я клієнта: ")
            priority = int(input("Введіть пріоритет запиту: "))
            request_queue.add_request(client_name, priority)
            stats_queue.add_stat(client_name)
        elif choice == '2':
            processed_client = request_queue.process_request()
            if processed_client:
                print(f"Запит від клієнта {processed_client} оброблено.")
            else:
                print("Черга запитів порожня.")
        elif choice == '3':
            request_queue.display_requests()
        elif choice == '4':
            stats_queue.display_stats()
        elif choice == '5':
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()

#2
class Passenger:
    def __init__(self, id):
        self.id = id

class Boat:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            print(f"Пасажир {passenger.id} зайняв місце на катері.")
        else:
            print(f"Пасажир {passenger.id} не може зайняти місце, катер повний.")

class Dock:
    def __init__(self, boat_interval, max_passengers):
        self.boat_interval = boat_interval
        self.max_passengers = max_passengers
        self.passenger_queue = []
        self.boat_queue = []

    def generate_passenger(self):
        return Passenger(len(self.passenger_queue) + 1)

    def generate_boat(self):
        return Boat(random.randint(5, 10))

    def passenger_arrival(self):
        while True:
            time.sleep(random.uniform(0.5, 2.0))
            passenger = self.generate_passenger()
            self.passenger_queue.append(passenger)
            print(f"Пасажир {passenger.id} прибув на причал.")

    def boat_arrival(self):
        while True:
            time.sleep(random.uniform(3.0, 5.0))
            boat = self.generate_boat()
            self.boat_queue.append(boat)
            print(f"Катер {len(self.boat_queue)} прибув на причал.")

    def embark_passengers(self):
        while True:
            if self.passenger_queue and self.boat_queue:
                passenger = self.passenger_queue.pop(0)
                boat = self.boat_queue.pop(0)
                boat.add_passenger(passenger)
            time.sleep(self.boat_interval)

def main():
    dock = Dock(10, 20)

    passenger_thread = threading.Thread(target=dock.passenger_arrival)
    boat_thread = threading.Thread(target=dock.boat_arrival)
    embark_thread = threading.Thread(target=dock.embark_passengers)

    passenger_thread.start()
    boat_thread.start()
    embark_thread.start()

if __name__ == "__main__":
    main()
