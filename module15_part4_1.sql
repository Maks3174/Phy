--Куратори (Curators)
CREATE TABLE Curators (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR NOT NULL,
    Surname VARCHAR NOT NULL
);

-- Факультети (Faculties)
CREATE TABLE Faculties (
    Id SERIAL PRIMARY KEY,
    Financing DECIMAL(10, 2) NOT NULL CHECK (Financing >= 0) DEFAULT 0,
    Name VARCHAR(100) NOT NULL UNIQUE
);

--Кафедри (Departments)
CREATE TABLE Departments (
    Id SERIAL PRIMARY KEY,
    Financing DECIMAL(10, 2) NOT NULL CHECK (Financing >= 0) DEFAULT 0,
    Name VARCHAR(100) NOT NULL UNIQUE,
    FacultyId INT NOT NULL,
    FOREIGN KEY (FacultyId) REFERENCES Faculties(Id)
);

--Групи (Groups)
CREATE TABLE Groups (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(10) NOT NULL UNIQUE,
    Year INT NOT NULL CHECK (Year BETWEEN 1 AND 5),
    DepartmentId INT NOT NULL,
    FOREIGN KEY (DepartmentId) REFERENCES Departments(Id)
);

--Викладачі (Teachers)
CREATE TABLE Teachers (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR NOT NULL,
    Surname VARCHAR NOT NULL,
    Salary DECIMAL(10, 2) NOT NULL CHECK (Salary > 0)
);

--Предмети (Subjects)
CREATE TABLE Subjects (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL UNIQUE
);

--Лекції (Lectures)
CREATE TABLE Lectures (
    Id SERIAL PRIMARY KEY,
    LectureRoom VARCHAR NOT NULL,
    SubjectId INT NOT NULL,
    TeacherId INT NOT NULL,
    FOREIGN KEY (SubjectId) REFERENCES Subjects(Id),
    FOREIGN KEY (TeacherId) REFERENCES Teachers(Id)
);

--Групи та куратори (GroupsCurators)
CREATE TABLE GroupsCurators (
    Id SERIAL PRIMARY KEY,
    CuratorId INT NOT NULL,
    GroupId INT NOT NULL,
    FOREIGN KEY (CuratorId) REFERENCES Curators(Id),
    FOREIGN KEY (GroupId) REFERENCES Groups(Id)
);

--Групи та лекції (GroupsLectures)
CREATE TABLE GroupsLectures (
    Id SERIAL PRIMARY KEY,
    GroupId INT NOT NULL,
    LectureId INT NOT NULL,
    FOREIGN KEY (GroupId) REFERENCES Groups(Id),
    FOREIGN KEY (LectureId) REFERENCES Lectures(Id)
);

INSERT INTO Curators (Name, Surname) VALUES
('Alexander', 'Ivanenko'),
('Maria', 'Petrova'),
('Sergey', 'Kovalenko');

INSERT INTO Departments (Financing, Name, FacultyId) VALUES
(300000.00, 'Department of Programming', 1),
(200000.00, 'Department of System Analysis', 1),
(150000.00, 'Department of Applied Mathematics', 2),
(100000.00, 'Department of Theoretical Physics', 3);

INSERT INTO Faculties (Financing, Name) VALUES
(1000000.00, 'Faculty of Computer Science'),
(800000.00, 'Faculty of Mathematics'),
(500000.00, 'Faculty of Physics');
INSERT INTO Teachers (Name, Surname, Salary) VALUES
('John', 'Doe', 50000.00),
('Jane', 'Smith', 55000.00),
('James', 'Bond', 60000.00);

INSERT INTO Subjects (Name) VALUES
('Computer Science'),
('Mathematics'),
('Physics');

INSERT INTO Lectures (LectureRoom, SubjectId, TeacherId) VALUES
('Room 101', 1, 1),
('Room 102', 2, 2),
('Room 103', 3, 3);


INSERT INTO Groups (Name, Year, DepartmentId) VALUES
('CS-101', 1, 1),
('MATH-101', 1, 2),
('PHYS-101', 1, 3);

INSERT INTO GroupsCurators (CuratorId, GroupId) VALUES
(1, 1),
(2, 2),
(3, 3);

INSERT INTO GroupsLectures (GroupId, LectureId) VALUES
(1, 1),
(2, 2),
(3, 3);

--1
SELECT Teachers.Name AS TeacherName, Groups.Name AS GroupName
FROM Teachers, Groups;
--2
SELECT F1.Name AS FacultyName, D1.Name AS DepartmentName, F1.Financing AS FacultyFinancing, D1.Financing AS DepartmentFinancing
FROM Departments D1
JOIN Faculties F1 ON D1.FacultyId = F1.Id
JOIN (
    SELECT F2.Id, MAX(D2.Financing) AS MaxDepartmentFinancing
    FROM Faculties F2
    JOIN Departments D2 ON F2.Id = D2.FacultyId
    GROUP BY F2.Id
) AS MaxFinancing ON F1.Id = MaxFinancing.Id
WHERE D1.Financing > MaxFinancing.MaxDepartmentFinancing;

--3
SELECT C.Surname AS CuratorSurname, G.Name AS GroupName
FROM GroupsCurators GC
JOIN Curators C ON GC.CuratorId = C.Id
JOIN Groups G ON GC.GroupId = G.Id;

--4
SELECT T.Name AS TeacherName, T.Surname AS TeacherSurname
FROM Teachers T
JOIN Lectures L ON T.Id = L.TeacherId
JOIN GroupsLectures GL ON L.Id = GL.LectureId
JOIN Groups G ON GL.GroupId = G.Id
WHERE G.Name = 'P107';

--5
SELECT T.Surname AS TeacherSurname, F.Name AS FacultyName
FROM Teachers T
JOIN Lectures L ON T.Id = L.TeacherId
JOIN Subjects S ON L.SubjectId = S.Id
JOIN Departments D ON S.Id = D.Id
JOIN Faculties F ON D.FacultyId = F.Id;

--6
SELECT D.Name AS DepartmentName, G.Name AS GroupName
FROM Departments D
JOIN Groups G ON D.Id = G.DepartmentId;
--7
SELECT S.Name AS SubjectName
FROM Teachers T
JOIN Lectures L ON T.Id = L.TeacherId
JOIN Subjects S ON L.SubjectId = S.Id
WHERE T.Name = 'Samantha' AND T.Surname = 'Adams';

--8
SELECT D.Name AS DepartmentName
FROM Departments D
JOIN Subjects S ON D.Id = S.Id
WHERE S.Name = 'Database Theory';

--9
SELECT G.Name AS GroupName
FROM Groups G
JOIN Departments D ON G.DepartmentId = D.Id
JOIN Faculties F ON D.FacultyId = F.Id
WHERE F.Name = 'Computer Science';

--10
SELECT G.Name AS GroupName, F.Name AS FacultyName
FROM Groups G
JOIN Departments D ON G.DepartmentId = D.Id
JOIN Faculties F ON D.FacultyId = F.Id
WHERE G.Year = 5;

--11
SELECT T.Name AS TeacherName, T.Surname AS TeacherSurname, L.LectureRoom, S.Name AS SubjectName, G.Name AS GroupName
FROM Teachers T
JOIN Lectures L ON T.Id = L.TeacherId
JOIN Subjects S ON L.SubjectId = S.Id
JOIN GroupsLectures GL ON L.Id = GL.LectureId
JOIN Groups G ON GL.GroupId = G.Id
WHERE L.LectureRoom = 'B103';
