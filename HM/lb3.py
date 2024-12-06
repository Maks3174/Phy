#1
def count_fruits(fruit_tuple, fruit_name):
    count = fruit_tuple.count(fruit_name)
    return count

fruits = ('apple', 'banana', 'orange', 'pear', 'apple', 'kiwi', 'apple', 'pineapple')
fruit_name = input("Enter the name of the fruit: ").lower()
fruit_count = count_fruits(fruits, fruit_name)
print("The number of", fruit_name, "fruits in the tuple:", fruit_count)

#2
def count_fruits(fruit_tuple, fruit_name):
    count = sum(1 for fruit in fruit_tuple if fruit_name in fruit)
    return count

fruits = ('apple', 'banana', 'orange', 'pear', 'apple', 'kiwi', 'apple', 'pineapple', 'bananamango', 'mango', 'strawberry-banana')
fruit_name = input("Enter the name of the fruit: ").lower()
fruit_count = count_fruits(fruits, fruit_name)
print("The number of", fruit_name, "fruits (including substrings) in the tuple:", fruit_count)

#3
def replace_manufacturer(manufacturer_tuple, manufacturer_name, replacement_word):
    replaced_tuple = tuple(replacement_word if manufacturer == manufacturer_name else manufacturer for manufacturer in manufacturer_tuple)
    return replaced_tuple

manufacturers = ('Toyota', 'Ford', 'Tesla', 'Ford', 'Ford', 'Tesla')
manufacturer_name = input("Enter the manufacturer name to replace: ").capitalize()
replacement_word = input("Enter the replacement word: ").capitalize()
replaced_manufacturers = replace_manufacturer(manufacturers, manufacturer_name, replacement_word)
print("Tuple after replacement:", replaced_manufacturers)


#4
def find_min_max():
    numbers = tuple(map(int, input("Введіть числа, розділені пробілами: ").split()))
    if not numbers:
        return None, None

    min_number = min(numbers)
    max_number = max(numbers)
    return min_number, max_number

min_max = find_min_max()
if min_max[0] is not None:
    print("Найменший елемент:", min_max[0])
    print("Найбільший елемент:", min_max[1])
else:
    print("Список чисел порожній.")


#5
def are_tuples_equal(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        return False

    for i in range(len(tuple1)):
        if tuple1[i] != tuple2[i]:
            return False

    return True

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
tuple3 = (4, 5, 6)

print(are_tuples_equal(tuple1, tuple2))
print(are_tuples_equal(tuple1, tuple3))

