#1
x = int(input("Введіть перше число: "))
y = int(input("Введіть друге число: "))

if x <= y:
    for i in range(x, y + 1):
        print(i)

else:
    print("Початкове число повинно бути менше або рівне кінцевому числу.")

#2
x = int(input("Введіть перше число: "))
y = int(input("Введіть друге число: "))

if x <= y:
    for i in range(x, y + 1):
        if i % 2 != 0:
            print(i)
else:
    print("Початкове число повинно бути менше або рівне кінцевому числу.")

#3
x = int(input("Введіть перше число: "))
y = int(input("Введіть друге число: "))

if x <= y:
    for i in range(x, y + 1):
        if i % 2 == 0:
            print(i)
else:
    print("Початкове число повинно бути менше або рівне кінцевому числу.")

#4
start_number = int(input("Введіть початкове число: "))
end_number = int(input("Введіть кінцеве число: "))

if start_number <= end_number:
    for i in range(end_number, start_number - 1, -1):
        print(i)
else:
    print("Початкове число повинно бути менше або рівне кінцевому числу.")
#5
x = int(input("Введіть початкове число: "))
y = int(input("Введіть кінцеве число: "))

if x > y:
    x, y = x, y
for i in range(x, y + 1):
    if i % 2 != 0:
        print(i)