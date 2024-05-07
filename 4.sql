CREATE TABLE Students (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100),
    city VARCHAR(100),
    country VARCHAR(100),
    birth_date DATE,
    email VARCHAR(100),
    phone VARCHAR(20),
    group_name VARCHAR(50),
    average_grade FLOAT,
    min_subject VARCHAR(100),
    min_subject_grade FLOAT,
    max_subject VARCHAR(100),
    max_subject_grade FLOAT
);
INSERT INTO Students (full_name, city, country, birth_date, email, phone, group_name, average_grade, min_subject, min_subject_grade, max_subject, max_subject_grade)
VALUES
    ('Іваненко Іван Іванович', 'Київ', 'Україна', '1998-05-15', 'ivanenko@example.com', '+380991234567', 'Група 1', 85.5, 'Математика', 80.0, 'Фізика', 90.0),
    ('Петренко Марина Петрівна', 'Львів', 'Україна', '1999-08-20', 'petrenko@example.com', '+380991234568', 'Група 2', 90.0, 'Хімія', 85.0, 'Англійська мова', 95.0),
    ('Сидоренко Олексій Сергійович', 'Одеса', 'Україна', '2000-01-10', 'sidorenko@example.com', '+380991234569', 'Група 1', 88.0, 'Біологія', 82.0, 'Географія', 92.0);

-- Завдання 5
SELECT * FROM students_grades;
SELECT full_name FROM students_grades;
SELECT AVG(average_grade) FROM students_grades;
SELECT full_name FROM students_grades WHERE min_grade > '83';
SELECT DISTINCT country FROM students_grades;
SELECT DISTINCT city FROM students_grades;
SELECT DISTINCT group_name FROM students_grades;
SELECT DISTINCT subject_name FROM students_grades WHERE average_grade = (SELECT MIN(average_grade) FROM students_grades);

