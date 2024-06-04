from itertools import permutations
#1
def product():
    numbers = input("Введіть числа через пробіл:").split()
    numbers = [int(num) for num in numbers]
    result = 1
    for num in numbers:
        result *= num
    return result

print("Добуток чисел:", product())

#2
def sort_words_by_length(*words):
    sorted_words = sorted(words, key=len)
    return sorted_words

result = sort_words_by_length("apple", "banana", "orange", "kiwi", "grapefruit")
print("Слова, відсортовані за довжиною:", result)

#3
def generate_anagrams(word):
    perms = permutations(word)
    anagrams = [''.join(perm) for perm in perms]
    return anagrams

word = input("Введіть слово: ")
result = generate_anagrams(word)
print("Усі можливі анаграми слова {}: {}".format(word, result))

#4
def find_numbers_with_odd_digits(*numbers):
    result = []
    for num in numbers:
        has_odd_digit = False
        for digit in str(num):
            if int(digit) % 2 != 0:
                has_odd_digit = True
                break
        if has_odd_digit:
            result.append(num)
    return result

numbers = [123, 456, 789, 2468, 13579]
result = find_numbers_with_odd_digits(*numbers)
print("Числа з непарними цифрами:", result)

#5
def find_anagrams(*args):
    anagrams = {}
    for word in args:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    return [(word1, word2) for words in anagrams.values() for word1 in words for word2 in words if word1 != word2]

strings = ["listen", "silent", "triangle", "integral", "debit card", "bad credit"]
print(find_anagrams(*strings))