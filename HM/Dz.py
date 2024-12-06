from functools import reduce
#1
square_root = lambda x: x ** 0.5

rectangle_perimeter = lambda lenght, width: 2 * (lenght + width)

compare_strings = lambda str1, str2: len(str1) == len(str2)

format_name = lambda first_name, last_name: f"{last_name}, {first_name}"

check_even = lambda num: num % 2 == 0

print("Квадратний корінь числа 12:", square_root(12))
print("Периметр прямокутника зі сторонами 5 та 10:", rectangle_perimeter(5, 10))
print("Чи рівні за довжиною рядки 'hello' та 'world':", compare_strings('hello', 'world'))
print("Ім'я та прізвище у форматі 'Прізвище, Ім'я':", format_name('John', 'Doe'))
print("Чи є число 7 парним:", check_even(7))
print()
#2
def celsius_to_fahrenheit(celsium):
    return (celsium * 9/5) + 32

temperatures_celsius = [0, 10, 20, 30, 35]

temperatures_fahrenheit = list(map(celsius_to_fahrenheit, temperatures_celsius))

print("Температури у градусах Фаренгейта:", temperatures_fahrenheit)

words = ["coffee", "milk", "bread", "vegetables", "bathroom"]

reversed_words = list(map(lambda x: x[::-1], words))

print("Слова в зворотньому порядку:", reversed_words)
print()
#3
words = ["apple", "banana", "cherry", "date", "elderberry"]
start_letter = 'b'

filtered_words = list(filter(lambda x: x.startswith(start_letter), words))

print("Слова, які починаються на літеру", start_letter + ":", filtered_words)

numbers = [1, -2, 3, -4, 5, -6]
negative_numbers = list(filter(lambda x: x < 0, numbers))

print("Від'ємні числа:", negative_numbers)

sentences = ["The quick brown fox", "jumps over the lazy dog", "apple pie", "banana split"]
target_word = "apple"
filtered_sentences = list(filter(lambda x: target_word in x, sentences))

print("Рядки, які містять слово", target_word + ":", filtered_sentences)
print()
#4
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // reduce(lambda x, y: x * y, [a, b])

numbers = [12, 15]

result_lcm = reduce(lcm, numbers)

print("Найменше спільне кратне для чисел:", result_lcm)

numbers = [1, 2, 3, 4, 5]

square = lambda x: x**2

sum_of_squares = reduce(lambda x, y: x + y, map(square, numbers))

print("Сума квадратів чисел:", sum_of_squares)