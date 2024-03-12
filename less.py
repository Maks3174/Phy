class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def display_info(self):
        print(f"Назва: {self.title}, Автор: {self.author}, Жанр: {self.genre}")

book1 = Book("Володар перснів", "Джон Роналд Руел Толкін", "фентезі")
book1.display_info()