#1
import random

random_numbers = [random.randint(10, 99) for i in range(10)]

even_numbers = [num for num in random_numbers if num % 2 == 0]
odd_numbers = [num for num in random_numbers if num % 2 != 0]

print("Випадковий список :", random_numbers)
print("Список парних чисел:", even_numbers)
print("Список непарних чисел:", odd_numbers)
print()

#2
numbers = [int(x) for x in input("Введіть список цілих чисел через пробіл: ").split()]

prime_count = sum(1 for num in numbers if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)))

print(f"Кількість простих чисел у списку: {prime_count}")
print()

#3
numbers = [int(x) for x in input("Введіть список цілих чисел через пробіл: ").split()]

min_threshold = int(input("Введіть мінімальний поріг: "))
max_threshold = int(input("Введіть максимальний поріг: "))

count_within_thresholds = sum(1 for num in numbers if min_threshold <= num < max_threshold)

print(f"Кількість елементів у списку, які більше або рівні {min_threshold} і менше {max_threshold}: {count_within_thresholds}")


