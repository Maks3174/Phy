#1
size = int(input("Введіть розміри квадрата:"))
for i in range(size):
    print("*" * size)

#2
wigth = int(input("Введіть ширину прямокутника:"))
height = int(input("Введіть висоту прямокутника:"))
for i in range(height):
    print("*" * wigth)

#3
size = int(input("Введіть розмір сторони квадрата: "))

for i in range(size):
    if i == 0 or i == size - 1:
        print('* ' * size)
    else:
        print('*' + '  ' * (size - 2) + '*')
#4
length = int(input("Введіть довжину прямокутника: "))
width = int(input("Введіть ширину прямокутника: "))

for i in range(length):
    if i == 0 or i == length - 1:
        print('* ' * width)
    else:
        print('*' + '  ' * (width - 2) + '*')
