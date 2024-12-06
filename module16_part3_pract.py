# Завдання 1: Запуск сервера Redis
redis-server &

# Завдання 2: Додавання ключа-значення
redis-cli SET name "John Doe"

# Завдання 3: Отримання значення за ключем
redis-cli GET name

# Завдання 4: Додавання списку
redis-cli RPUSH fruits "apple" "banana" "orange"

# Завдання 5: Отримання елементів списку
redis-cli LRANGE fruits 0 -1

# Завдання 6: Додавання хешу
redis-cli HMSET user:1 name "Alice" age 25

# Завдання 7: Отримання значень з хешу
redis-cli HGETALL user:1

# Завдання 8: Додавання елементу до множини
redis-cli SADD tags "red" "green" "blue"

# Завдання 9: Отримання всіх елементів множини
redis-cli SMEMBERS tags

# Завдання 10: Додавання лічильника
redis-cli INCR counter

# Завдання 11: Отримання значення лічильника
redis-cli GET counter

# Завдання 12: Видалення ключа
redis-cli DEL name

# Завдання 13: Перевірка існування ключа
redis-cli EXISTS name

# Завдання 14: Додавання значення з таймаутом
redis-cli SETEX message 60 "Hello, Redis!"

# Завдання 15: Очищення всіх ключів
redis-cli FLUSHALL

# Завдання 16: Геоаналітика з Redis
redis-cli GEOADD geo_locations 30.1234 40.5678 "Location1"

# Завдання 17: Хешування
redis-cli HMSET students Alice 90 Bob 85 Carol 88
redis-cli HGETALL students
redis-cli HSET students Bob 87
redis-cli HGETALL students

# Завдання 18: Статистика унікальних користувачів
redis-cli PFADD unique_users user1 user2 user3

# Завдання 19: Використання транзакцій
redis-cli MULTI
redis-cli LPUSH mylist "Hello" "World"
redis-cli HMSET myhash field1 "Hello" field2 "World"
redis-cli EXEC

# Завдання 20: Закриття сервера Redis
redis-cli SHUTDOWN