class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def display_info(self):
        print(f"Назва: {self.title}, Автор: {self.author}, Жанр: {self.genre}")

    def __str__(self):
        return f"Книга: {self.title}, Автор: {self.author}, Жанр: {self.genre}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.genre == other.genre

    def __lt__(self, other):
        return self.title < other.title

    def __le__(self, other):
        return self.title <= other.title

    def __gt__(self, other):
        return self.title > other.title

    def __ge__(self, other):
        return self.title >= other.title

book1 = Book("Володар перснів", "Джон Роналд Руел Толкін", "фентезі")
book2 = Book("Гаррі Поттер і філософський камінь", "Джоан Роулінг", "фентезі")

print(book1 < book2)
print(book1 == book2)

print(book1)
print(book2)
