#1
input_string = input("Введіть рядок: ")

positions = []

for index, char in enumerate(input_string):
    if char == 'a':
        positions.append(index)

if positions:
    print(f"Позиції символу 'a': {positions}")
else:
    print("Символ 'a' не знайдено у введеному рядку.")

#2
input_string = input("Введіть рядок: ")

words = input_string.split()

long_words = [word for word in words if len(word) > 5]

if long_words:
    print(f"Слова з довжиною більше 5 символів: {long_words}")
else:
    print("Немає слів з довжиною більше 5 символів у введеному рядку.")

#3
input_str1 = input("Введи перший рядок: ")
input_str2 = input("Тепер другий: ")

str1 = input_str1.lower()
str2 = input_str2.lower()

if sorted(str1) == sorted(str2):
    print("Ура! Це анаграма.")
else:
    print("Нажаль, це не анаграма. Спробуйте ще раз.")

#4
input_str = input("Введи рядок: ")

char_count = {}

for char in input_str:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

most_common_char = max(char_count, key=char_count.get)
count_of_most_common_char = char_count[most_common_char]

print(f"Найповторюваніший символ: {most_common_char}")
print(f"Кількість його повторень: {count_of_most_common_char}")