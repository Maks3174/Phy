#Ресторан
class OrderQueue:
    def __init__(self):
        self.queue = []

    def add_order(self, order):
        self.queue.append(order)
        print(f"Замовлення {order} додано до черги.")

    def process_order(self):
        if self.queue:
            processed_order = self.queue.pop(0)
            print(f"Замовлення {processed_order} оброблено.")
        else:
            print("Черга порожня. Немає замовлень для обробки.")

def main():
    order_queue = OrderQueue()

    while True:
        print("\nМеню:")
        print("1. Додати замовлення до черги")
        print("2. Обробити наступне замовлення")
        print("3. Вийти")
        choice = input("Оберіть операцію: ")

        if choice == '1':
            order = input("Введіть номер замовлення: ")
            order_queue.add_order(order)
        elif choice == '2':
            order_queue.process_order()
        elif choice == '3':
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()

#1
class CharQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def enqueue(self, char):
        if not self.is_full():
            self.queue.append(char)
            print(f"Символ '{char}' додано до черги.")
        else:
            print("Черга повна. Неможливо додати новий символ.")

    def dequeue(self):
        if not self.is_empty():
            char = self.queue.pop(0)
            print(f"Символ '{char}' видалено з черги.")
        else:
            print("Черга порожня. Неможливо видалити символ.")

    def show(self):
        if not self.is_empty():
            print("Елементи черги:", self.queue)
        else:
            print("Черга порожня.")

def main():
    max_size = int(input("Введіть максимальний розмір черги: "))
    queue = CharQueue(max_size)

    while True:
        print("\nМеню:")
        print("1. Перевірити, чи черга порожня")
        print("2. Перевірити, чи черга повна")
        print("3. Додати символ до черги")
        print("4. Видалити символ з черги")
        print("5. Відобразити всі елементи черги")
        print("6. Вийти")
        choice = input("Оберіть операцію: ")

        if choice == '1':
            if queue.is_empty():
                print("Черга порожня.")
            else:
                print("Черга не порожня.")
        elif choice == '2':
            if queue.is_full():
                print("Черга повна.")
            else:
                print("Черга не повна.")
        elif choice == '3':
            char = input("Введіть символ для додавання: ")
            queue.enqueue(char)
        elif choice == '4':
            queue.dequeue()
        elif choice == '5':
            queue.show()
        elif choice == '6':
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()

#2
class PriorityCharQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def insert_with_priority(self, char, priority):
        if not self.is_full():
            self.queue.append((char, priority))
            print(f"Символ '{char}' з пріоритетом {priority} додано до черги.")
        else:
            print("Черга повна. Неможливо додати новий символ з пріоритетом.")

    def pull_highest_priority_element(self):
        if not self.is_empty():
            highest_priority_element = max(self.queue, key=lambda x: x[1])
            self.queue.remove(highest_priority_element)
            print(f"Видалено елемент '{highest_priority_element[0]}' з найвищим пріоритетом {highest_priority_element[1]}.")
        else:
            print("Черга порожня. Неможливо видалити елемент.")

    def peek(self):
        if not self.is_empty():
            highest_priority_element = max(self.queue, key=lambda x: x[1])
            print(f"Елемент з найвищим пріоритетом: '{highest_priority_element[0]}' з пріоритетом {highest_priority_element[1]}.")
        else:
            print("Черга порожня. Немає елементів для перегляду.")

    def show(self):
        if not self.is_empty():
            print("Елементи черги з їх пріоритетами:")
            for char, priority in self.queue:
                print(f"Символ: '{char}', Пріоритет: {priority}")
        else:
            print("Черга порожня.")

def main():
    max_size = int(input("Введіть максимальний розмір черги: "))
    queue = PriorityCharQueue(max_size)

    while True:
        print("\nМеню:")
        print("1. Перевірити, чи черга порожня")
        print("2. Перевірити, чи черга повна")
        print("3. Додати символ з пріоритетом до черги")
        print("4. Видалити елемент з найвищим пріоритетом")
        print("5. Переглянути елемент з найвищим пріоритетом")
        print("6. Відобразити всі елементи черги")
        print("7. Вийти")
        choice = input("Оберіть операцію: ")

        if choice == '1':
            if queue.is_empty():
                print("Черга порожня.")
            else:
                print("Черга не порожня.")
        elif choice == '2':
            if queue.is_full():
                print("Черга повна.")
            else:
                print("Черга не повна.")
        elif choice == '3':
            char = input("Введіть символ для додавання: ")
            priority = int(input("Введіть пріоритет: "))
            queue.insert_with_priority(char, priority)
        elif choice == '4':
            queue.pull_highest_priority_element()
        elif choice == '5':
            queue.peek()
        elif choice == '6':
            queue.show()
        elif choice == '7':
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
