#1
def sort_by_ids(ids, phones):
        sorted_data = sorted(zip(ids, phones), key=lambda x: x[0])
        return [x[0] for x in sorted_data], [x[1] for x in sorted_data]
def sort_by_phones(ids, phones):
    sorted_data = sorted(zip(phones, ids), key=lambda x: x[0])
    return [x[1] for x in sorted_data], [x[0] for x in sorted_data]

def display_contacts(ids, phones):
    print("Список користувачів:")
    for i in range(len(ids)):
        print(f"Код: {ids[i]}, Телефон: {phones[i]}")

def get_valid_id():
    while True:
        try:
            return int(input("Введіть ідентифікаційний код: "))
        except ValueError:
            print("Невірний формат. Будь ласка, введіть ціле число.")

def get_valid_phone():
    while True:
        phone = input("Введіть номер телефону (у форматі XXX-XXXX): ")
        if len(phone) == 8 and phone[:3].isdigit() and phone[4:].isdigit() and phone[3] == "-":
            return phone
        else:
            print("Невірний формат. Будь ласка, введіть у форматі XXX-XXXX.")

ids = [101, 102, 103, 104]
phones = ["555-1234", "555-5678", "555-9876", "555-4321"]

while True:
    print("\nМеню:")
    print("1. Відсортувати за ідентифікаційними кодами")
    print("2. Відсортувати за номерами телефонів")
    print("3. Вивести список користувачів з кодами та телефонами")
    print("4. Вихід")
    choice = input("Виберіть опцію: ")

    if choice == "1":
        ids, phones = sort_by_ids(ids, phones)
        print("Список відсортований за ідентифікаційними кодами.")
    elif choice == "2":
        ids, phones = sort_by_phones(ids, phones)
        print("Список відсортований за номерами телефонів.")
    elif choice == "3":
        display_contacts(ids, phones)
    elif choice == "4":
        print("Дякую за використання довідника!")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")

#2
def sort_by_title(books, years):
    sorted_data = sorted(zip(books, years), key=lambda x: x[0])
    return [x[0] for x in sorted_data], [x[1] for x in sorted_data]

def sort_by_year(books, years):
    sorted_data = sorted(zip(years, books), key=lambda x: x[0])
    return [x[1] for x in sorted_data], [x[0] for x in sorted_data]

def display_books(books, years):
    print("Список книг:")
    for i in range(len(books)):
        print(f"Назва: {books[i]}, Рік випуску: {years[i]}")

books = ["Війна і мир", "Майстер та Маргарита", "1984", "Під куполом"]
years = [1869, 1966, 1949, 2009]

while True:
    print("\nМеню:")
    print("1. Відсортувати за назвою книг")
    print("2. Відсортувати за роками випуску")
    print("3. Вивести список книг з назвами та роками випуску")
    print("4. Вихід")
    choice = input("Виберіть опцію: ")

    if choice == "1":
        books, years = sort_by_title(books, years)
        print("Список відсортований за назвою книг.")
    elif choice == "2":
        books, years = sort_by_year(books, years)
        print("Список відсортований за роками випуску.")
    elif choice == "3":
        display_books(books, years)
    elif choice == "4":
        print("Дякую за використання програми «Книги»!")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
