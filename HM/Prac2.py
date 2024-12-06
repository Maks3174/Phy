#1
string1 = input("Введіть перший рядок: ")
string2 = input("Введіть другий рядок: ")

count = 0

if len(string1) < len(string2):
    for i in range(len(string2) - len(string1) + 1):
        if string2[i:i + len(string1)] == string1:
            count += 1

    print(f"Рядок '{string1}' входить у рядок '{string2}' {count} разів.")
else: print("Перший рядок не може входити у другий рядок")

#2
user_input = input("Введіть рядок: ")

words = user_input.split()

longest_word = ""
max_length = 0

if words:
    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)

    print(f"Найдовше слово: '{longest_word}', довжина: {max_length}")
else:
    print("Рядок порожній.")

#3
user_input = input("Введіть рядок: ")

words = user_input.split()

vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

for word in words:
    count_vowels = 0
    count_consonants = 0

    for char in word:
        if char in vowels:
            count_vowels += 1
        elif char in consonants:
            count_consonants += 1

    print(f"Слово: '{word}', Голосних: {count_vowels}, Приголосних: {count_consonants}")


#4
user_input = input("Введіть рядок: ")

vowels = set("aeiouAEIOU")

result = ''.join('*' if char in vowels else char for char in user_input)

print("Змінений рядок:", result)
