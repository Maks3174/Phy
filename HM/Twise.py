#1
time_in_seconds = int(input("Введіть час у секундах, який минув з початку дня: "))

if time_in_seconds < 0 or time_in_seconds >= 24 * 3600:
    print("Некоректний ввід часу.")
else:
    operation = input("Виберіть операцію (години, хвилини, секунди): ")

    remaining_seconds = 24 * 3600 - time_in_seconds

    remaining_hours = remaining_seconds // 3600
    remaining_minutes = (remaining_seconds % 3600) // 60
    remaining_seconds = remaining_seconds % 60

    if operation == 'години':
        print(f"Залишилося {remaining_hours} годин до півночі.")
    elif operation == 'хвилини':
        print(f"Залишилося {remaining_minutes} хвилин до півночі.")
    elif operation == 'секунди':
        print(f"Залишилося {remaining_seconds} секунд до півночі.")
    else:
        print("Невірна операція. Будь ласка, введіть години, хвилини або секунди.")
#2
import math

diameter = float(input("Введіть діаметр кола: "))

operation = input("Виберіть операцію (площа або периметр): ")

radius = diameter / 2

area = math.pi * radius**2
perimeter = 2 * math.pi * radius

if operation == 'площа':
    print(f"Площа кола з діаметром {diameter} - {area}")
elif operation == 'периметр':
    print(f"Периметр кола з діаметром {diameter} - {perimeter}")
else:
    print("Невірна операція. Будь ласка, введіть 'площа' або 'периметр'.")
#3
cost_per_console = float(input("Введіть вартість однієї ігрової приставки: "))
quantity = int(input("Введіть кількість ігрових приставок: "))
discount_percentage = float(input("Введіть відсоток знижки: "))

total_cost = cost_per_console * quantity
discount_amount = (discount_percentage / 100) * total_cost
final_cost = total_cost - discount_amount

operation = input("Виберіть операцію (загальна сума або вартість однієї приставки): ")

if operation == 'загальна сума':
    print(f"Загальна сума замовлення: {final_cost}")
elif operation == 'вартість однієї приставки':
    print(f"Вартість однієї приставки з урахуванням знижки: {final_cost / quantity}")
else:
    print("Невірна операція. Будь ласка, введіть 'загальна сума' або 'вартість однієї приставки'.")
#4
file_size_gb = float(input("Введіть розмір файлу в гігабайтах: "))
internet_speed_bps = float(input("Введіть швидкість інтернет-з'єднання в бітах за секунду: "))

file_size_bits = file_size_gb * 8 * 1024**3

time_seconds = file_size_bits / internet_speed_bps
time_minutes = time_seconds / 60
time_hours = time_minutes / 60

operation = input("Виберіть операцію (години, хвилини або секунди): ")

if operation == 'години':
    print(f"Час завантаження файлу: {time_hours:.2f} годин")
elif operation == 'хвилини':
    print(f"Час завантаження файлу: {time_minutes:.2f} хвилин")
elif operation == 'секунди':
    print(f"Час завантаження файлу: {time_seconds:.2f} секунд")
else:
    print("Невірна операція. Будь ласка, введіть 'години', 'хвилини' або 'секунди'.")
#5
hours = int(input("Введіть кількість годин: "))

if 0 <= hours < 6:
    print("Good Night")
elif 6 <= hours < 13:
    print("Good Morning")
elif 13 <= hours < 17:
    print("Good Day")
elif 17 <= hours < 24:
    print("Good Evening")
else:
    print("Невірне введення. Введіть число від 0 до 23.")