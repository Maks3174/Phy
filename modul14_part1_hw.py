import threading
import random
import shutil
import os
import math
#1
numbers = []

def fill_list():
    global numbers
    numbers = [random.randint(1, 100) for _ in range(10)]
    print("Список заповнено: ", numbers)

def calculate_sum():
    global numbers
    sum_of_numbers = sum(numbers)
    print("Сума елементів списку: ", sum_of_numbers)

def calculate_average():
    global numbers
    average = sum(numbers) / len(numbers)
    print("Середнє арифметичне значення: ", average)

def main():
    thread_fill = threading.Thread(target=fill_list)
    thread_sum = threading.Thread(target=calculate_sum)
    thread_average = threading.Thread(target=calculate_average)

    thread_fill.start()
    thread_fill.join()

    thread_sum.start()
    thread_average.start()

if __name__ == "__main__":
    main()

#2


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def fill_file(filename, size):
    with open(filename, 'w') as f:
        for _ in range(size):
            f.write(str(random.randint(1, 1000)) + '\n')


def find_primes(filename, output_filename):
    primes = []
    with open(filename, 'r') as f:
        for line in f:
            number = int(line)
            if is_prime(number):
                primes.append(number)
    with open(output_filename, 'w') as f:
        for prime in primes:
            f.write(str(prime) + '\n')


def find_factorials(filename, output_filename):
    with open(filename, 'r') as f:
        factorials = [factorial(int(line)) for line in f]
    with open(output_filename, 'w') as f:
        for factorial_num in factorials:
            f.write(str(factorial_num) + '\n')


def main():
    filename = input("Введіть шлях до файлу: ")

    thread_fill = threading.Thread(target=fill_file, args=(filename, 10))
    thread_primes = threading.Thread(target=find_primes, args=(filename, "primes.txt"))
    thread_factorials = threading.Thread(target=find_factorials, args=(filename, "factorials.txt"))

    thread_fill.start()
    thread_fill.join()

    thread_primes.start()
    thread_factorials.start()

    thread_primes.join()
    thread_factorials.join()

    print("Статистика виконаних операцій:")
    print("Прості числа знайдено та записано у файл primes.txt")
    print("Факторіали знайдено та записано у файл factorials.txt")


if __name__ == "__main__":
    main()

#3
def copy_directory(source_dir, dest_dir):
    try:
        shutil.copytree(source_dir, dest_dir)
        print(f"Вміст директорії {source_dir} був успішно скопійований до {dest_dir}")
    except Exception as e:
        print(f"Під час копіювання виникла помилка: {str(e)}")

def main():
    source_dir = input("Введіть шлях до існуючої директорії: ")
    dest_dir = input("Введіть шлях до нової директорії: ")

    thread_copy = threading.Thread(target=copy_directory, args=(source_dir, dest_dir))
    thread_copy.start()
    thread_copy.join()

if __name__ == "__main__":
    main()


#4
def merge_files_with_word(source_dir, word, output_file):
    files_with_word = []

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                if word in f.read():
                    files_with_word.append(file_path)

    with open(output_file, 'w') as out_file:
        for file_path in files_with_word:
            with open(file_path, 'r') as f:
                out_file.write(f.read())

    return len(files_with_word)

def remove_banned_words(input_file, banned_words_file, output_file):
    with open(input_file, 'r') as in_file:
        content = in_file.read()

    with open(banned_words_file, 'r') as banned_file:
        banned_words = banned_file.read().splitlines()

    for banned_word in banned_words:
        content = content.replace(banned_word, "")

    with open(output_file, 'w') as out_file:
        out_file.write(content)

def main():
    source_dir = input("Введіть шлях до існуючої директорії: ")
    search_word = input("Введіть слово для пошуку: ")

    merged_file = "merged_files.txt"
    cleaned_file = "cleaned_file.txt"

    thread_merge = threading.Thread(target=merge_files_with_word, args=(source_dir, search_word, merged_file))
    thread_clean = threading.Thread(target=remove_banned_words, args=(merged_file, "banned_words.txt", cleaned_file))

    thread_merge.start()

    thread_merge.join()

    thread_clean.start()
    thread_clean.join()

    print("Статистика виконаних операцій:")
    print(f"Кількість знайдених файлів із словом '{search_word}': {thread_merge.result}")
    print("Вміст файлу був очищений від заборонених слів.")

if __name__ == "__main__":
    main()
