import random

random_num = [random.randint(-50, 50) for _ in range(20)]
negative_sum = sum(x for x in random_num if x < 0)
even_sum = sum(x for x in random_num if x % 2 == 0)
odd_sum = sum(x for x in random_num if x %2 != 0)

product_index = 1
for i in range(0, len(random_num), 3):
    product_index *= random_num[i]

min_index = random_num.index(min(random_num))
max_index = random_num.index(max(random_num))
product_min_max = 1
for i in range(min(min_index, max_index) + 1, max(min_index, max_index)):
    product_min_max *= random_num[i]

first_positive_index = next((i for i, num in enumerate(random_num) if num > 0), None)

last_positive_index = next((i for i, num in enumerate(random_num[::-1]) if num > 0), None)

if first_positive_index is not None and last_positive_index is not None:
    last_positive_index = len(random_num) - last_positive_index - 1

    sum_between_positives = sum(random_num[first_positive_index + 1:last_positive_index])
else:
    print("У списку немає додатних чисел.")

print("Список випадкових чисел:", random_num)
print("Сума від'ємних чисел:", negative_sum)
print("Сума парних чисел:", even_sum)
print("Сума непарних чисел:", odd_sum)
print("Добуток елементів з індексами кратними 3:", product_index)
print("Добуток елементів між мінімальним і максимальним елементом:", product_min_max)
print("Сума елементів, що знаходяться між першим та останнім додатнім елементами:", sum_between_positives)

#2
import random
from colorama import Fore, Style, init

init(autoreset=True)


def display_board(board):
    for row in board:
        print(" ".join(row))


def make_guess(attempts_left):
    try:
        row = int(input("Введіть рядок (від 0 до 4): "))
        col = int(input("Введіть стовпчик (від 0 до 4): "))

        if not (0 <= row <= 4 and 0 <= col <= 4):
            raise ValueError("Невірні координати. Спробуйте ще раз.")

        return row, col
    except ValueError as e:
        print(Fore.RED + str(e) + Style.RESET_ALL)
        print(Fore.YELLOW + f"Залишилось спроб: {attempts_left}" + Style.RESET_ALL)
        return make_guess(attempts_left)


def play_game():
    board = [[Fore.GREEN + "O" + Style.RESET_ALL] * 5 for _ in range(5)]
    ship_row, ship_col = random.randint(0, 4), random.randint(0, 4)

    print("Відкрийте поле та вгадайте, де знаходиться корабель!")

    attempts = 3
    while attempts > 0:
        display_board(board)
        guess_row, guess_col = make_guess(attempts)

        if board[guess_row][guess_col] == Fore.RED + "X" + Style.RESET_ALL:
            print(Fore.YELLOW + "Вибрано вже відкриту клітину. Спробуйте ще раз." + Style.RESET_ALL)
            continue

        if guess_row == ship_row and guess_col == ship_col:
            print(Fore.BLUE + "Ви вразили корабель! Вітаємо з перемогою!" + Style.RESET_ALL)
            return

        distance = abs(ship_row - guess_row) + abs(ship_col - guess_col)
        if distance > 2:
            print("Холодно")
        elif distance == 2:
            print("Тепло")
        elif distance == 1:
            print("Гаряче")

        board[guess_row][guess_col] = Fore.RED + "X" + Style.RESET_ALL
        attempts -= 1

    print(Fore.RED + "Ви вичерпали всі спроби. Гра завершена." + Style.RESET_ALL)


play_game()
