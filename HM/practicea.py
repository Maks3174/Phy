#1
def user_id_generator():
    count = 0

    def generate_id(name):
        nonlocal count
        count += 1
        return f"{name}_{count}"

    return generate_id

generate_user_id = user_id_generator()
print(generate_user_id("John"))
print(generate_user_id("Bob"))
print(generate_user_id("Maks"))

#2
def arithmetic_calculator():
    history = []

    def calculate(num1, operator, num2):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "Division by zero is not allowed."
            else:
                return num1 / num2

    def undo():
        if history:
            history.pop()
            print("Last operation undone.")
        else:
            print("History is empty.")

    while True:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        result = calculate(num1, operator, num2)
        print("Result:", result)

        history.append((num1, operator, num2, result))

        option = input("Do you want to undo the last operation? (yes/no): ").lower()
        if option == 'yes':
            undo()

        exit_option = input("Do you want to exit? (yes/no): ").lower()
        if exit_option == 'yes':
            break

arithmetic_calculator()

#3
def sum_of_digits(number):
    if number < 10:
        return number
    else:
        return number % 10 + sum_of_digits(number // 10)

# Функція для генерації піраміди з зірочок
def pyramid(rows, count=1):
    if count > rows:
        return
    else:
        print(" " * (rows - count) + "* " * count)
        pyramid(rows, count + 1)

# Приклад використання функцій
number = 12345
print("Sum of digits in", number, "is:", sum_of_digits(number))

print("\nPyramid:")
pyramid(5)