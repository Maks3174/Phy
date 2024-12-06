# 2. Робота з ключами та значеннями
redis-cli SET username "YourName"

# 3. Робота зі списками
redis-cli RPUSH todo_list "Поготувати обід" "Вивчити Redis"
redis-cli LRANGE todo_list 0 -1

# 4. Робота з хешами
redis-cli HMSET user_data age 25 country "Ukraine"
redis-cli HGETALL user_data

# 5. Робота з множинами
redis-cli SADD tags "programming" "redis" "tutorial"
redis-cli SMEMBERS tags

# 6. Лічильники
redis-cli SET page_views 0
for ((i=1; i<=5; i++)); do
  redis-cli INCR page_views
done
redis-cli GET page_views

# 7. Створення ключа із таймаутом
redis-cli SETEX session_token 120 "abc123"

# 8. Видалення ключів
redis-cli DEL username
redis-cli EXISTS username

# 9. Патерни ключів
redis-cli SET user:1:name "YourName"
redis-cli KEYS "user:*"

# 10. Робота з бітовими рядками
redis-cli SETBIT online_status 0 1
redis-cli GETBIT online_status 0

# 11. Використання транзакцій
redis-cli MULTI
redis-cli SET balance 0
redis-cli INCRBY balance 1000
redis-cli EXEC

# 12. Використання Redis для кешування
redis-cli SADD cache:popular_articles "article1" "article2" "article3"

# 13. Задача на операції над множинами
redis-cli SADD set1 "a" "b" "c"
redis-cli SADD set2 "c" "d" "e"
redis-cli SUNIONSTORE union_set set1 set2
redis-cli SINTERSTORE intersection_set set1 set2

# 14. Використання патерну Pub/Sub
( redis-cli SUBSCRIBE messages & )
sleep 1
redis-cli PUBLISH messages "Hello, Redis!"

# 16. Робота з геоданими
redis-cli GEOADD locations 30.1234 40.5678 "Location1"

# 17. Видалення елементів списку
redis-cli LPUSH tasks "Task 1" "Task 2" "Task 3"
redis-cli LPUSH tasks "Task 4"
redis-cli LPOP tasks
redis-cli LRANGE tasks 0 -1

# 18. Робота з HyperLogLog
redis-cli PFADD unique_users "user1" "user2" "user3"

# 19. Робота з рядками
redis-cli RPUSH message_queue "Message1" "Message2" "Message3"
redis-cli LRANGE message_queue 0 -1
