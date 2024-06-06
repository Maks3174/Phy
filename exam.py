#part 1
#1
num1 = int(input("Введіть перше ціле число: "))
num2 = int(input("Введіть друге ціле число: "))

start = min(num1, num2)
end = max(num1, num2)

sum_of_range = sum(range(start, end + 1))

print(f"Сума чисел в діапазоні дорівнює {sum_of_range}")

#2
sum_of_even_numbers = sum(range(2, 101, 2))

print(f"Сума всіх парних чисел від 1 до 100 дорівнює {sum_of_even_numbers}")

#3
user_string = input("Введіть рядок: ")

for char in user_string:
    print(char)

#4
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [number for number in original_list if number % 2 == 0]

print("Список парних чисел:", even_numbers)

#5
def filter_capitalized_strings(strings):
    return [string.strip() for string in strings if string and string.strip()[0].isupper()]

user_input = input("Введіть рядки, розділені комами: ")

input_list = user_input.split(",")

capitalized_strings = filter_capitalized_strings(input_list)

print("Рядки, що починаються з великої літери:", capitalized_strings)


#6
def filter_python_strings(strings):
    return [string for string in strings if 'Python' in string]

user_input = input("Введіть рядки, розділені комами: ")

input_list = [s.strip() for s in user_input.split(",")]

python_strings = filter_python_strings(input_list)

print("Рядки, які містять слово 'Python':", python_strings)

#7
def add_word(dictionary):
    word = input("Введіть слово: ").strip()
    definition = input("Введіть визначення: ").strip()
    dictionary[word] = definition
    print(f"Слово '{word}' додано з визначенням: '{definition}'")

def remove_word(dictionary):
    word = input("Введіть слово для видалення: ").strip()
    if word in dictionary:
        del dictionary[word]
        print(f"Слово '{word}' було видалено.")
    else:
        print(f"Слово '{word}' не знайдено у словнику.")

def search_word(dictionary):
    word = input("Введіть слово для пошуку: ").strip()
    if word in dictionary:
        print(f"Визначення слова '{word}': {dictionary[word]}")
    else:
        print(f"Слово '{word}' не знайдено у словнику.")

def display_menu():
    print("\nМеню:")
    print("1. Додати слово")
    print("2. Видалити слово")
    print("3. Знайти слово")
    print("4. Вийти")

def main():
    dictionary = {}
    while True:
        display_menu()
        choice = input("Виберіть опцію (1-4): ").strip()
        if choice == '1':
            add_word(dictionary)
        elif choice == '2':
            remove_word(dictionary)
        elif choice == '3':
            search_word(dictionary)
        elif choice == '4':
            print("Вихід з програми.")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()

#8
tuple_list = [(1, 3), (3, 2), (2, 1)]

sorted_list = sorted(tuple_list, key=lambda x: x[1])

print(sorted_list)

#part2
from datetime import datetime


class WebPage:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.publish_date = datetime.now()

    def display_details(self):
        print("Заголовок сторінки:", self.title)
        print("Вміст сторінки:", self.content)
        print("Дата публікації:", self.publish_date)


class WebSite:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.pages = []

    def add_page(self, title, content):
        page = WebPage(title, content)
        self.pages.append(page)
        print(f"Створено нову сторінку '{title}' на сайті '{self.name}'")

    def remove_page(self, title):
        for page in self.pages:
            if page.title == title:
                self.pages.remove(page)
                print(f"Сторінка '{title}' видалена з сайту '{self.name}'")
                return
        print(f"Сторінка '{title}' не знайдена на сайті '{self.name}'")

    def display_info(self):
        print("Інформація про сайт:")
        print("Назва сайту:", self.name)
        print("URL:", self.url)
        print("Список сторінок:")
        for page in self.pages:
            print("-" * 30)
            print("Заголовок:", page.title)
            print("Дата публікації:", page.publish_date)


def main():
    print("Ласкаво просимо до програми Симулятор роботи сайту!")
    website_name = input("Введіть назву сайту: ")
    website_url = input("Введіть URL сайту: ")
    website = WebSite(website_name, website_url)

    while True:
        print("\nМеню:")
        print("1. Додати нову сторінку")
        print("2. Видалити сторінку")
        print("3. Показати інформацію про сайт")
        print("4. Вийти")

        choice = input("Виберіть опцію (1-4): ")

        if choice == '1':
            title = input("Введіть заголовок нової сторінки: ")
            content = input("Введіть вміст нової сторінки: ")
            website.add_page(title, content)
        elif choice == '2':
            title = input("Введіть заголовок сторінки, яку бажаєте видалити: ")
            website.remove_page(title)
        elif choice == '3':
            website.display_info()
        elif choice == '4':
            print("Дякую за використання програми. До побачення!")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
