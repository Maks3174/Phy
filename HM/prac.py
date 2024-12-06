def calculate_moon_weight(initial_weight, increase_rate, n):
    total_weight = initial_weight
    for year in range(1, n + 1):
        total_weight += increase_rate * year ** 2
    return total_weight


initial_weight = float(input("Введіть вашу початкову вагу: "))
increase_rate = float(input("Введіть швидкість збільшення ваги щороку: "))
n = int(input("Введіть кількість років: "))

result = calculate_moon_weight(initial_weight, increase_rate, n)
print("Ваша вага на Місяці через", n, "років буде:", result)
