#1
def calculate_factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * calculate_factorial(num - 1)

def calculate_series(n):
    sum = 1
    for i in range(1, n + 1):
        sum += 1 / calculate_factorial(i)
    return sum

n = int(input("Введіть значення n: "))
result = calculate_series(n)
print(f"Сума ряду для n = {n} дорівнює {result}")
#2
def calculate_digit_sum(number):
    return sum(map(int, str(number)))
def find_beatiful_num (start, end, target):
    b_numbers = []
    for num in range(start, end + 1):
        if calculate_digit_sum(num) == target:
            b_numbers.append(num)
    return  b_numbers
start_range = int(input("Введіть початок діапазону: "))
end_range = int(input("Введіть кінець діапазону: "))
target_digit_sum = int(input("Введіть суму цифр для пошуку: "))
result_number = find_beatiful_num(start_range, end_range, target_digit_sum)
print(f"Красиві числа в діапазоні від {start_range} до {end_range} з сумою цифр {target_digit_sum}: {result_number}")

#3
import  math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
def calculate_perimeter(coordinates):
    perimeter = 0

    for i in range(len(coordinates) - 1):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates [i + 1]
        perimeter += calculate_distance(x1, y1, x2, y2)

    x_first, y_first = coordinates[0]
    x_last, y_last = coordinates[-1]
    perimeter += calculate_distance(x_last, y_last, x_first, y_first)

    return perimeter

coordinates = []
while True:
    x_str = input("Введіть координату x (або залиште порожнім для завершення введення): ")
    if not x_str:
        break

    y_str = input("Введіть координату y: ")
    x = float(x_str)
    y = float(y_str)
    coordinates.append((x, y))

perimeter_result = calculate_perimeter(coordinates)
print(f"Периметр багатокутника: {perimeter_result}")