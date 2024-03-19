#1
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

n = len(matrix)
lower_right_sum = sum(matrix[i][j] for i in range(n//2, n) for j in range(n//2, n))
lower_left_sum = sum(matrix[i][j] for i in range(n//2, n) for j in range(n//2))
print("Сума елементів у правому нижньому куті:", lower_right_sum)
print("Сума елементів у лівому нижньому куті:", lower_left_sum)

#2
#2.1
from colorama import Fore, Back, Style

matrix = []

for i in range(7):
    row = []
    for j in range(7):
        if i == 0 or i == 6 or j == 0 or j == 6:
            row.append(Fore.BLUE + '1' + Style.RESET_ALL)
        else:
            row.append(Fore.YELLOW + '0' + Style.RESET_ALL)
    matrix.append(row)

for row in matrix:
    print(' '.join(row))
print()
#2.2
from colorama import Fore, Style

n = 7

matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i < n // 2:
            matrix[i][j] = i + 4
        else:
            matrix[i][j] = n - i + 3

color_map = {
    7: Fore.BLUE,
    6: Fore.BLUE,
    5: Fore.CYAN,
    4: Fore.YELLOW,
}

for row in matrix:
    for num in row:
        if num in color_map:
            print(color_map[num] + str(num), end=" ")
        else:
            print(num, end=" ")
    print(Style.RESET_ALL)
print()

#2.3
from colorama import Fore, Style

n = 7

matrix = [[1 if j >= i else 0 for j in range(n)] for i in range(n)]

for row in matrix:
    for element in row:
        if element == 1:
            print(Fore.BLUE + str(element), end=' ')
        else:
            print(Fore.YELLOW + str(element), end=' ')
    print(Style.RESET_ALL)
print()
#2.4
from colorama import Fore, Back, Style

color_mapping = {
    0: Fore.YELLOW + Style.BRIGHT,
    2: Fore.YELLOW + Style.BRIGHT,
    6: Fore.CYAN + Style.BRIGHT,
    8: Fore.CYAN + Style.BRIGHT,
    10: Fore.CYAN + Style.BRIGHT,
    12: Fore.BLUE + Style.BRIGHT,
    14: Fore.BLUE + Style.BRIGHT
}

matrix = [
    [2, 4, 6, 8, 10, 12, 14],
    [4, 6, 8, 10, 12, 14, 0],
    [6, 8, 10, 12, 14, 0, 0],
    [8, 10, 12, 14, 0, 0, 0],
    [10, 12, 14, 0, 0, 0, 0],
    [12, 14, 0, 0, 0, 0, 0],
    [14, 0, 0, 0, 0, 0, 0]
]

for row in matrix:
    for item in row:
        if item in color_mapping:
            print(color_mapping[item] + str(item), end=' ')
        else:
            print(str(item), end=' ')
    print(Style.RESET_ALL)
