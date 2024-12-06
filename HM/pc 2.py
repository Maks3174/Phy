#1
def merge_lists(list1, list2, list3, list4):
    merged_list = []
    for lst in [list1, list2, list3, list4]:
        merged_list.extend(lst)
    return merged_list

def bubble_sort_asc(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

list1 = [int(x) for x in input("Введіть перший список чисел через пробіл: ").split()]
list2 = [int(x) for x in input("Введіть другий список чисел через пробіл: ").split()]
list3 = [int(x) for x in input("Введіть третій список чисел через пробіл: ").split()]
list4 = [int(x) for x in input("Введіть четвертий список чисел через пробіл: ").split()]
target = int(input("Введіть число для пошуку: "))

merged_list = merge_lists(list1, list2, list3, list4)

sort_order = input("Оберіть напрямок сортування (asc для зростання, desc для спадання): ")

if sort_order == "asc":
    bubble_sort_asc(merged_list)
elif sort_order == "desc":
    bubble_sort_desc(merged_list)

index = linear_search(merged_list, target)

print("Відсортований список:", merged_list)
if index != -1:
    print(f"Значення {target} знаходиться на позиції {index} у списку.")
else:
    print(f"Значення {target} не знайдено у списку.")

#2
def merge_lists(list1, list2, list3, list4):
    return list1 + list2 + list3 + list4

list1 = [int(x) for x in input("Введіть перший список чисел через пробіл: ").split()]
list2 = [int(x) for x in input("Введіть другий список чисел через пробіл: ").split()]
list3 = [int(x) for x in input("Введіть третій список чисел через пробіл: ").split()]
list4 = [int(x) for x in input("Введіть четвертий список чисел через пробіл: ").split()]
target = int(input("Введіть число для пошуку: "))

merged_list = merge_lists(list1, list2, list3, list4)

unique_elements = list(set(merged_list))

sort_order = input("Оберіть напрямок сортування (asc для зростання, desc для спадання): ")

if sort_order == "asc":
    unique_elements.sort()
elif sort_order == "desc":
    unique_elements.sort(reverse=True)

index = unique_elements.index(target) if target in unique_elements else -1

print("Відсортований список унікальних елементів:", unique_elements)
if index != -1:
    print(f"Значення {target} знаходиться на позиції {index} у списку.")
else:
    print(f"Значення {target} не знайдено у списку.")

#3
def linear_search(products, target_product):
    for product, price in products:
        if product == target_product:
            return price
    return None


def binary_search(products, target_price):
    found_prices = []
    for _, price in products:
        if price >= target_price:
            found_prices.append(price)
    return found_prices


products = [("apple", 10), ("banana", 15), ("orange", 12), ("grape", 20), ("kiwi", 8)]

target_product = input("Введіть назву продукту: ")

product_price = linear_search(products, target_product)
if product_price is not None:
    print(f"Вартість продукту '{target_product}': {product_price}")

    prices_above_target = binary_search(sorted(products, key=lambda x: x[1]), product_price)
    if prices_above_target:
        print(f"Продукти з ціною більше або рівної вартості продукту '{target_product}': {prices_above_target}")
    else:
        print(f"Немає продуктів з ціною більше або рівної вартості продукту '{target_product}'.")
else:
    print("Продукт не знайдено.")

