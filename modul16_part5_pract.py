#1
import redis
import hashlib

r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def add_user(username, password, full_name, email):
    if r.hexists('users', username):
        return "User already exists"

    user_data = {
        'username': username,
        'password': hash_password(password),
        'full_name': full_name,
        'email': email,
        'friends': [],
        'posts': []
    }
    r.hset('users', username, str(user_data))
    return "User added successfully"


def delete_user(username):
    if not r.hexists('users', username):
        return "User does not exist"

    r.hdel('users', username)
    return "User deleted successfully"


def update_user(username, full_name=None, email=None):
    if not r.hexists('users', username):
        return "User does not exist"

    user_data = eval(r.hget('users', username))
    if full_name:
        user_data['full_name'] = full_name
    if email:
        user_data['email'] = email

    r.hset('users', username, str(user_data))
    return "User updated successfully"


def get_user(username):
    if not r.hexists('users', username):
        return "User does not exist"

    user_data = eval(r.hget('users', username))
    return user_data


def search_user_by_full_name(full_name):
    users = r.hgetall('users')
    matching_users = [eval(user) for user in users.values() if eval(user)['full_name'] == full_name]
    return matching_users


def add_friend(username, friend_username):
    if not r.hexists('users', username) or not r.hexists('users', friend_username):
        return "One of the users does not exist"

    user_data = eval(r.hget('users', username))
    friend_data = eval(r.hget('users', friend_username))

    if friend_username not in user_data['friends']:
        user_data['friends'].append(friend_username)
        r.hset('users', username, str(user_data))

    if username not in friend_data['friends']:
        friend_data['friends'].append(username)
        r.hset('users', friend_username, str(friend_data))

    return "Friend added successfully"


def remove_friend(username, friend_username):
    if not r.hexists('users', username) or not r.hexists('users', friend_username):
        return "One of the users does not exist"

    user_data = eval(r.hget('users', username))
    friend_data = eval(r.hget('users', friend_username))

    if friend_username in user_data['friends']:
        user_data['friends'].remove(friend_username)
        r.hset('users', username, str(user_data))

    if username in friend_data['friends']:
        friend_data['friends'].remove(username)
        r.hset('users', friend_username, str(friend_data))

    return "Friend removed successfully"


def add_post(username, content):
    if not r.hexists('users', username):
        return "User does not exist"

    user_data = eval(r.hget('users', username))
    user_data['posts'].append(content)
    r.hset('users', username, str(user_data))

    return "Post added successfully"


def get_posts(username):
    if not r.hexists('users', username):
        return "User does not exist"

    user_data = eval(r.hget('users', username))
    return user_data['posts']


def get_friends(username):
    if not r.hexists('users', username):
        return "User does not exist"

    user_data = eval(r.hget('users', username))
    return user_data['friends']


def main():
    while True:
        print("\nСоціальна мережа")
        print("1. Вхід")
        print("2. Додати користувача")
        print("3. Видалити користувача")
        print("4. Редагувати інформацію про користувача")
        print("5. Пошук користувача за ПІБ")
        print("6. Перегляд інформації про користувача")
        print("7. Перегляд усіх друзів користувача")
        print("8. Перегляд усіх публікацій користувача")
        print("9. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            username = input("Введіть ім'я користувача: ")
            password = input("Введіть пароль: ")
            user_data = get_user(username)
            if user_data and user_data['password'] == hash_password(password):
                print("Вхід виконано")
            else:
                print("Невірний логін або пароль")

        elif choice == '2':
            username = input("Введіть ім'я користувача: ")
            password = input("Введіть пароль: ")
            full_name = input("Введіть повне ім'я: ")
            email = input("Введіть email: ")
            print(add_user(username, password, full_name, email))

        elif choice == '3':
            username = input("Введіть ім'я користувача: ")
            print(delete_user(username))

        elif choice == '4':
            username = input("Введіть ім'я користувача: ")
            full_name = input("Введіть нове повне ім'я (або залиште порожнім): ")
            email = input("Введіть новий email (або залиште порожнім): ")
            print(update_user(username, full_name, email))

        elif choice == '5':
            full_name = input("Введіть повне ім'я для пошуку: ")
            users = search_user_by_full_name(full_name)
            if users:
                for user in users:
                    print(user)
            else:
                print("Користувачів не знайдено")

        elif choice == '6':
            username = input("Введіть ім'я користувача: ")
            user_data = get_user(username)
            if user_data:
                print(user_data)
            else:
                print("Користувача не знайдено")

        elif choice == '7':
            username = input("Введіть ім'я користувача: ")
            friends = get_friends(username)
            if friends:
                print(friends)
            else:
                print("Друзів не знайдено")

        elif choice == '8':
            username = input("Введіть ім'я користувача: ")
            posts = get_posts(username)
            if posts:
                print(posts)
            else:
                print("Публікацій не знайдено")

        elif choice == '9':
            break

        else:
            print("Невірна опція. Спробуйте ще раз.")


if __name__ == "__main__":
    main()

#2
r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def add_user(username, password):
    if r.hexists('users', username):
        return "User already exists"

    user_data = {
        'username': username,
        'password': hash_password(password)
    }
    r.hset('users', username, str(user_data))
    return "User added successfully"


def validate_user(username, password):
    if not r.hexists('users', username):
        return False

    user_data = eval(r.hget('users', username))
    return user_data['password'] == hash_password(password)


def add_exhibit(exhibit_id, title, description, category, related_people):
    if r.hexists('exhibits', exhibit_id):
        return "Exhibit already exists"

    exhibit_data = {
        'exhibit_id': exhibit_id,
        'title': title,
        'description': description,
        'category': category,
        'related_people': related_people
    }
    r.hset('exhibits', exhibit_id, str(exhibit_data))

    for person in related_people:
        r.sadd(f'person:{person}', exhibit_id)

    return "Exhibit added successfully"


def delete_exhibit(exhibit_id):
    if not r.hexists('exhibits', exhibit_id):
        return "Exhibit does not exist"

    exhibit_data = eval(r.hget('exhibits', exhibit_id))
    related_people = exhibit_data['related_people']

    for person in related_people:
        r.srem(f'person:{person}', exhibit_id)

    r.hdel('exhibits', exhibit_id)
    return "Exhibit deleted successfully"


def update_exhibit(exhibit_id, title=None, description=None, category=None, related_people=None):
    if not r.hexists('exhibits', exhibit_id):
        return "Exhibit does not exist"

    exhibit_data = eval(r.hget('exhibits', exhibit_id))

    if title:
        exhibit_data['title'] = title
    if description:
        exhibit_data['description'] = description
    if category:
        exhibit_data['category'] = category
    if related_people:
        old_related_people = exhibit_data['related_people']
        for person in old_related_people:
            r.srem(f'person:{person}', exhibit_id)

        exhibit_data['related_people'] = related_people
        for person in related_people:
            r.sadd(f'person:{person}', exhibit_id)

    r.hset('exhibits', exhibit_id, str(exhibit_data))
    return "Exhibit updated successfully"


def get_exhibit(exhibit_id):
    if not r.hexists('exhibits', exhibit_id):
        return "Exhibit does not exist"

    exhibit_data = eval(r.hget('exhibits', exhibit_id))
    return exhibit_data


def get_all_exhibits():
    exhibits = r.hgetall('exhibits')
    return [eval(exhibit) for exhibit in exhibits.values()]


def get_related_people(exhibit_id):
    if not r.hexists('exhibits', exhibit_id):
        return "Exhibit does not exist"

    exhibit_data = eval(r.hget('exhibits', exhibit_id))
    return exhibit_data['related_people']


def get_exhibits_by_person(person_name):
    exhibit_ids = r.smembers(f'person:{person_name}')
    return [eval(r.hget('exhibits', exhibit_id)) for exhibit_id in exhibit_ids]


def get_exhibits_by_category(category):
    exhibits = r.hgetall('exhibits')
    return [eval(exhibit) for exhibit in exhibits.values() if eval(exhibit)['category'] == category]


def main():
    current_user = None

    while True:
        print("\nМузей літератури")
        if current_user:
            print(f"Ви увійшли як: {current_user}")
        print("1. Вхід")
        print("2. Додати експонат")
        print("3. Видалити експонат")
        print("4. Редагування інформації про експонат")
        print("5. Перегляд повної інформації про експонат")
        print("6. Виведення інформації про всі експонати")
        print("7. Перегляд інформації про людей, які мають відношення до певного експонату")
        print("8. Перегляд інформації про експонати, що мають відношення до певної людини")
        print("9. Перегляд набору експонатів на основі певного критерію")
        print("10. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            username = input("Введіть ім'я користувача: ")
            password = input("Введіть пароль: ")
            if validate_user(username, password):
                current_user = username
                print("Вхід виконано")
            else:
                print("Невірний логін або пароль")

        elif choice == '2' and current_user:
            exhibit_id = input("Введіть ID експоната: ")
            title = input("Введіть назву: ")
            description = input("Введіть опис: ")
            category = input("Введіть категорію: ")
            related_people = input("Введіть людей, пов'язаних з експонатом (через кому): ").split(',')
            related_people = [person.strip() for person in related_people]
            print(add_exhibit(exhibit_id, title, description, category, related_people))

        elif choice == '3' and current_user:
            exhibit_id = input("Введіть ID експоната: ")
            print(delete_exhibit(exhibit_id))

        elif choice == '4' and current_user:
            exhibit_id = input("Введіть ID експоната: ")
            title = input("Введіть нову назву (або залиште порожнім): ")
            description = input("Введіть новий опис (або залиште порожнім): ")
            category = input("Введіть нову категорію (або залиште порожнім): ")
            related_people = input("Введіть нових людей, пов'язаних з експонатом (або залиште порожнім): ")
            if related_people:
                related_people = related_people.split(',')
                related_people = [person.strip() for person in related_people]
            else:
                related_people = None
            print(update_exhibit(exhibit_id, title, description, category, related_people))

        elif choice == '5':
            exhibit_id = input("Введіть ID експоната: ")
            exhibit_data = get_exhibit(exhibit_id)
            if exhibit_data:
                print(exhibit_data)
            else:
                print("Експонат не знайдено")

        elif choice == '6':
            exhibits = get_all_exhibits()
            if exhibits:
                for exhibit in exhibits:
                    print(exhibit)
            else:
                print("Експонатів не знайдено")

        elif choice == '7':
            exhibit_id = input("Введіть ID експоната: ")
            related_people = get_related_people(exhibit_id)
            if related_people:
                print(related_people)
            else:
                print("Людей не знайдено")

        elif choice == '8':
            person_name = input("Введіть ім'я людини: ")
            exhibits = get_exhibits_by_person(person_name)
            if exhibits:
                for exhibit in exhibits:
                    print(exhibit)
            else:
                print("Експонатів не знайдено")

        elif choice == '9':
            category = input("Введіть категорію експонатів для пошуку: ")
            exhibits = get_exhibits_by_category(category)
            if exhibits:
                for exhibit in exhibits:
                    print(exhibit)
            else:
                print("Експонатів не знайдено")

        elif choice == '10':
            break

        else:
            print("Невірна опція або недостатні права. Спробуйте ще раз.")


if __name__ == "__main__":
    main()


#3