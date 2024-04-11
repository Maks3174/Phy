class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_number(self, number):
        if self.check_value(number):
            print("Це число вже є у списку.")
            return

        new_node = Node(number)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_number(self, number):
        if not self.head:
            print("Список порожній.")
            return

        if self.head.data == number:
            self.head = self.head.next
            return

        prev = None
        current = self.head
        while current and current.data != number:
            prev = current
            current = current.next

        if not current:
            print("Цього числа немає у списку.")
            return

        prev.next = current.next

    def show_list(self, reverse=False):
        if not self.head:
            print("Список порожній.")
            return

        numbers = []
        current = self.head
        while current:
            numbers.append(current.data)
            current = current.next

        if reverse:
            numbers.reverse()

        print("Список у зворотньому порядку:" if reverse else "Список у порядку:")
        for num in numbers:
            print(num)

    def check_value(self, value):
        if not self.head:
            return False

        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next

        return False

    def replace_value(self, old_value, new_value, replace_all=False):
        if not self.head:
            print("Список порожній.")
            return

        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_value
                if not replace_all:
                    return
            current = current.next


number_list = LinkedList()

while True:
    print("\nМеню:")
    print("1. Додати нове число до списку")
    print("2. Видалити усі входження числа зі списку")
    print("3. Показати вміст списку")
    print("4. Показати вміст списку у зворотньому порядку")
    print("5. Перевірити, чи є значення у списку")
    print("6. Замінити значення у списку")
    print("7. Вийти")

    choice = input("Виберіть дію: ")

    if choice == '1':
        number = int(input("Введіть число, яке потрібно додати до списку: "))
        number_list.add_number(number)
    elif choice == '2':
        number = int(input("Введіть число, яке потрібно видалити зі списку: "))
        number_list.remove_number(number)
    elif choice == '3':
        number_list.show_list()
    elif choice == '4':
        number_list.show_list(reverse=True)
    elif choice == '5':
        value = int(input("Введіть число для перевірки: "))
        if number_list.check_value(value):
            print("Це число є у списку.")
        else:
            print("Цього числа немає у списку.")
    elif choice == '6':
        old_value = int(input("Введіть значення, яке потрібно замінити: "))
        new_value = int(input("Введіть нове значення: "))
        replace_all = input("Замінити всі входження? (Так/Ні): ").lower() == 'так'
        number_list.replace_value(old_value, new_value, replace_all)
    elif choice == '7':
        print("Дякую за користування. Програма завершена.")
        break
    else:
        print("Неправильний вибір. Будь ласка, введіть число від 1 до 7.")
