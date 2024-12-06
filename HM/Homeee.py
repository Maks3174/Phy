from functools import reduce

sales_data = [
    ("Shop A", [100, 200, 150, 300]),
    ("Shop B", [50, 120, 80, 200]),
    ("Shop C", [200, 180, 160, 250])
]

shop_profits = map(lambda shop: (shop[0], sum(shop[1])), sales_data)

total_profit = reduce(lambda x, y: x + y, map(lambda shop: sum(shop[1]), sales_data))

profit_over_500 = filter(lambda shop: sum(shop[1]) > 500, sales_data)

average_profit = reduce(lambda x, y: x + y, map(lambda shop: sum(shop[1]), sales_data)) / len(sales_data)

print("Прибуток для кожного магазину:", list(shop_profits))
print("Загальний прибуток для всіх магазинів:", total_profit)
print("Магазини з прибутком більше 500:", list(profit_over_500))
print("Середній прибуток для всіх магазинів:", average_profit)