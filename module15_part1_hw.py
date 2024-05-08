#1
-- CREATE DATABASE Birds;
#2
-- ALTER DATABASE Birds RENAME TO Cats;
#3
-- DROP DATABASE IF EXISTS Cats;
#4
CREATE TABLE IF NOT EXISTS VegetablesAndFruits (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(50) NOT NULL,
    color VARCHAR(50),
    calories INT,
    description TEXT
);

INSERT INTO VegetablesAndFruits (name, type, color, calories, description)
VALUES
    ('Apple', 'Fruit', 'Red', 52, 'A round fruit with red skin and sweet flesh.'),
    ('Banana', 'Fruit', 'Yellow', 89, 'A long curved fruit with yellow skin and soft flesh.'),
    ('Carrot', 'Vegetable', 'Orange', 41, 'A long orange root vegetable often used in salads and cooking.'),
    ('Spinach', 'Vegetable', 'Green', 23, 'A leafy green vegetable with a slightly bitter taste.'),
    ('Tomato', 'Fruit', 'Red', 18, 'A round red fruit often used in salads and cooking.'),
    ('Broccoli', 'Vegetable', 'Green', 34, 'A green vegetable with small florets that is often steamed or boiled.');

#5
SELECT * FROM VegetablesAndFruits;
SELECT * FROM VegetablesAndFruits WHERE Type = 'Vegetable';
SELECT * FROM VegetablesAndFruits WHERE Type = 'Fruit';
SELECT Name FROM VegetablesAndFruits;
SELECT DISTINCT Color FROM VegetablesAndFruits;
SELECT * FROM VegetablesAndFruits WHERE Type = 'Fruit' AND Color = 'Red';
SELECT * FROM VegetablesAndFruits WHERE Type = 'Vegetable' AND Color = 'Green';