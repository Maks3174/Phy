#1
def compress_and_save(data, filename):
    with open(filename, 'w') as file:
        compressed_data = ' '.join(map(str, data))
        file.write(compressed_data)

def load_from_file(filename):
    with open(filename, 'r') as file:
        data = file.read().split()
        return [int(item) for item in data]

def main():
    data = list(map(int, input("Введіть список цілих чисел через пробіл: ").split()))

    filename = "compressed_data.txt"

    compress_and_save(data, filename)
    print("Дані успішно збережено у файлі.")

    loaded_data = load_from_file(filename)
    print("Дані успішно завантажено з файлу:", loaded_data)

if __name__ == "__main__":
    main()

#2
def compress(data):
    return ' '.join(map(str, data))

def decompress(data):
    return list(map(int, data.split()))

def load_data():
    try:
        with open("data.txt", "r") as file:
            compressed_data = file.read()
            return decompress(compressed_data)
    except FileNotFoundError:
        print("Файл з даними не знайдено.")
        return []

def save_data(data):
    compressed_data = compress(data)
    with open("data.txt", "w") as file:
        file.write(compressed_data)
    print("Дані успішно збережено у файлі.")

def add_data(data):
    new_data = list(map(int, input("Введіть нові дані через пробіл: ").split()))
    data.extend(new_data)
    print("Дані успішно додано.")

def remove_data(data):
    try:
        value = int(input("Введіть значення, яке потрібно видалити: "))
        if value in data:
            data.remove(value)
            print("Дані успішно видалено.")
        else:
            print("Таке значення не знайдено.")
    except ValueError:
        print("Неправильний формат вводу.")

def main():
    data = []

    while True:
        print("\nМеню:")
        print("1. Завантаження даних")
        print("2. Збереження даних")
        print("3. Додавання даних")
        print("4. Видалення даних")
        print("5. Вихід")
        choice = input("Оберіть опцію: ")

        if choice == '1':
            data = load_data()
        elif choice == '2':
            save_data(data)
        elif choice == '3':
            add_data(data)
        elif choice == '4':
            remove_data(data)
        elif choice == '5':
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()


#3
import gzip
import pickle

def save_data(data, filename):
    with gzip.open(filename, 'wb') as f:
        pickle.dump(data, f)

def load_data(filename):
    with gzip.open(filename, 'rb') as f:
        data = pickle.load(f)
    return data

def add_user(users, username, password):
    users[username] = password

def delete_user(users, username):
    if username in users:
        del users[username]
    else:
        print(f"Користувача з логіном {username} не знайдено.")

def search_user(users, username):
    if username in users:
        print(f"Пароль для користувача {username}: {users[username]}")
    else:
        print(f"Користувача з логіном {username} не знайдено.")

def edit_password(users, username, new_password):
    if username in users:
        users[username] = new_password
    else:
        print(f"Користувача з логіном {username} не знайдено.")

initial_users = {'user1': 'password1', 'user2': 'password2'}

save_data(initial_users, 'users_data.gz')

loaded_users = load_data('users_data.gz')

add_user(loaded_users, 'new_user', 'new_password')

delete_user(loaded_users, 'user1')

search_user(loaded_users, 'user2')

edit_password(loaded_users, 'user2', 'new_password2')

save_data(loaded_users, 'updated_users_data.gz')
