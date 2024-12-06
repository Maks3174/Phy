num1 = int(input("Введіть перше ціле число"))
num2 = int(input("Введіть друге ціле число"))
num3 = int(input("Введіть третю ціле число"))

if (num1 + num2 == 0) or (num1 + num3 == 0) or (num2 + num3 == 0):
    print("Є взаємно протилежні")
else:
    print("Взаємно протилежних пар не знайдено.")

x1, y1 = map(float, input("Введіть координати вершини 1 (x1 y1): ").split())
x2, y2 = map(float, input("Введіть координати вершини 2 (x2 y2): ").split())
x3, y3 = map(float, input("Введіть координати вершини 3 (x3 y3): ").split())
x4, y4 = map(float, input("Введіть координати вершини 4 (x4 y4): ").split())

# Перевірка, чи є чотирикутник паралелограмом
is_parallelogram = (x2 - x1, y2 - y1) == (x3 - x4, y3 - y4) and (x3 - x2, y3 - y2) == (x4 - x1, y4 - y1)

# Виведення результату
if is_parallelogram:
    print("Чотирикутник є паралелограмом.")
else:
    print("Чотирикутник не є паралелограмом.")



x1, y1 = map(float, input("Введіть координати вершини 1 (x1 y1)").split())
x2, y2 = map(float, input("Введіть координати вершини 1 (x2 y2)").split())
x3, y3 = map(float, input("Введіть координати вершини 1 (x3 y3)").split())
x4, y4 = map(float, input("Введіть координати вершини 1 (x4 y4)").split())

is_parallelogram = (x2 - x1, y2 - y1) == (x3 - x4, y3 - y4) and (x3 -x2, y3 - y2) == (x4 - x1, y4 - y1)

if is_parallelogram:
    print("Чотирикутник є паралелограмом.")
else:
    print("Чотирикутник не є паралелограмом")