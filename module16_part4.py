#1
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

def register_user(username, password):
    if r.hexists("users", username):
        print("Користувач вже існує.")
    else:
        r.hset("users", username, password)
        print("Користувача зареєстровано.")

def login(username, password):
    if r.hexists("users", username):
        stored_password = r.hget("users", username).decode()
        if stored_password == password:
            print("Вхід успішний.")
            return True
        else:
            print("Неправильний пароль.")
    else:
        print("Користувача не знайдено.")
    return False

def add_item_to_cart(username, item, quantity):
    cart_key = f"cart:{username}"
    r.hset(cart_key, item, quantity)
    print(f"Товар {item} у кількості {quantity} додано до кошика.")

def remove_item_from_cart(username, item):
    cart_key = f"cart:{username}"
    if r.hexists(cart_key, item):
        r.hdel(cart_key, item)
        print(f"Товар {item} видалено з кошика.")
    else:
        print(f"Товар {item} не знайдено у кошику.")

def update_item_in_cart(username, item, quantity):
    cart_key = f"cart:{username}"
    if r.hexists(cart_key, item):
        r.hset(cart_key, item, quantity)
        print(f"Кількість товару {item} оновлено на {quantity}.")
    else:
        print(f"Товар {item} не знайдено у кошику.")

def clear_cart(username):
    cart_key = f"cart:{username}"
    r.delete(cart_key)
    print("Кошик очищено.")

def search_item_in_cart(username, item):
    cart_key = f"cart:{username}"
    if r.hexists(cart_key, item):
        quantity = r.hget(cart_key, item).decode()
        print(f"Товар {item} у кількості {quantity} є у кошику.")
    else:
        print(f"Товар {item} не знайдено у кошику.")

def view_cart(username):
    cart_key = f"cart:{username}"
    cart = r.hgetall(cart_key)
    if cart:
        print("Вміст кошика:")
        for item, quantity in cart.items():
            print(f"{item.decode()}: {quantity.decode()}")
    else:
        print("Кошик порожній.")

def main():
    current_user = None
    while True:
        print("\nМеню:")
        print("1. Зареєструватися")
        print("2. Увійти")
        print("3. Додати товар до кошика")
        print("4. Видалити товар з кошика")
        print("5. Змінити кількість товару в кошику")
        print("6. Очистити кошик")
        print("7. Пошук товару в кошику")
        print("8. Переглянути вміст кошика")
        print("9. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            username = input("Введіть ім'я користувача: ")
            password = input("Введіть пароль: ")
            register_user(username, password)
        elif choice == "2":
            username = input("Введіть ім'я користувача: ")
            password = input("Введіть пароль: ")
            if login(username, password):
                current_user = username
        elif choice == "3":
            if current_user:
                item = input("Введіть назву товару: ")
                quantity = input("Введіть кількість: ")
                add_item_to_cart(current_user, item, quantity)
            else:
                print("Спочатку увійдіть у систему.")
        elif choice == "4":
            if current_user:
                item = input("Введіть назву товару: ")
                remove_item_from_cart(current_user, item)
            else:
                print("Спочатку увійдіть у систему.")
        elif choice == "5":
            if current_user:
                item = input("Введіть назву товару: ")
                quantity = input("Введіть нову кількість: ")
                update_item_in_cart(current_user, item, quantity)
            else:
                print("Спочатку увійдіть у систему.")
        elif choice == "6":
            if current_user:
                clear_cart(current_user)
            else:
                print("Спочатку увійдіть у систему.")
        elif choice == "7":
            if current_user:
                item = input("Введіть назву товару для пошуку: ")
                search_item_in_cart(current_user, item)
            else:
                print("Спочатку увійдіть у систему.")
        elif choice == "8":
            if current_user:
                view_cart(current_user)
            else:
                print("Спочатку увійдіть у систему.")
        elif choice == "9":
            print("Вихід із програми.")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()

#2

r = redis.Redis(host='localhost', port=6379, db=0)

def register_user(username, password):
    if r.hexists("users", username):
        print("Користувач вже існує.")
    else:
        r.hset("users", username, password)
        print("Користувача зареєстровано.")

def login(username, password):
    if r.hexists("users", username):
        stored_password = r.hget("users", username).decode()
        if stored_password == password:
            print("Вхід успішний.")
            return True
        else:
            print("Неправильний пароль.")
    else:
        print("Користувача не знайдено.")
    return False

def add_score(username, score):
    r.zadd("leaderboard", {username: score})
    print(f"Результат {score} додано для користувача {username}.")

def remove_score(username):
    r.zrem("leaderboard", username)
    print(f"Результат користувача {username} видалено з таблиці.")

def update_score(username, score):
    r.zadd("leaderboard", {username: score})
    print(f"Результат користувача {username} оновлено на {score}.")

def clear_leaderboard():
    r.delete("leaderboard")
    print("Таблиця рекордів очищена.")

def search_score(username):
    score = r.zscore("leaderboard", username)
    if score is not None:
        print(f"Користувач {username} має результат {score}.")
    else:
        print(f"Результат для користувача {username} не знайдено.")

def view_leaderboard():
    leaderboard = r.zrevrange("leaderboard", 0, -1, withscores=True)
    if leaderboard:
        print("Вміст таблиці рекордів:")
        for user, score in leaderboard:
            print(f"{user.decode()}: {int(score)}")
    else:
        print("Таблиця рекордів порожня.")

def top_ten():
    top_scores = r.zrevrange("leaderboard", 0, 9, withscores=True)
    if top_scores:
        print("Топ 10 результатів:")
        for user, score in top_scores:
            print(f"{user.decode()}: {int(score)}")
    else:
        print("Таблиця рекордів порожня.")

def main():
    current_user = None
    while True:
        print("\nМеню:")
        print("1. Зареєструватися")
        print("2. Увійти")
        print("3. Додати результат")
        print("4. Видалити результат")
        print("5. Змінити результат")
        print("6. Очистити таблицю")
        print("7. Пошук результату")
        print("8. Переглянути таблицю")
        print("9. Відобразити топ 10")
        print("10. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            username = input("Введіть ім'я користувача: ")
            password = input("Введіть пароль: ")
            register_user(username, password)
        elif choice == "2":
            username = input("Введіть ім'я користувача: ")
            password = input("Введіть пароль: ")
            if login(username, password):
                current_user = username
        elif choice == "3":
            if current_user:
                score = int(input("Введіть результат: "))
                add_score(current_user, score)
            else:
                print("Спочатку увійдіть у систему.")
        elif choice == "4":
            if current_user:
                remove_score(current_user)
            else:
                print("Спочатку увійдіть у систему.")
        elif choice == "5":
            if current_user:
                score = int(input("Введіть новий результат: "))
                update_score(current_user, score)
            else:
                print("Спочатку увійдіть у систему.")
        elif choice == "6":
            clear_leaderboard()
        elif choice == "7":
            username = input("Введіть ім'я користувача для пошуку: ")
            search_score(username)
        elif choice == "8":
            view_leaderboard()
        elif choice == "9":
            top_ten()
        elif choice == "10":
            print("Вихід із програми.")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()




