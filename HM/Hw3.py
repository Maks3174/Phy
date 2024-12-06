#1
def calculate(x, y):
    result = x ** y
    return result

if __name__ == "__main__":
    try:
        x = int(input("Введіть ціле число x: "))
        y = int(input("Введіть ціле число y: "))

        result = calculate(x, y)
        print(f"{x} до степеня {y} дорівнює {result}")
    except ValueError:
        print("Введіть цілі числа.")

#2
ans = 0
for i in range(100, 1000):
    a, b, c = str(i)
    if a == b or a == c or b == c:
        ans += 1

print(f"Кількість цілих чисел в яких є дві однакові цифри: {ans} ")
#3
count = 0
for num in range(100, 10000):
    digits = set(str(num))
    if len(digits) == len(str(num)):
        count += 1
print(f"Кількість цілих чисел в яких усі цифри різні: {count} ")
#4
number = input("Введіть ціле число: ")
filtered_number = (''.join([c for c in number if c != '3' and c != '6']))
print(f"Число без '3' і '6': {filtered_number}")
