import random
import string
#1
def multiples_word(list1, list2):
    return [x * y for x, y in zip(list1, list2)]

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

result = multiples_word(list1, list2)

print("Добуток пар чисел:", result)

def merge(str1, str2):
    return ''.join([x + y for x, y in zip(str1, str2)])

string1 = "critical "
string2 = "damage"

result_merge = merge(string1, string2)

print("Результат з'єднання рядків:", result_merge)

def compare_lists(list1, list2):
    different_indexes = [i for i, (x, y) in enumerate(zip(list1, list2)) if x != y]
    return different_indexes

list1 = [1, 2, 3, 4]
list2 = [1, 3, 3, 5]

result_indexes = compare_lists(list1, list2)

print("Індекси, де елементи списків відрізняються:", result_indexes)

def sum_columns(matrix):
    return [sum(column) for column in zip(*matrix)]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result_sum = sum_columns(matrix)

print("Сума елементів кожного стовпця в матриці:", result_sum)

#2
def password_generator(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = 10
password = password_generator(password_length)
print("Згенерований пароль:", password)

#3
def filter_by_condition(numbers, condition):
    filtered_numbers = []
    if condition == "even":
        filtered_numbers = [num for num in numbers if num % 2 == 0]
    elif condition == "odd":
        filtered_numbers = [num for num in numbers if num % 2 != 0]
    elif condition == "positive":
        filtered_numbers = [num for num in numbers if num > 0]
    return filtered_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = filter_by_condition(numbers, "even")
print("Парні числа:", even_numbers)

odd_numbers = filter_by_condition(numbers, "odd")
print("Непарні числа:", odd_numbers)

positive_numbers = filter_by_condition(numbers, "positive")
print("Позитивні числа:", positive_numbers)