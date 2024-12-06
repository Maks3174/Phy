#1
import random

rows, colums = 5, 5

matrix = [[random.randint(1, 100) for _ in range(colums)] for _ in range(rows)]
print(*matrix)
result = sum(matrix[i][j] for i in range(2) for j in range(2)) / 4
print("Середнє арифметичне у кутах 2x2: ", result)

#2
people = 10
mounth = 12

salary = [[random.randint(15_000, 30_000) for _ in range(mounth)] for _ in range(people)]

print("Зарплати: ")
for row in salary:
    print(row)

selected_month = int(input("Введіть номер місяця (1-12): ")) - 1

total_salary = sum(row[selected_month] for row in salary)
print(f"Сумарна зарплата за обраний місяць: {total_salary}")

#3
from colorama import Fore, Back, Style, init

init(autoreset=True)

size = 7

matrix = [
    [
        (
            (Back.BLUE + ' ' + str(1) + ' ' + Back.RESET)
            if (i + j) % 2 == 0
            else (Back.YELLOW + ' ' + str(0) + ' ' + Back.RESET)
        )
        for j in range(size)
    ]
    for i in range(size)
]

for row in matrix:
    print(' '.join(row))

#
from colorama import Fore, Back, Style

def fill_and_print_matrix(n):
    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            matrix[i][j] = n - i

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                print(Fore.YELLOW + str(matrix[i][j]), end=' ')
            else:
                print(Fore.BLUE + str(matrix[i][j]), end=' ')
        print()

# Розмірність матриці
n = 7

# Заповнення та виведення матриці
fill_and_print_matrix(n)
