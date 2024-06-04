#1
number = int(input("Введіть число: "))
if number % 2 == 0:
    print(f"{number} - Even number")
else:
    print(f"{number} - Odd number")
#2
num = int(input("Ведіть число"))
if num % 7 == 0:
    print(f"{number} - Number is multiple 7")
else:
    print(f"{number} - Number is not multiple 7")
#3
number1 = float(input("Введіть перше число: "))
number2 = float(input("Введіть друге число: "))
maximum = max(number1, number2)

print(f"Максимум із {number1} і {number2} - {maximum}")
#4
numbe1 = float(input("Введіть перше число: "))
numbe2 = float(input("Введіть друге число: "))
minimum = min(numbe1, numbe2)
print(f"Мінімум із {numbe1} і {numbe2} - {minimum}")
#5
number1 = float(input("Введіть перше число: "))
number2 = float(input("Введіть друге число: "))
operation = input("Виберіть операцію (+, -, *, /): ")
if operation == '+':
    result = number1 + number2
    print(f"Сума чисел {number1} і {number2} - {result}")
elif operation == '-':
    result = number1 - number2
    print(f"Різниця чисел {number1} і {number2} - {result}")
elif operation == '*':
    result = number1 * number2
    print(f"Добуток чисел {number1} і {number2} - {result}")
elif operation == '/':
    # Перевірка ділення на нуль
    if number2 != 0:
        result = number1 / number2
        print(f"Частка чисел {number1} і {number2} - {result}")
    else:
        print("Ділення на нуль неможливе.")
else:
    print("Невірна операція. Будь ласка, введіть +, -, *, або /.")