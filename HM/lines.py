import random

list1 = [random.randint(1, 10) for i in range (5)]
list2 = [random.randint(1, 10) for i in range (5)]

list3 = list1 + list2

unique_elements = list(set(list3))

common_elements = list(set(list1) & set(list2))

unique_list1 = list(set(list1) - set(list2))
unique_list2 = list(set(list2) - set(list1))


min_max_list = [min(list1), max(list1), min(list2), max(list2)]

print("Список 1: ", list1)
print("Список 2: ", list2)
print("Елементи обох списків", list3)
print("Елементи обох списків без повторень:", unique_elements)
print("Елементи, спільні для двох списків:", common_elements)
print("Тільки унікальні елементи першого списку:", unique_list1)
print("Тільки унікальні елементи другого списку:", unique_list2)
print("Тільки мінімальне та максимальне значення кожного зі списків:", min_max_list)