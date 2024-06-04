#1
number1 = float(input("Введіть перше число: "))
number2 = float(input("Введіть друге число: "))
number3 = float(input("Введіть третє число: "))

operation = input("Виберіть операцію (+ для суми, * для добутку, ** для ): ")

if operation == '+':
    result = number1 + number2 + number3
    print(f"Сума трьох чисел: {result}")
elif operation == '*':
    result = number1 * number2 * number3
    print(f"Добуток трьох чисел: {result}")
else:
    print("Невірна операція. Введіть '+' для суми або '*' для добутку.")

#2
number1 = float(input("Введіть перше число"))
number2 = float(input("Введіть друге число"))
number3 = float(input("Введіть третє число"))
operation = input("Виберіть операцію (min, max, avg): ")
if operation == "max":
    result = max(number1, number2, number3)
    print(f"Максимум із трьох чисел: {result}")
elif operation == "min":
    result = min(number1, number2, number3)
    print(f"Мінімум із трьох чисел: {result}")
elif operation == "avg":
    result = (number1 + number2 + number3) / 3
    print(f"Середнє арифметичне трьох чисел:{result}")
else:
    print("Невірна операція.Введіть 'max' для максимуму, 'min' для мінімуму або 'avg' для середнього арифметичного.")
#3
meters = float(input("Введіть кількість метрів: "))

operation = input("Виберіть операцію (милі, дюйми або ярди): ")

miles_conversion = 0.000621371
inches_conversion = 39.3701
yards_conversion = 1.09361

if operation == 'милі':
    result = meters * miles_conversion
    print(f"{meters} метрів = {result} миль")
elif operation == 'дюйми':
    result = meters * inches_conversion
    print(f"{meters} метрів = {result} дюймів")
elif operation == 'ярди':
    result = meters * yards_conversion
    print(f"{meters} метрів = {result} ярдів")
else:
    print("Невірна операція. Введіть 'милі', 'дюйми' або 'ярди' для конвертації.")