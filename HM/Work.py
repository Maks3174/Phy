#1
def process_text(text):

    processed = '. '.join(sentence.capitalize() for sentence in text.split('. '))

    digit = sum(char.isdigit() for char in text)
    punctuation = sum(char in '.,;:?!' for char in text)
    exclamation = text.count('!')

    return processed, digit, punctuation, exclamation


input_text = "Це речення. Ще одне речення! І ще одне. 123 цифри. Розділові знаки: ,;:!?"
result_text, digit, punctuation, exclamation = process_text(input_text)

print("Змінений текст:")
print(result_text)

print(f"Кількість цифр у тексті: {digit}")
print(f"Кількість розділових знаків у тексті: {punctuation}")
print(f"Кількість знаків оклику у тексті: {exclamation}")
print()
#2
def count_words(input_string):

    words = input_string.split()

    word_count = len(words)

    return word_count

user_input = input("Введіть рядок: ")

result = count_words(user_input)
print(f"Кількість слів у рядку: {result}")
print()
#3
def sum_of_digits(input_string):
    digits = [int(char) for char in input_string if char.isdigit()]

    digits_sum = sum(digits)

    return digits_sum

input_string = "1a23&456e78uu9"

result = sum_of_digits(input_string)
print(f"Сума цифр у рядку: {result}")
print()
#4
def count_spaces(input_string):

    space_count = sum(1 for char in input_string if char.isspace())

    return space_count

input_string = "Дуже   багато   пробілів   між   словами"

result = count_spaces(input_string)
print(f"Кількість пробілів у рядку: {result}")

#5
#генератор паролю
import random
import string
s1 = string.ascii_letters
s2 = string.digits
s3 = string.punctuation
s = s1 + s2 + s3
password = ""
for _ in range(15):
    password += random.choice(s)
print(password)
#2 спосіб
password = ''.join(random.choice(s) for _ in range(15))
print(password)
#превірка складності паролю
if len(password) < 8:
    print("Пароль занадто короткий")
else:
    upper_found = False
    for char in password:
        if char.isupper():
            upper_found = True
            break
    if not upper_found:
        print("Пароль повинен містити як мінімум одну велику букву")

    lower_found = False
    for char in password:
        if char.islower():
            lower_found = True
            break
    if not lower_found:
        print("Пароль повинен містити як мінімум одну маленьку букву")

    digit_found = False
    for char in password:
        if char.isdigit():
            digit_found = True
            break
    if not digit_found:
        print("Пароль повинен містити як мінімум одну цифру")

    special_found = False
    for char in password:
        if char in string.punctuation:
            special_found = True
            break
    if not special_found:
        print("Пароль повинен містити як мінімум один спец. символ")

    if upper_found and lower_found and digit_found and special_found:
        print("Пароль ідеальний")