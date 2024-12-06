
яINSERT INTO Students (full_name, date_of_birth, city, country, email, phone_number, grade) VALUES
('John Smith', '2000-05-15', 'New York', 'USA', 'john@example.com', '1234567890', 85.50),
('Alice Johnson', '2001-08-20', 'Los Angeles', 'USA', 'alice@example.com', '9876543210', 90.25),
('Michael Brown', '1989-11-10', 'London', 'UK', 'michael@example.com', '7418529630', 79.00),
('Sophia Miller', '2000-03-25', 'Paris', 'France', 'sophia@example.com', '1592637480', 87.75),
('Emma Wilson', '2001-01-05', 'Berlin', 'Germany', 'emma@example.com', '3698577770', 92.80),
('Daniel Taylor', '2000-09-12', 'Sydney', 'Australia', 'daniel@exampl		e.com', '2581470369', 88.90);

-- ALTER TABLE Students
-- ADD COLUMN lower_limit DECIMAL(5,2) DEFAULT 0.00,
-- ADD COLUMN upper_limit DECIMAL(5,2) DEFAULT 100.00;


-- SELECT full_name
-- FROM Students
-- WHERE grade = (SELECT MIN(grade) FROM Students WHERE grade BETWEEN lower_limit AND upper_limit);

-- SELECT *
-- FROM Students
-- WHERE DATE_PART('year', AGE(CURRENT_DATE, date_of_birth)) = 20;

-- SELECT *
-- FROM Students
-- WHERE DATE_PART('year', AGE(CURRENT_DATE, date_of_birth)) BETWEEN 20 AND 25;

-- SELECT *
-- FROM Students
-- WHERE full_name LIKE 'John%';

-- SELECT *
-- FROM Students
-- WHERE phone_number LIKE '%777%';

-- SELECT email
-- FROM Students
-- WHERE LOWER(email) LIKE 'a%';


-- SELECT MIN(avg_grade) AS min_avg_grade
-- FROM (
--     SELECT AVG(grade) AS avg_grade
--     FROM Students
--     GROUP BY student_id
-- ) AS avg_grades;

-- SELECT MAX(average_grade) AS max_average_grade
-- FROM (
--     SELECT student_id, AVG(grade) AS average_grade
--     FROM Students
--     GROUP BY student_id
-- ) AS student_avg_grades;

-- SELECT city, COUNT(*) AS student_count
-- FROM Students
-- GROUP BY city;

-- SELECT country, COUNT(*) AS student_count
-- FROM Students
-- GROUP BY country;

-- ALTER TABLE Students
-- ADD COLUMN subject VARCHAR(100);

-- UPDATE Students
-- SET subject = 'Math';

-- SELECT COUNT(*) AS student_count
-- FROM Students
-- WHERE grade = (
--     SELECT MIN(grade)
--     FROM Students
-- ) AND city = 'Math';

-- SELECT MAX(grade) AS max_math_grade
-- FROM Students
-- WHERE subject = 'Math';

-- SELECT COUNT(*) AS student_count
-- FROM Students
-- WHERE grade = (
--     SELECT MAX(grade)
--     FROM Students
--     WHERE subject = 'Math'
-- ) AND subject = 'Math';


-- SELECT city, COUNT(*) AS student_count
-- FROM Students
-- GROUP BY city;

-- Показати середню оцінку групи.
-- SELECT city, AVG(grade) AS average_grade
-- FROM Students
-- GROUP BY city;



















