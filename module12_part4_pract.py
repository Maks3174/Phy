from fastrbtree import FastRBTree as RBTree

class Dictionary:
    def __init__(self):
        self.tree = RBTree()
        self.popularity_counter = RBTree()

    def add_word(self, word, translations):
        self.tree[word] = translations
        self.popularity_counter[word] = 0

    def get_translations(self, word):
        return self.tree.get(word)

    def update_translations(self, word, translations):
        if word in self.tree:
            self.tree[word] = translations
            print(f"Переклади слова '{word}' оновлено.")
        else:
            print(f"Слово '{word}' відсутнє у словнику.")

    def delete_word(self, word):
        if word in self.tree:
            del self.tree[word]
            del self.popularity_counter[word]
            print(f"Слово '{word}' видалено зі словника.")
        else:
            print(f"Слово '{word}' відсутнє у словнику.")

    def add_translation(self, word, translation):
        if word in self.tree:
            self.tree[word].append(translation)
            print(f"Переклад '{translation}' додано до слова '{word}'.")
        else:
            print(f"Слово '{word}' відсутнє у словнику.")

    def remove_translation(self, word, translation):
        if word in self.tree and translation in self.tree[word]:
            self.tree[word].remove(translation)
            print(f"Переклад '{translation}' видалено зі слова '{word}'.")
        else:
            print(f"Слово '{word}' або переклад '{translation}' відсутні у словнику.")

    def increment_popularity_counter(self, word):
        if word in self.popularity_counter:
            self.popularity_counter[word] += 1
        else:
            print(f"Слово '{word}' відсутнє у словнику.")

    def decrement_popularity_counter(self, word):
        if word in self.popularity_counter and self.popularity_counter[word] > 0:
            self.popularity_counter[word] -= 1
        else:
            print(f"Слово '{word}' відсутнє у словнику або лічильник популярності вже дорівнює 0.")

    def get_top_popular_words(self, n=10):
        return sorted(self.popularity_counter.items(), key=lambda x: x[1], reverse=True)[:n]

    def get_top_unpopular_words(self, n=10):
        return sorted(self.popularity_counter.items(), key=lambda x: x[1])[:n]

if __name__ == "__main__":
    dictionary = Dictionary()
    dictionary.add_word("apple", ["яблуко", "малина"])
    dictionary.add_word("banana", ["банан", "помаранч"])
    dictionary.add_word("carrot", ["морква", "картопля"])

    print("Словник:")
    print(dictionary.tree)

    print("\nПереклади слова 'apple':", dictionary.get_translations("apple"))

    dictionary.update_translations("banana", ["банан", "помаранч", "банановий сік"])
    print("\nОновлені переклади слова 'banana':", dictionary.get_translations("banana"))

    dictionary.delete_word("apple")
    print("\nСловник після видалення слова 'apple':")
    print(dictionary.tree)

    dictionary.add_translation("banana", "ананас")
    print("\nДоданий переклад 'ананас' до слова 'banana':", dictionary.get_translations("banana"))

    dictionary.remove_translation("banana", "помаранч")
    print("\nВидалений переклад 'помаранч' зі слова 'banana':", dictionary.get_translations("banana"))

    print("\nТоп-10 найпопулярніших слів:", dictionary.get_top_popular_words())
    print("\nТоп-10 найнепопулярніших слів:", dictionary.get_top_unpopular_words())

    dictionary.increment_popularity_counter("banana")
    print("\nТоп-10 найпопулярніших слів після збільшення популярності слова 'banana':", dictionary.get_top_popular_words())

    dictionary.decrement_popularity_counter("banana")
    print("\nТоп-10 найпопулярніших слів після зменшення популярності слова 'banana':", dictionary.get_top_popular_words())
