#1
def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

try:
    num1 = int(input('Введіть перше додатнє ціле число: '))
    num2 = int(input('Введіть друге додатнє ціле число: '))

    if num1 <= 0 or num2 <= 0:
        raise ValueError('Введіть тільки додатні цілі числа.')

    gcd = find_gcd(num1, num2)
    print(f'Найбільший спільний дільник чисел {num1} і {num2} дорівнює: {gcd}')

except ValueError as ve:
    print(f'Помилка: {ve}')
except Exception as e:
    print(f'Непередбачена помилка: {e}')

#2



#3
#4