#1
def linear_search(numbers, target):
    if not target.isdigit():
        print("Помилка: Будь ласка, введіть ціле число.")
        return -1

    target = int(target)

    for i, num in enumerate(numbers):
        if num == target:
            return i

    return -1

numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
target_number = input("Введіть число для пошуку: ")

if not target_number:
    print("Помилка: Введіть, будь ласка, число.")
else:
    index = linear_search(numbers, target_number)
    if index != -1:
        print("Число знаходиться на позиції:", index)
    else:
        print("Число не знайдено у списку.")


#2
def binary_search(countries, target):
    if not target:
        print("Помилка: Введіть, будь ласка, назву країни для пошуку.")
        return -1

    left, right = 0, len(countries) - 1

    while left <= right:
        mid = (left + right) // 2
        if countries[mid].lower() == target.lower():
            return mid
        elif countries[mid].lower() < target.lower():
            left = mid + 1
        else:
            right = mid - 1

    return -1


countries = [
    "Australia", "Brazil", "Canada", "China", "France",
    "Germany", "India", "Italy", "Japan", "Mexico",
    "Netherlands", "Russia", "Saudi Arabia", "South Africa", "South Korea",
    "Spain", "Switzerland", "Taiwan", "Turkey", "Ukraine",
    "United Arab Emirates", "United Kingdom", "United States", "Vietnam", "Zimbabwe"
]

country = input("Введіть назву країни: ")

if country.lower() not in [c.lower() for c in countries]:
    print("Помилка: Введена країна не входить до списку відомих країн.")
else:
    index = binary_search(countries, country)
    if index != -1:
        print("Країна знаходиться на позиції:", index)
    else:
        print("Країну не знайдено в списку.")

#3
def linear_search(students, last_name):
    if not last_name:
        print("Помилка: Введіть, будь ласка, прізвище студента для пошуку.")
        return -1

    for i, student in enumerate(students):
        if student["last_name"].lower() == last_name.lower():
            return i
    return -1


students_list = [
    {"first_name": "John", "last_name": "Doe", "group": "A101"},
    {"first_name": "Jane", "last_name": "Smith", "group": "A102"},
    {"first_name": "Alice", "last_name": "Johnson", "group": "A103"},
]

search_last_name = input("Введіть прізвище студента: ")

index = linear_search(students_list, search_last_name)
if index != -1:
    print("Студент з прізвищем", search_last_name, "знаходиться на позиції:", index)
else:
    print("Студента з прізвищем", search_last_name, "не знайдено в списку.")
