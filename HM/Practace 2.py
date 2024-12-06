#1
number = int(input("Введіть число: "))
suma = count = count_zero = 0
while number > 0:
    count += 1
    suma += number % 10
    if number % 10 == 0:
        count_zero += 1
    number //= 10
print(f"Кількість цифр {count}, нулів {count_zero} сума чисел {suma}")
#2
def print_chessboard(size):
    for i in range(size):
        row = ""
        for j in range(size):
            row += "***"
            if j < size - 1:
                row += "---"
        print(row)

if __name__ == "__main__":
    try:
        size = int(input("Введіть розмір клітинки шахівниці: "))
        print_chessboard(size)
    except ValueError:
        print("Будь ласка, введіть коректне ціле число.")
#3
import random


def generate_question(difficulty):
    if difficulty == 1:
        num1 = random.randint(2, 5)
        num2 = random.randint(2, 5)
    elif difficulty == 2:
        num1 = random.randint(6, 9)
        num2 = random.randint(6, 9)
    else:
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)

    return num1, num2


def ask_question(num1, num2):
    user_answer = int(input(f"Скільки буде {num1} * {num2}? "))
    return user_answer


def check_answer(num1, num2, user_answer):
    correct_answer = num1 * num2
    return user_answer == correct_answer


def run_quiz():
    try:
        difficulty = int(input("Виберіть рівень складності (1 - легкий, 2 - середній, 3 - складний): "))
        num_questions = int(input("Введіть кількість питань: "))

        if 1 <= difficulty <= 3:
            score = 0

            for _ in range(num_questions):
                num1, num2 = generate_question(difficulty)
                user_answer = ask_question(num1, num2)

                if check_answer(num1, num2, user_answer):
                    print("Правильно!")
                    score += 1
                else:
                    print(f"Неправильно. Правильна відповідь: {num1} * {num2} = {num1 * num2}")

            print(f"\nВаша оцінка: {score}/{num_questions}")
        else:
            print("Невірний рівень складності. Введіть число від 1 до 3.")
    except ValueError:
        print("Будь ласка, введіть коректне ціле число.")


if __name__ == "__main__":
    run_quiz()
#4
def print_romb(size):
    for i in range(size):
        print(" " * (size - i - 1) + "*" * (2 * i + 1))
    for i in range(size - 2, -1, -1):
        print(" " * (size - i - 1) + "*" * (2 * i + 1))

if __name__ == "__main__":
    try:
        size = int(input("Введіть розмір ромба: "))
        print_romb(size)
    except ValueError:
        print("Будь ласка, введіть коректне ціле число.")