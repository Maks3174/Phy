import math
#1
try:
    num = float(input("Введіть число: "))
    if num < 0:
        raise ValueError("Введене число повинно бути додатнім")

    square_root = math.sqrt(num)
    print("Квадратний корінь числа", num, "дорівнює", square_root)
except ValueError as ve:
    print("Помилка:", ve)

#2
def calculate_square_root(num):
    return math.sqrt(num)


try:
    number = float(input("Введіть число: "))
    if number < 0:
        raise ValueError("Введене число повинно бути додатнім")

    result = calculate_square_root(number)
    print("Квадратний корінь числа", number, "дорівнює", result)
except ValueError as ve:
    print("Помилка:", ve)


def calculate_square_root(num):
    if num < 0:
        raise ValueError("Введене число повинно бути додатнім")
    return math.sqrt(num)

try:
    number = float(input("Введіть число: "))
    result = calculate_square_root(number)
    print("Квадратний корінь числа", number, "дорівнює", result)
except ValueError as ve:
    print("Помилка:", ve)
#3
def display_menu():
    print("Меню:")
    print("1. Відображення словника")
    print("2. Пошук значення в словнику")
    print("3. Заміна значення в словнику за ключем")
    print("4. Відображення значення за введеним ключем")
    print("5. Видалення значення за введеним ключем")
    print("6. Вихід")

def display_dictionary(dictionary):
    print("Словник:")
    if dictionary:
        for key, value in dictionary.items():
            print(f"{key}: {value}")
    else:
        print("Словник порожній")

def search_value(dictionary, key):
    if key in dictionary:
        print(f"Значення для ключа '{key}': {dictionary[key]}")
    else:
        print("Помилка: вказаний ключ не знайдений у словнику")

def replace_value(dictionary, key, new_value):
    if key in dictionary:
        dictionary[key] = new_value
        print(f"Значення для ключа '{key}' замінено на '{new_value}'")
    else:
        print("Помилка: вказаний ключ не знайдений у словнику")

def display_value_by_key(dictionary):
    key = input("Введіть ключ для відображення його значення: ")
    search_value(dictionary, key)

def delete_value_by_key(dictionary):
    key = input("Введіть ключ для видалення його значення: ")
    if key in dictionary:
        del dictionary[key]
        print(f"Значення для ключа '{key}' видалено зі словника")
    else:
        print("Помилка: вказаний ключ не знайдений у словнику")

def main():
    user_dictionary = {}

    while True:
        display_menu()
        choice = input("Виберіть опцію: ")

        if choice == '1':
            display_dictionary(user_dictionary)
        elif choice == '2':
            key = input("Введіть ключ для пошуку його значення: ")
            search_value(user_dictionary, key)
        elif choice == '3':
            key = input("Введіть ключ для заміни його значення: ")
            new_value = input("Введіть нове значення: ")
            replace_value(user_dictionary, key, new_value)
        elif choice == '4':
            display_value_by_key(user_dictionary)
        elif choice == '5':
            delete_value_by_key(user_dictionary)
        elif choice == '6':
            print("Дякую за використання програми!")
            break
        else:
            print("Помилка: виберіть правильну опцію")

if __name__ == "__main__":
    main()
