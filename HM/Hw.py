#1
first_num = int(input("Введіть перше число"))
end_num = int(input("Введіть друге число"))
print("Усі число діапазону:")
currect_num = first_num
while currect_num <= end_num:
    if currect_num % 7 == 0:
        print(currect_num)
    currect_num += 1

#2
first_num = int(input("Введіть перше число"))
end_num = int(input("Введіть друге число"))
print("Усі числа діапазону:")
currect_num = first_num
while currect_num <= end_num:
    print(currect_num, "\t", end="")
    currect_num += 1
print()
print("Усі числа діапазону за спаданням:")
currect_num = end_num
while currect_num >= first_num:
    print(currect_num, "\t", end="")
    currect_num -= 1
print()
print("Усі числа кратні 7:")
currect_num = first_num
while currect_num <= end_num:
    if currect_num % 7 == 0:
        print(currect_num)
    currect_num += 1
print()
multiple_of_5 = 0
currect_num = first_num
while currect_num <= end_num:
    if currect_num % 5 == 0:
        multiple_of_5 += 1
    currect_num += 1
print(f"Кількість чисел кратних 5:\n{multiple_of_5}")

#3
first_num = int(input("Введіть перше число"))
end_num = int(input("Введіть друге число"))
currect_num = first_num
while currect_num <= end_num:
    if currect_num % 3 == 0 and currect_num % 5 == 0:
        print("Fizz Buzz")
    elif currect_num % 3 == 0:
        print("Fizz")
    elif currect_num % 5 == 0:
        print("Buzz")
    else:
        print(currect_num)
    currect_num += 1