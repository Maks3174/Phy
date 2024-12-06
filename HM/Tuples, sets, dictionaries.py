#1
def common_element(t1, t2, t3):
    common = set(t1).intersection(t2, t3)
    return common

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
tuple3 = (5, 6, 7, 8, 9)

result = common_element(tuple1, tuple2, tuple3)
print(result)

#2
def unique_elements(t1, t2, t3):
    set1 = set(t1)
    set2 = set(t2)
    set3 = set(t3)

    unique_t1 = set1.difference(set2, set3)
    unique_t2 = set2.difference(set1, set3)
    unique_t3 = set3.difference(set1, set2)

    unique = unique_t1.union(unique_t2, unique_t3)

    return unique

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
tuple3 = (5, 6, 7, 8, 9)

result = unique_elements(tuple1, tuple2, tuple3)
print(result)

#3
def common_elements_at_same_position(t1, t2, t3):
    for item1, item2, item3 in zip(t1, t2, t3):
        if item1 == item2 == item3:
            yield item1

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (1, 2, 3, 4, 5)
tuple3 = (1, 2, 3, 4, 6)

result = list(common_elements_at_same_position(tuple1, tuple2, tuple3))
print(result)

#4
english_vowels = {'a', 'e', 'i', 'o', 'u'}
spanish_vowels = {'a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú'}

common_vowels = english_vowels.intersection(spanish_vowels)

print("Голосні, що присутні і в англійській, і в іспанській мовах:", common_vowels)

#5
def common_endings(words):
    endings = [word[-2:] for word in words]

    return set(endings)

words = ["apple", "banana", "orange", "pineapple"]
result = common_endings(words)
print("Унікальні закінчення:", result)
