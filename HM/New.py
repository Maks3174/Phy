#1
import random

matrix = [[random.randint(10, 99) for _ in range(50)] for _ in range(5)]

print("Двовимірний масив:")
for row in matrix:
    print(row)

max_value = max(max(row) for row in matrix)
max_indices = [(i, row.index(max_value)) for i, row in enumerate(matrix) if max_value in row][0]

print(f"\nІндекси першого входження максимального елемента ({max_value}):")
print(f"Номер рядка: {max_indices[0]}")
print(f"Номер стовпця: {max_indices[1]}")
print()
#2
n = int(input("Введіть кількість рядків (n): "))
m = int(input("Введіть кількість стовпців (m): "))

chessboard = [['.' if (i + j) % 2 == 0 else '*' for j in range(m)] for i in range(n)]

print("\nШаховий масив:")
for row in chessboard:
    print(' '.join(row))
print()

#3
n = int(input("Введіть розмір масиву n: "))

array = [[abs(i - j) for j in range(n)] for i in range(n)]

print("\nОтриманий масив:")
for row in array:
    print(row)

