#1
def read_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines

def compare_files(file1, file2):
    lines1 = read_file(file1)
    lines2 = read_file(file2)

    for line1, line2 in zip(lines1, lines2):
        if line1 != line2:
            print(f"Файл 1: {line1.strip()}")
            print(f"Файл 2: {line2.strip()}")

compare_files("file1.txt", "file2.txt")


#2
def count_statistics(file_name):
    char_count = 0
    line_count = 0
    vowel_count = 0
    consonant_count = 0
    digit_count = 0

    with open(file_name, 'r') as file:
        for line in file:
            char_count += len(line.strip())

            line_count += 1

            for char in line:
                if char.isalpha():
                    if char.lower() in "aeiou":
                        vowel_count += 1
                    else:
                        consonant_count += 1

                elif char.isdigit():
                    digit_count += 1

    return char_count, line_count, vowel_count, consonant_count, digit_count

statistics = count_statistics("input_file.txt")
print("Статистика:", statistics)


#3
def remove_last_line(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    modified_lines = lines[:-1]

    with open(output_file, 'w') as file:
        file.writelines(modified_lines)

remove_last_line("input_file.txt", "output_file.txt")

#4
def longest_line_length(file_name):
    max_length = 0
    with open(file_name, 'r') as file:
        for line in file:
            line_length = len(line.strip())
            if line_length > max_length:
                max_length = line_length
    return max_length

max_length = longest_line_length("input_file.txt")
print("Довжина найдовшого рядка:", max_length)

#5
def count_word_occurrences(file_name, word):
    count = 0
    with open(file_name, 'r') as file:
        for line in file:
            words = line.split()
            count += words.count(word)
    return count

search_word = input("Введіть слово для пошуку: ")

occurrences = count_word_occurrences("input_file.txt", search_word)
print(f"Кількість входжень слова '{search_word}': {occurrences}")

#6
def replace_word_in_file(input_file, output_file, old_word, new_word):
    with open(input_file, 'r') as file:
        text = file.read()

    modified_text = text.replace(old_word, new_word)

    with open(output_file, 'w') as file:
        file.write(modified_text)

old_word = input("Введіть слово, яке потрібно замінити: ")
new_word = input("Введіть слово, на яке потрібно замінити: ")

replace_word_in_file("input_file.txt", "output_file.txt", old_word, new_word)
