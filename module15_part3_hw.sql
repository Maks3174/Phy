CREATE TABLE Departments (
    Id SERIAL PRIMARY KEY,
    Financing MONEY NOT NULL DEFAULT 0,
    Name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Faculties (
    Id SERIAL PRIMARY KEY,
    Dean VARCHAR(255) NOT NULL,
    Name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Groups (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(10) NOT NULL UNIQUE,
    Rating INT NOT NULL CHECK (Rating BETWEEN 0 AND 5),
    Year INT NOT NULL CHECK (Year BETWEEN 1 AND 5)
);

CREATE TABLE Teachers (
    Id SERIAL PRIMARY KEY,
    EmploymentDate DATE NOT NULL CHECK (EmploymentDate >= '1990-01-01'),
    IsAssistant BOOLEAN NOT NULL DEFAULT FALSE,
    IsProfessor BOOLEAN NOT NULL DEFAULT FALSE,
    Name VARCHAR(255) NOT NULL,
    Position VARCHAR(255) NOT NULL,
    Premium MONEY NOT NULL DEFAULT 0,
    Salary MONEY NOT NULL CHECK (Salary > '0'::MONEY),  -- Змінено порівняння на '0'::MONEY
    Surname VARCHAR(255) NOT NULL
);

INSERT INTO Departments (Financing, Name) VALUES
(100000.00, 'Computer Science'),
(120000.00, 'Mathematics'),
(80000.00, 'Physics');

INSERT INTO Faculties (Dean, Name) VALUES
('John Smith', 'Faculty of Science'),
('Emily Johnson', 'Faculty of Mathematics');

INSERT INTO Groups (Name, Rating, Year) VALUES
('CS101', 4, 1),
('MATH101', 5, 1),
('PHYS101', 4, 1);

INSERT INTO Teachers (EmploymentDate, IsAssistant, IsProfessor, Name, Position, Premium, Salary, Surname) VALUES
('2010-05-15', TRUE, FALSE, 'Michael', 'Assistant Professor', 1000.00, 3000.00, 'Johnson'),
('2005-08-20', FALSE, TRUE, 'Emma', 'Professor', 2000.00, 5000.00, 'Williams');

--1
SELECT Id, Name, Financing FROM Departments ORDER BY Id DESC;

--2
SELECT "Name" AS "Group Name", "Rating" AS "Group Rating" FROM Groups;

--3
SELECT "Name" AS "Group Name", "Rating" AS "Group Rating" FROM Groups;

--4
SELECT CONCAT('The dean of faculty ', Name, ' is ', Dean) AS "Faculty Details" FROM Faculties;

--5
SELECT Surname FROM Teachers WHERE IsProfessor = true AND Salary > '1050'::money;

--6
SELECT Name FROM Departments WHERE Financing::numeric < 11000 OR Financing::numeric > 25000;

--7
SELECT Name FROM Faculties WHERE Name != 'Computer Science';

--8
SELECT Surname, Position FROM Teachers WHERE IsProfessor = FALSE;

--9
SELECT Surname, Position, Salary, Premium FROM Teachers WHERE IsAssistant = TRUE AND Premium BETWEEN 160 AND 550;

--10
SELECT Surname, Salary
FROM Teachers
WHERE IsAssistant = TRUE;

--11
SELECT Surname, Position FROM Teachers WHERE EmploymentDate < '2000-01-01';

--12
SELECT "Name" AS "Name of Department" FROM Departments WHERE "Name" < 'Software Development' ORDER BY "Name";

--13
SELECT Surname
FROM Teachers
WHERE IsAssistant = TRUE AND (Salary + Premium) <= 1200::money;

--14
SELECT "Name" AS "Group Name" FROM Groups WHERE "Year" = 5 AND "Rating" BETWEEN 2 AND 4;

--15
SELECT Surname FROM Teachers WHERE IsAssistant = TRUE AND (Salary::numeric::integer < 550 OR Premium::numeric::integer < 200);
