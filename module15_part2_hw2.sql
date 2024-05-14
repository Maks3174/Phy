#1
CREATE TABLE Produce (
    produce_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    type VARCHAR(50),
    color VARCHAR(50),
    origin VARCHAR(100),
    price DECIMAL(8, 2),
    calories DECIMAL(8, 2),
    category VARCHAR(50)
);

INSERT INTO Produce (name, type, color, origin, price, calories, category) VALUES
('Помідор', 'Плідовий овоч', 'Червоний', 'Україна', 25.50, 18.0, 'Овочі'),
('Брокколі', 'Капустяний овоч', 'Зелений', 'Іспанія', 30.75, 34.0, 'Овочі'),
('Огірок', 'Плодовий овоч', 'Зелений', 'Німеччина', 15.25, 15.0, 'Овочі'),
('Морква', 'Кореневий овоч', 'Помаранчевий', 'Україна', 20.00, 41.0, 'Овочі');

INSERT INTO Produce (name, type, color, origin, price, calories, category) VALUES
('Яблуко', 'Плід', 'Червоний', 'Україна', 12.50, 52.0, 'Фрукти'),
('Апельсин', 'Плід', 'Помаранчевий', 'Іспанія', 18.75, 47.0, 'Фрукти'),
('Банан', 'Плід', 'Жовтий', 'Еквадор', 22.00, 89.0, 'Фрукти'),
('Ківі', 'Плід', 'Зелений', 'Нова Зеландія', 30.00, 61.0, 'Фрукти');

SELECT *
FROM Produce
WHERE category = 'Овочі' AND calories < 50;

SELECT *
FROM Produce
WHERE category = 'Фрукти' AND calories BETWEEN 40 AND 60;

SELECT *
FROM Produce
WHERE category = 'Овочі' AND name LIKE '%капуста%';

SELECT *
FROM Produce
WHERE name LIKE '%гемоглобін%' OR type LIKE '%гемоглобін%' OR origin LIKE '%гемоглобін%';

SELECT *
FROM Produce
WHERE color IN ('Червоний', 'Жовтий');

#2
SELECT COUNT(*) AS vegetable_count
FROM Produce
WHERE category = 'Овочі';

SELECT COUNT(*) AS fruit_count
FROM Produce
WHERE category = 'Фрукти';

SELECT color, COUNT(*) AS produce_count
FROM Produce
WHERE color = 'Червоний'
GROUP BY color;

SELECT color, COUNT(*) AS produce_count
FROM Produce
GROUP BY color;

SELECT color, MIN(produce_count) AS min_count
FROM (
    SELECT color, COUNT(*) AS produce_count
    FROM Produce
    GROUP BY color
) AS color_counts
GROUP BY color
ORDER BY min_count
LIMIT 1;

SELECT color, MAX(produce_count) AS max_count
FROM (
    SELECT color, COUNT(*) AS produce_count
    FROM Produce
    GROUP BY color
) AS color_counts
GROUP BY color
ORDER BY max_count DESC
LIMIT 1;

SELECT MIN(calories) AS min_calories
FROM Produce;

SELECT MAX(calories) AS max_calories
FROM Produce;

SELECT AVG(calories) AS avg_calories
FROM Produce;

SELECT *
FROM Produce
WHERE category = 'Фрукти'
ORDER BY calories
LIMIT 1;

SELECT *
FROM Produce
WHERE category = 'Фрукти'
ORDER BY calories DESC
LIMIT 1;