#1
import pickle
import gzip

def save_data(data, filename):
    with gzip.open(filename, 'wb') as f:
        pickle.dump(data, f)

def load_data(filename):
    with gzip.open(filename, 'rb') as f:
        data = pickle.load(f)
    return data

user_data = []
while True:
    num = input("Введіть ціле число або 'stop' для завершення вводу: ")
    if num.lower() == 'stop':
        break
    try:
        user_data.append(int(num))
    except ValueError:
        print("Неправильне введення. Спробуйте ще раз.")

save_data(user_data, 'compressed_data.pkl.gz')

loaded_data = load_data('compressed_data.pkl.gz')
print("Завантажені дані з файлу:", loaded_data)

#2
def save_data(data, filename):
    with gzip.open(filename, 'wb') as f:
        pickle.dump(data, f)


def load_data(filename):
    with gzip.open(filename, 'rb') as f:
        data = pickle.load(f)
    return data


def main():
    data = []

    while True:
        print("\nМеню:")
        print("1. Завантаження даних")
        print("2. Збереження даних")
        print("3. Додавання даних")
        print("4. Видалення даних")
        print("5. Вихід")

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
            try:
                num = int(input("Введіть ціле число для додавання: "))
                data.append(num)
                print("Дані успішно додано до списку.")
            except ValueError:
                print("Неправильне введення. Будь ласка, введіть ціле число.")
        elif choice == '4':
            try:
                index = int(input("Введіть індекс елемента, який потрібно видалити: "))
                if 0 <= index < len(data):
                    del data[index]
                    print("Елемент успішно видалено.")
                else:
                    print("Неправильний індекс.")
            except ValueError:
                print("Неправильне введення. Будь ласка, введіть ціле число.")
        elif choice == '5':
            print("До побачення!")
            break
        else:
            print("Неправильний вибір. Будь ласка, виберіть опцію зі списку.")


if __name__ == "__main__":
    main()

#3

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
