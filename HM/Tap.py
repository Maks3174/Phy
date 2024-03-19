current_number = 11

while current_number <= 29:
    current_number += 2
    print(current_number, )

#2
a = 1
while a <= 5:
    for i in range(5):
        print("*", end="")
        a += 1

#3
print()
size = 4
row = 1
while row <= size:
    col = 1
    while col <= row:
        print("*", end=" ")
        col += 1
    print()
    row += 1

print()
import time
def animated(total, width=30, symbol="\u2665"):
    print("Завантаження:")
    for i in range(total + 1):
        progress = int((i / total) * width)
        bar = symbol * progress + "-" * (width - progress)
        per = int((i / total) * 100)
        print(f"\r[{bar}] {per}%", end="", flush=True)
        time.sleep(0.1)

total_iterations = 40
animated(total_iterations)

#4
def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)

    for num in range(2, 101):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num*num, limit + 1, num):
                is_prime[multiple] = False

    for num in range(int(limit**0.5) + 1, limit + 1):
        if is_prime[num]:
            primes.append(num)

    return primes

primes_in_range = sieve_of_eratosthenes(100)
print("Прості числа в діапазоні від 2 до 100:", primes_in_range)
