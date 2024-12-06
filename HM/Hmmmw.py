#1
def greet_user():
    name = input("Введіть ваше ім'я: ")
    age = input("Введіть ваш вік: ")

    try:
        age = int(age)
        if age < 0 or age > 130:
            raise ValueError("Вік повинен бути від 0 до 130 років")
        else:
            print(f"Привіт, {name}! Твій вік — {age}")
    except ValueError as e:
        print(f"Помилка: {e}")

greet_user()

#2
def greet_user(name, age):
    if age < 0 or age > 130:
        raise ValueError("Вік повинен бути від 0 до 130 років")
    return f"Привіт, {name}! Твій вік — {age}"

name = input("Введіть ваше ім'я: ")
age = int(input("Введіть ваш вік: "))

try:
    greeting = greet_user(name, age)
    print(greeting)
except ValueError as e:
    print(f"Помилка: {e}")


def greet_user(name, age):
    try:
        if age < 0 or age > 130:
            raise ValueError("Вік повинен бути від 0 до 130 років")
        else:
            return f"Привіт, {name}! Твій вік — {age}"
    except ValueError as e:
        return f"Помилка: {e}"

name = input("Введіть ваше ім'я: ")
age = int(input("Введіть ваш вік: "))

greeting = greet_user(name, age)
print(greeting)


#3
def process_numbers(numbers):
    if any(num < 0 for num in numbers):
        raise ValueError("Знайдено від'ємне число в списку")
    else:
        return sum(numbers)

try:
    numbers = []
    while True:
        num = int(input("Введіть додатне число (або 0, щоб завершити): "))
        if num == 0:
            break
        numbers.append(num)

    result = process_numbers(numbers)
    print(f"Сума всіх чисел у списку: {result}")

except ValueError as e:
    print(f"Помилка: {e}")


#4
# Перша версія:
def sum_of_list(lst):
    return sum(lst)

try:
    numbers = [int(x) for x in input("Введіть числа через пробіл: ").split()]
    result = sum_of_list(numbers)
    print(f"Сума елементів списку: {result}")

except ValueError as e:
    print(f"Помилка: {e}")


# Друга версія:
def sum_of_list_v2(lst):
    try:
        return sum(lst)
    except TypeError:
        raise ValueError("Список містить недопустимі значення")

try:
    numbers = [int(x) for x in input("Введіть числа через пробіл: ").split()]
    result = sum_of_list_v2(numbers)
    print(f"Сума елементів списку: {result}")

except ValueError as e:
    print(f"Помилка: {e}")

