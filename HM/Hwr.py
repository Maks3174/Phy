#1
def travel_to_stars(ship_speed):
    try:
        ship_speed = float(ship_speed)
    except ValueError:
        print("Помилка: введіть число для швидкості корабля.")
        return

    star_names = [
        "Proxima Centauri",
        "Alpha Centauri A",
        "Alpha Centauri B",
        "Barnard's Star",
        "Wolf 359"
    ]

    star_distances = [
        4.22,
        4.37,
        4.37,
        5.96,
        7.78
    ]

    star_distances = dict(zip(star_names, star_distances))

    for star, distance in star_distances.items():
        travel_time = distance * 946073047 * 1000 / (ship_speed * 3600)
        if travel_time > 10 * 365 * 24:
            required_speed = distance * 946073047 * 1000 / (10 * 365 * 24 * 3600)
            print(
                f"Рекомендація: Попрацюйте над кораблем. Для {star} потрібна швидкість більше {required_speed:.2f} км/год.")
        else:
            print(f"Час подорожі до {star}: {travel_time:.2f} годин")


ship_speed = input("Введіть швидкість корабля у км/год: ")
travel_to_stars(ship_speed)

#2
from datetime import datetime


def days_between_dates(date1, date2):
    try:
        date1_obj = datetime.strptime(date1, "%Y-%m-%d")
        date2_obj = datetime.strptime(date2, "%Y-%m-%d")

        delta = date2_obj - date1_obj

        return abs(delta.days)
    except ValueError:
        print("Помилка: невірний формат дати. Використовуйте формат YYYY-MM-DD.")


date1 = input("Введіть першу дату (у форматі YYYY-MM-DD): ")
date2 = input("Введіть другу дату (у форматі YYYY-MM-DD): ")

days = days_between_dates(date1, date2)
if days is not None:
    print("Кількість днів між датами:", days)

#3
hex_values = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

hex_value = input("Введіть символ у шістнадцятирічній системі: ")
decimal_value = hex_values.get(hex_value.upper(), -1)
print("Десяткове значення:", decimal_value)

decimal_number = int(input("Введіть десяткове число (від 0 до 15): "))
if 0 <= decimal_number <= 15:
    hex_values = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hex_value = hex_values.get(decimal_number)
    print("Шістнадцятирічне значення:", hex_value)
else:
    print("Помилка: Десяткове число має бути від 0 до 15")
