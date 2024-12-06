#1Хід тури
def can_rook_move(start_column, start_row, end_column, end_row):
    if start_column == end_column or start_row == end_row:
        return "YES"
    else:
        return "NO"

start_column = int(input("Введіть стовбець для першої клітинки (від 1 до 8)"))
start_row = int(input("Введіть рядок для першої клітинки (від 1 до 8)"))
end_column = int(input("Введіть стовбець для другої клітинки (від 1 до 8)"))
end_row = int(input("Введіть рядок для другої клітинки (від 1 до 8)"))

result = can_rook_move(start_column, start_row, end_column, end_row)
print(result)

#2Шахова дошка
def same_color(column1, row1, column2, row2):
    color1 = (column1 + row1) % 2
    color2 = (column2 + row2) % 2

    return color1 == color2


column1 = int(input("Введіть стовпець для першої клітини (від 1 до 8): "))
row1 = int(input("Введіть рядок для першої клітини (від 1 до 8): "))
column2 = int(input("Введіть стовпець для другої клітини (від 1 до 8): "))
row2 = int(input("Введіть рядок для другої клітини (від 1 до 8): "))

if same_color(column1, row1, column2, row2):
    print("YES")
else:
    print("NO")

#3Ход короля
def move_possible(start_column, start_row, end_column, end_row):
    colum_diff = abs(start_column - end_column)
    row_diff = abs(start_row - end_row)
    return  colum_diff <= 1 and row_diff <= 1
start_column = int(input("Введіть стовпець для першої клітини (від 1 до 8): "))
start_row = int(input("Введіть рядок для першої клітини (від 1 до 8): "))
end_column = int(input("Введіть стовпець для другої клітини (від 1 до 8): "))
end_row = int(input("Введіть рядок для другої клітини (від 1 до 8): "))

result = move_possible(start_column, start_row, end_column, end_row)
if result:
    print("YES")
else:
    print("NO")

#5.Шоколадка
def break_chokolat(n, m, k):
    return k % n == 0 or k % m == 0

n = int(input("Введіть кількість рядків (n): "))
m = int(input("Введіть кількість стовпців (m): "))
k = int(input("Введіть необхідну кількість часточок (k): "))

result = break_chokolat(n, m, k)
if result:
    print("YES")
else:
    print("NO")

#6.Високосний рік
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("YES")
    else:
        print("No")

year = int(input("Введіть рік:"))
result = leap_year(year)
print(result)

#7
def min_distance_to_edge(N, M, x, y):
    min_to_long_edge = min(x, M - x)

    min_to_short_edge = min(y, N - y)

    min_distance = min(min_to_long_edge, min_to_short_edge)

    return min_distance

N = int(input("Введіть довжину басейну (N): "))
M = int(input("Введіть ширину басейну (M): "))
x = int(input("Введіть відстань до довгого борту (x): "))
y = int(input("Введіть відстань до короткого борту (y): "))

result = min_distance_to_edge(N, M, x, y)
print(result)
