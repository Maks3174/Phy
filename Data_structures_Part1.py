class NumberList:
    def __init__(self):
        self.numbers = set()

    def add_number(self, number):
        if number not in self.numbers:
            self.numbers.add(number)
        else:
            print("Це число вже є у списку.")

    def remove_number(self, number):
        self.numbers.discard(number)

    def show_list(self, reverse=False):
        numbers = list(self.numbers)
        if reverse:
            numbers.reverse()
        print("Список у зворотньому порядку:" if reverse else "Список у порядку:")
        for num in numbers:
            print(num)

    def check_value(self, value):
        if value in self.numbers:
            print("Це число є у списку.")
        else:
            print("Цього числа немає у списку.")

    def replace_value(self, old_value, new_value, replace_all=False):
        if replace_all:
            self.numbers = {new_value if num == old_value else num for num in self.numbers}
        elif old_value in self.numbers:
            self.numbers.remove(old_value)
            self.numbers.add(new_value)
        else:
            print("Цього числа немає у списку.")


number_list = NumberList()

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
        number_list.check_value(value)
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
