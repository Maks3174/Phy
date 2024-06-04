#1
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

x1 = float(input("Введіть х-координату першої точки: "))
y1 = float(input("Введіть y-координату першої точки: "))
x2 = float(input("Введіть х-координату другої точки: "))
y2 = float(input("Введіть y-координату другої точки: "))

result = distance(x1, y1, x2, y2)
print("Відстань між точками становить:", result)

print()
#2
def power(a, n):
    if a <= 0:
        raise ValueError("Число 'a' повинно бути додатнім.")

    result = 1
    for _ in range(n):
        result *= a
    return result


try:
    a = float(input("Введіть дійсне позитивне число a: "))
    n = int(input("Введіть ціле число n: "))
    print("Результат піднесення числа a до степеня n:", power(a, n))
except ValueError as ve:
    print(ve)
print()
#3
def calculate_factorials(lst):
    new_list = []
    for number in lst:
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        new_list.append(factorial)
    return new_list

input_list = input("Введіть список чисел, розділених пробілами: ").split()
number_list = [int(num) for num in input_list]

result = calculate_factorials(number_list)
print("Список факторіалів:", result)
print()
#4
def find_indices(lst, number):
    indices = []
    for index, element in enumerate(lst):
        if element == number:
            indices.append(index)
    return indices

input_list = input("Введіть список чисел, розділених пробілами: ").split()
number_list = [int(num) for num in input_list]

target_number = int(input("Введіть номер, який потрібно знайти в списку: "))

result = find_indices(number_list, target_number)
print("Індекси", target_number, "у списку:", result)
print()
#5
def remove_number(lst, number):
    count_removed = lst.count(number)
    while number in lst:
        lst.remove(number)
    return count_removed, lst

input_list = input("Введіть список чисел, розділених пробілами: ").split()
number_list = [int(num) for num in input_list]
target_number = int(input("Введіть номер, який потрібно видалити зі списку: "))

removed_count, new_list = remove_number(number_list, target_number)
print("Кількість видалених елементів:", removed_count)
print("Новий список без видалених елементів:", *new_list)
