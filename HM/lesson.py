def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def divide_numbers():
    try:
        dividend = float(input("Enter the dividend: "))
        divisor = float(input("Enter the divisor: "))
        result = dividend / divisor
        print("Result:", result)

        if is_prime(int(result)):
            print("The result is a prime number!")
        else:
            print("The result is not a prime number.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")


divide_numbers()

#2
def divide_numbers(dividend, divisor):
    return dividend / divisor

try:
    dividend = float(input("Enter the dividend: "))
    divisor = float(input("Enter the divisor: "))
    result = divide_numbers(dividend, divisor)
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


def divide_numbers(dividend, divisor):
    try:
        result = dividend / divisor
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None

dividend = float(input("Enter the dividend: "))
divisor = float(input("Enter the divisor: "))
result = divide_numbers(dividend, divisor)
if result is not None:
    print("Result:", result)


#3
try:
    string_input = input("Enter a number: ")
    number = float(string_input)
    print("Number entered:", number)
except ValueError:
    print("Error: Could not convert the input to a number.")


#4
def try_convert_to_number(input_str):
    return float(input_str)

try:
    string_input = input("Enter a number: ")
    number = try_convert_to_number(string_input)
    print("Number entered:", number)
except ValueError:
    print("Error: Could not convert the input to a number.")


def try_convert_to_number(input_str):
    try:
        return float(input_str)
    except ValueError:
        print("Error: Could not convert the input to a number.")

string_input = input("Enter a number: ")
try_convert_to_number(string_input)
