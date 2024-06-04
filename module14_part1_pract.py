#1
import threading

def find_max(lst):
    max_val = max(lst)
    print(f"Максимум у списку: {max_val}")

def find_min(lst):
    min_val = min(lst)
    print(f"Мінімум у списку: {min_val}")

def main():
    user_input = input("Введіть значення через кому: ")
    lst = [int(x.strip()) for x in user_input.split(',')]

    max_thread = threading.Thread(target=find_max, args=(lst,))
    min_thread = threading.Thread(target=find_min, args=(lst,))

    max_thread.start()
    min_thread.start()

    max_thread.join()
    min_thread.join()

if __name__ == "__main__":
    main()

#2
def find_sum(lst):
    sum_val = sum(lst)
    print(f"Сума елементів у списку: {sum_val}")

def find_average(lst):
    avg_val = sum(lst) / len(lst)
    print(f"Середнє арифметичне у списку: {avg_val}")

def main():
    user_input = input("Введіть значення через кому: ")
    lst = [int(x.strip()) for x in user_input.split(',')]

    sum_thread = threading.Thread(target=find_sum, args=(lst,))
    avg_thread = threading.Thread(target=find_average, args=(lst,))

    sum_thread.start()
    avg_thread.start()

    sum_thread.join()
    avg_thread.join()

if __name__ == "__main__":
    main()


#3
import threading


# Функція для зчитування чисел з файлу та розділення їх на парні та непарні
def process_numbers(filename):
    even_numbers = []
    odd_numbers = []

    with open(filename, 'r') as f:
        numbers = [int(x.strip()) for x in f.readlines()]

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    # Створення нового файлу для парних чисел
    with open("even_numbers.txt", 'w') as f:
        f.write('\n'.join(map(str, even_numbers)))

    # Створення нового файлу для непарних чисел
    with open("odd_numbers.txt", 'w') as f:
        f.write('\n'.join(map(str, odd_numbers)))

    print(f"Кількість парних чисел: {len(even_numbers)}")
    print(f"Кількість непарних чисел: {len(odd_numbers)}")


def main():
    # Зчитуємо шлях до файлу з клавіатури
    filename = input("Введіть шлях до файлу: ")

    # Створюємо потік для обробки чисел
    process_thread = threading.Thread(target=process_numbers, args=(filename,))
    process_thread.start()
    process_thread.join()


if __name__ == "__main__":
    main()
