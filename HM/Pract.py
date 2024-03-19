# 1
with open('source_file.txt', 'r') as input_file:
    content = input_file.read()

words = content.split()

with open('new_file.txt', 'w') as output_file:
    filtered_words = [word for word in words if len(word) >= 7]

    output_file.write(' '.join(filtered_words))

#2
with open('source_file.txt', 'r') as input_file:
    lines = input_file.readlines()
with open('new_file.txt', 'w') as output_file:
    for line in lines:
        output_file.write(line)

#3
with open('source_file.txt', 'r') as input_file:
    lines = input_file.readlines()
    reversed_lines = reversed(lines)

with open('new_file.txt', 'w') as output_file:
    for line in reversed_lines:
        output_file.write(line)

#4
with open('source_file.txt', 'r') as input_file:
    lines = input_file.readlines()

indexes = [i for i, line in enumerate(lines) if ',' not in line]

if indexes:
    last_index = indexes[-1]
    lines.insert(last_index + 1, '\n************')
else:
    lines.append('************\n')

with open('new_file.txt', 'w') as output_file:
    output_file.writelines(lines)

#5
start_char = input("Введіть символ, з якого починаються слова: ")

with open('source_file.txt', 'r') as file:
    content = file.read()

    words = content.split()

    count = sum(1 for word in words if word.startswith(start_char))

print(f"Кількість слів, що починаються з символу '{start_char}': {count}")

#6
with open('source_file.txt', 'r') as input_file:
    lines = input_file.readlines()

with open('new_file.txt', 'w') as output_file:
    for line in lines:
        modified_line = line.replace('*', '&').replace('&', '*')
        output_file.write(modified_line)

#7
lines = [
    "Перший ",
    "Другий ",
    "Третій ",
    "Четвертий "
]

with open('source_file.txt', 'w') as file:
    for line in lines:
        file.write(line + '\n')


#8
with open('source_file.txt', 'r') as file:
    content = file.read()

num_characters = len(content)

print(f"Кількість символів у файлі: {num_characters}")

#9
with open('source_file.txt', 'r') as file:
    content = file.read()

num_characters = len(content)

print(f"Кількість символів у файлі: {num_characters}")
