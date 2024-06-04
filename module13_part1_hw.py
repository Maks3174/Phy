import pickle
import gzip

#1
def save_data(data, filename):
    with gzip.open(filename, 'wb') as f:
        pickle.dump(data, f)


def load_data(filename):
    with gzip.open(filename, 'rb') as f:
        data = pickle.load(f)
    return data


def add_country(data, country, capital):
    data[country] = capital


def delete_country(data, country):
    if country in data:
        del data[country]
        print(f"Країна {country} та її столиця були успішно видалені.")
    else:
        print(f"Країна {country} не знайдена у словнику.")


def search_country(data, country):
    if country in data:
        return data[country]
    else:
        return f"Країна {country} не знайдена у словнику."


def edit_country(data, country, new_capital):
    if country in data:
        data[country] = new_capital
        print(f"Назва столиці для країни {country} була змінена на {new_capital}.")
    else:
        print(f"Країна {country} не знайдена у словнику.")


def main():
    data = {}

    while True:
        print("\nМеню:")
        print("1. Завантаження даних")
        print("2. Збереження даних")
        print("3. Додавання країни та столиці")
        print("4. Видалення країни та столиці")
        print("5. Пошук столиці за назвою країни")
        print("6. Редагування столиці країни")
        print("7. Вихід")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            try:
                filename = input("Введіть ім'я файлу для завантаження: ")
                data = load_data(filename)
                print("Дані завантажено успішно.")
            except FileNotFoundError:
                print("Файл не знайдено.")
        elif choice == '2':
            try:
                filename = input("Введіть ім'я файлу для збереження: ")
                save_data(data, filename)
                print("Дані збережено успішно.")
            except Exception as e:
                print("Помилка під час збереження даних:", e)
        elif choice == '3':
            country = input("Введіть назву країни: ")
            capital = input("Введіть назву столиці: ")
            add_country(data, country, capital)
        elif choice == '4':
            country = input("Введіть назву країни, яку потрібно видалити: ")
            delete_country(data, country)
        elif choice == '5':
            country = input("Введіть назву країни: ")
            capital = search_country(data, country)
            print(f"Столиця країни {country}: {capital}")
        elif choice == '6':
            country = input("Введіть назву країни: ")
            new_capital = input("Введіть нову назву столиці: ")
            edit_country(data, country, new_capital)
        elif choice == '7':
            print("До побачення!")
            break
        else:
            print("Неправильний вибір. Будь ласка, виберіть опцію зі списку.")


if __name__ == "__main__":
    main()


#2
def save_data(data, filename):
    with gzip.open(filename, 'wb') as f:
        pickle.dump(data, f)


def load_data(filename):
    with gzip.open(filename, 'rb') as f:
        data = pickle.load(f)
    return data


def add_group(data, group, album):
    data[group] = album


def delete_group(data, group):
    if group in data:
        del data[group]
        print(f"Група {group} та її альбоми були успішно видалені.")
    else:
        print(f"Група {group} не знайдена у словнику.")


def search_group(data, group):
    if group in data:
        return data[group]
    else:
        return f"Група {group} не знайдена у словнику."


def edit_group(data, group, new_album):
    if group in data:
        data[group] = new_album
        print(f"Назва альбому для групи {group} була змінена на {new_album}.")
    else:
        print(f"Група {group} не знайдена у словнику.")


def main():
    data = {}

    while True:
        print("\nМеню:")
        print("1. Завантаження даних")
        print("2. Збереження даних")
        print("3. Додавання групи та альбому")
        print("4. Видалення групи та альбому")
        print("5. Пошук альбому за назвою групи")
        print("6. Редагування альбому групи")
        print("7. Вихід")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            try:
                filename = input("Введіть ім'я файлу для завантаження: ")
                data = load_data(filename)
                print("Дані завантажено успішно.")
            except FileNotFoundError:
                print("Файл не знайдено.")
        elif choice == '2':
            try:
                filename = input("Введіть ім'я файлу для збереження: ")
                save_data(data, filename)
                print("Дані збережено успішно.")
            except Exception as e:
                print("Помилка під час збереження даних:", e)
        elif choice == '3':
            group = input("Введіть назву групи: ")
            album = input("Введіть назву альбому: ")
            add_group(data, group, album)
        elif choice == '4':
            group = input("Введіть назву групи, яку потрібно видалити: ")
            delete_group(data, group)
        elif choice == '5':
            group = input("Введіть назву групи: ")
            album = search_group(data, group)
            print(f"Альбом групи {group}: {album}")
        elif choice == '6':
            group = input("Введіть назву групи: ")
            new_album = input("Введіть нову назву альбому: ")
            edit_group(data, group, new_album)
        elif choice == '7':
            print("До побачення!")
            break
        else:
            print("Неправильний вибір. Будь ласка, виберіть опцію зі списку.")


if __name__ == "__main__":
    main()
