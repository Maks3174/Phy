class TreeNode:
    def __init__(self, word, translations):
        self.word = word
        self.translations = translations
        self.left = None
        self.right = None
        self.count = 0

class Dictionary:
    def __init__(self):
        self.root = None
        self.popular_words = {}
        self.unpopular_words = {}

    def insert(self, word, translations):
        self.root = self._insert(self.root, word, translations)

    def _insert(self, node, word, translations):
        if node is None:
            return TreeNode(word, translations)
        if word < node.word:
            node.left = self._insert(node.left, word, translations)
        elif word > node.word:
            node.right = self._insert(node.right, word, translations)
        return node

    def search(self, word):
        return self._search(self.root, word)

    def _search(self, node, word):
        if node is None:
            return None
        if node.word == word:
            node.count += 1
            return node.translations
        if word < node.word:
            return self._search(node.left, word)
        return self._search(node.right, word)

    def add_translation(self, word, translation):
        translations = self.search(word)
        if translations is not None:
            translations.append(translation)

    def remove_translation(self, word, translation):
        translations = self.search(word)
        if translations is not None and translation in translations:
            translations.remove(translation)

    def add_word(self, word, translations):
        self.insert(word, translations)

    def remove_word(self, word):
        pass

    def display_top_words(self, n):
        sorted_words = sorted(self.popular_words.items(), key=lambda x: x[1], reverse=True)
        print(f"Топ-{n} найпопулярніших слів:")
        for i in range(min(n, len(sorted_words))):
            print(f"{i+1}. {sorted_words[i][0]} (кількість звернень: {sorted_words[i][1]})")

    def display_bottom_words(self, n):
        sorted_words = sorted(self.unpopular_words.items(), key=lambda x: x[1])
        print(f"Топ-{n} найнепопулярніших слів:")
        for i in range(min(n, len(sorted_words))):
            print(f"{i+1}. {sorted_words[i][0]} (кількість звернень: {sorted_words[i][1]})")

def main():
    dictionary = Dictionary()

    dictionary.add_word("apple", ["яблуко"])
    dictionary.add_word("banana", ["банан"])
    dictionary.add_word("cherry", ["вишня"])

    print("Переклад слова 'apple':", dictionary.search("apple"))
    print("Переклад слова 'banana':", dictionary.search("banana"))
    print("Переклад слова 'cherry':", dictionary.search("cherry"))
    print("Переклад слова 'grape':", dictionary.search("grape"))

    dictionary.add_translation("apple", "яблучко")
    print("Переклад слова 'apple' після додавання:", dictionary.search("apple"))
    dictionary.remove_translation("apple", "яблуко")
    print("Переклад слова 'apple' після видалення:", dictionary.search("apple"))

    dictionary.display_top_words(10)
    dictionary.display_bottom_words(10)

if __name__ == "__main__":
    main()
