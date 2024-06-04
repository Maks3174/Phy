#1
def find_largest(n):
    largest_num = 0
    for number in range(n - 1, 0, -1):
        if number % 5 == 0 and number % 10 != 0:
            largest_num = number
            break
    return largest_num

n = int(input("Введіть натуральне число n: "))
result = find_largest(n)
print(f"Найбільше число менше {n}, кратне 5 і не кратне 10: {result}")
print()

#2
def fibonacci_sequence(n):
    sequence = [0, 1]

    while sequence[-1] + sequence[-2] <= n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence


def fibonacci_sum(n):
    fib_sequence = fibonacci_sequence(n)
    fib_sum = sum(fib_sequence)
    return fib_sum, fib_sequence


n = int(input("Введіть число n: "))

sum_result, sequence_result = fibonacci_sum(n)
print(f"Сума чисел Фібоначчі до {n}: {sum_result}")
print("Послідовність Фібоначчі:", sequence_result)
print()

#3
import math
def sin (x, iterations):
    result = 0
    for n in range(iterations):
        term = ((-1) ** n * (x ** (2 * n + 1)) / math.factorial(2 * n + 1))
        result += term
    return result

x = float(input("Введіть значення x в радіанах "))
iterations = int(input("Введіть кількість ітерацій: "))

sin_result = sin(x, iterations)
print(f"sin({x}) з використанням {iterations} ітерацій ряду Тейлора: {sin_result}")
print()

#4
import math
n = int(input("Введіть кількість ітерацій"))
e_approx = 1
factorial = 1
for i in range(1, n+1):
    factorial +=1
    e_approx += 1 / factorial
print(math.log(n))
print(e_approx)

#Додаткове
def avg(grades):
    total = sum(grades)
    return total / len(grades)

stud = int(input("Введіть кількість студентів: "))
practic = int(input("Введіть кількість практичних робіт: "))

grades_dict = {}
for student in range(1, stud + 1):
    student_grades = []
    print(f"\nСтудент{student}:")
    for practical in range(1, practic + 1):
        grade = float(input(f"Введіть оцінку за практичну роботу{practical}"))
        student_grades.append(grade)
        grades_dict[student] = student_grades

for student, grades in grades_dict.items():
    ave