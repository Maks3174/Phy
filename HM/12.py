#1
start = int(input("Введіть початкове число: "))
end = int(input("Введіть кінцеве число: "))

sum = 0
count = 0

current_number = start
while current_number <= end:
    sum += current_number
    count += 1
    current_number += 1

average = sum / count

print("Сума чисел у діапазоні:", sum)
print("Середнє арифметичне:", average)
#2
number = int(input("Введіть число: "))

factorial = 1

current_number = 1
while current_number <= number:
    factorial *= current_number
    current_number += 1

print(f"Факторіал числа {number} = {factorial}")
#3
length = int(input("Введіть довжину лінії: "))

line = ""

current_position = 1
while current_position <= length:
    line += '*'
    current_position += 1

print(line)

#4
length = int(input("Введіть довжину лінії: "))
symbol = input("Введіть символ для заповнення лінії: ")

line = ""

current_position = 1
while current_position <= length:
    line += symbol
    current_position += 1

print(line)