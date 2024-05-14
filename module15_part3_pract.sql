-- Створення таблиці Відділення (Departments)
CREATE TABLE Departments (
    Id SERIAL PRIMARY KEY,
    Building INT NOT NULL CHECK (Building BETWEEN 1 AND 5),
    Financing DECIMAL(10,2) NOT NULL DEFAULT 0.00 CHECK (Financing >= 0),
    Name VARCHAR(100) NOT NULL UNIQUE
);

-- Створення таблиці Захворювання (Diseases)
CREATE TABLE Diseases (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL UNIQUE,
    Severity INT NOT NULL DEFAULT 1 CHECK (Severity >= 1)
);

-- Створення таблиці Лікарі (Doctors)
CREATE TABLE Doctors (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Phone CHAR(10),
    Salary DECIMAL(10,2) NOT NULL CHECK (Salary > 0),
    Surname VARCHAR(255) NOT NULL
);

-- Створення таблиці Обстеження (Examinations)
CREATE TABLE Examinations (
    Id SERIAL PRIMARY KEY,
    DayOfWeek INT NOT NULL CHECK (DayOfWeek BETWEEN 1 AND 7),
    EndTime TIME NOT NULL,
    Name VARCHAR(100) NOT NULL UNIQUE,
    StartTime TIME NOT NULL CHECK (StartTime >= '08:00' AND StartTime <= '18:00')
);

-- Створення таблиці Палати (Wards)
CREATE TABLE Wards (
    Id SERIAL PRIMARY KEY,
    Building INT NOT NULL CHECK (Building BETWEEN 1 AND 5),
    Floor INT NOT NULL CHECK (Floor >= 1),
    Name VARCHAR(20) NOT NULL UNIQUE
);

INSERT INTO Departments (Building, Financing, Name) VALUES
(1, 25000, 'Cardiology'),
(2, 30000, 'Orthopedics'),
(3, 20000, 'Neurology'),
(4, 35000, 'Oncology'),
(5, 28000, 'Pediatrics');

INSERT INTO Diseases (Name, Severity) VALUES
('Hypertension', 2),
('Fracture', 3),
('Migraine', 1),
('Leukemia', 4),
('Asthma', 2);

	INSERT INTO Doctors (Name, Phone, Salary, Surname) VALUES
('John', '1234567890', 3500.00, 'Doe'),
('Alice', '0987654321', 4200.00, 'Johnson'),
('Michael', '2345678901', 3900.00, 'Smith'),
('Sophia', '5678901234', 3800.00, 'Brown'),
('Daniel', '7890123456', 4000.00, 'Taylor');

INSERT INTO Examinations (DayOfWeek, EndTime, Name, StartTime) VALUES
(1, '10:00', 'MRI Scan', '08:00'),
(2, '11:30', 'X-Ray', '09:00'),
(3, '13:00', 'Blood Test', '10:00'),
(4, '14:30', 'Ultrasound', '11:00'),
(5, '16:00', 'ECG', '12:00');

INSERT INTO Wards (Building, Floor, Name) VALUES
(1, 1, '101A'),
(2, 2, '202B'),
(3, 1, '301C'),
(4, 3, '403D'),
(5, 2, '502E');