#1
def list_operations():
    my_list = []

    def add_element():
        nonlocal my_list
        element = input("Введіть елемент для додавання до списку: ")
        my_list.append(element)
        print(f"Елемент {element} додано до списку.")

    def remove_element():
        nonlocal my_list
        element = input("Введіть елемент для видалення зі списку: ")
        if element in my_list:
            my_list.remove(element)
            print(f"Елемент {element} видалено зі списку.")
        else:
            print(f"Елемент {element} не знайдено у списку.")

    return add_element, remove_element

add_element, remove_element = list_operations()

add_element()
add_element()
remove_element()
remove_element()

#2
def sum_range(start, end):
    if start > end:
        return 0
    else:
        return start + sum_range(start + 1, end)

start = int(input("Введіть початкове значення діапазону: "))
end = int(input("Введіть кінцеве значення діапазону: "))

result = sum_range(start, end)
print("Сума чисел в заданому діапазоні:", result)

#3
def cache_decorator(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print("Використано кеш для аргументів:", args)
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return wrapper

@cache_decorator
def add(x, y):
    print("Виклик функції add")
    return x + y

x = int(input("Введіть перше число: "))
y = int(input("Введіть друге число: "))
print(add(x, y))

x = int(input("Введіть перше число: "))
y = int(input("Введіть друге число: "))
print(add(x, y))
