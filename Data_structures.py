class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_element(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_element(self, data):
        if not self.head:
            print("Список порожній")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        print("Елемент не знайдено")

    def display_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def check_value(self, value):
        current = self.head
        while current:
            if current.data == value:
                print("Значення знайдено у списку")
                return
            current = current.next
        print("Значення не знайдено у списку")

    def replace_value(self, old_value, new_value):
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_value
                print("Значення змінено")
                return
            current = current.next
        print("Значення не знайдено у списку")

def main():
    linked_list = LinkedList()

    while True:
        print("\nМеню:")
        print("1. Додати елемент до списку")
        print("2. Видалити елемент зі списку")
        print("3. Показати вміст списку")
        print("4. Перевірити, чи є значення у списку")
        print("5. Замінити значення у списку")
        print("6. Вийти")
        choice = input("Оберіть опцію: ")

        if choice == '1':
            num = int(input("Введіть число для додавання: "))
            linked_list.add_element(num)
        elif choice == '2':
            num = int(input("Введіть число для видалення: "))
            linked_list.remove_element(num)
        elif choice == '3':
            print("Вміст списку:")
            linked_list.display_list()
        elif choice == '4':
            num = int(input("Введіть число для перевірки: "))
            linked_list.check_value(num)
        elif choice == '5':
            old_num = int(input("Введіть значення, яке потрібно замінити: "))
            new_num = int(input("Введіть нове значення: "))
            linked_list.replace_value(old_num, new_num)
        elif choice == '6':
            print("Удачі!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()


#2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_element(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_element(self, data):
        if not self.head:
            print("Список порожній")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        print("Елемент не знайдено")

    def display_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def check_value(self, value):
        current = self.head
        while current:
            if current.data == value:
                print("Значення знайдено у списку")
                return
            current = current.next
        print("Значення не знайдено у списку")

    def replace_value(self, old_value, new_value):
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_value
                print("Значення змінено")
                return
            current = current.next
        print("Значення не знайдено у списку")

def main():
    linked_list = LinkedList()

    while True:
        print("\nМеню:")
        print("1. Додати елемент до списку")
        print("2. Видалити елемент зі списку")
        print("3. Показати вміст списку")
        print("4. Перевірити, чи є значення у списку")
        print("5. Замінити значення у списку")
        print("6. Вийти")
        choice = input("Оберіть опцію: ")

        if choice == '1':
            num = int(input("Введіть число для додавання: "))
            linked_list.add_element(num)
        elif choice == '2':
            num = int(input("Введіть число для видалення: "))
            linked_list.remove_element(num)
        elif choice == '3':
            print("Вміст списку:")
            linked_list.display_list()
        elif choice == '4':
            num = int(input("Введіть число для перевірки: "))
            linked_list.check_value(num)
        elif choice == '5':
            old_num = int(input("Введіть значення, яке потрібно замінити: "))
            new_num = int(input("Введіть нове значення: "))
            linked_list.replace_value(old_num, new_num)
        elif choice == '6':
            print("Удачі!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()