CREATE TABLE IF NOT EXISTS Sponsors (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL UNIQUE
);

INSERT INTO Sponsors (Name) VALUES
    ('Sponsor A'),
    ('Sponsor B'),
    ('Sponsor C');

--Відділення (Departments)
CREATE TABLE IF NOT EXISTS Departments (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL UNIQUE
);

INSERT INTO Departments (Name) VALUES
    ('Cardiology'),
    ('Neurology'),
    ('Orthopedics');

--Лікарі (Doctors)
CREATE TABLE IF NOT EXISTS Doctors (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Surname VARCHAR(255) NOT NULL,
    Premium DECIMAL(10, 2) NOT NULL DEFAULT 0,
    Salary DECIMAL(10, 2) NOT NULL,
    DepartmentId INT NOT NULL,
    FOREIGN KEY (DepartmentId) REFERENCES Departments(Id)
);

INSERT INTO Doctors (Name, Surname, Premium, Salary, DepartmentId) VALUES
    ('John', 'Doe', 2000, 50000, 1),
    ('Jane', 'Smith', 1500, 48000, 2),
    ('Michael', 'Johnson', 1800, 52000, 3);

--Спеціалізації (Specializations)
CREATE TABLE IF NOT EXISTS Specializations (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL UNIQUE
);

INSERT INTO Specializations (Name) VALUES
    ('Cardiologist'),
    ('Neurologist'),
    ('Orthopedist');

--Лікарі та спеціалізації (DoctorsSpecializations)
CREATE TABLE IF NOT EXISTS DoctorsSpecializations (
    Id SERIAL PRIMARY KEY,
    DoctorId INT NOT NULL,
    SpecializationId INT NOT NULL,
    FOREIGN KEY (DoctorId) REFERENCES Doctors(Id),
    FOREIGN KEY (SpecializationId) REFERENCES Specializations(Id)
);

-- Припустимо, що лікар John Doe має спеціалізації кардіолога та невролога
INSERT INTO DoctorsSpecializations (DoctorId, SpecializationId) VALUES
    (1, 1),
    (1, 2);

-- Лікар Jane Smith має спеціалізацію невролога
INSERT INTO DoctorsSpecializations (DoctorId, SpecializationId) VALUES
    (2, 2);

-- Лікар Michael Johnson має спеціалізацію ортопеда
INSERT INTO DoctorsSpecializations (DoctorId, SpecializationId) VALUES
    (3, 3);


--Пожертвування (Donations)
CREATE TABLE IF NOT EXISTS Donations (
    Id SERIAL PRIMARY KEY,
    Amount DECIMAL(10, 2) NOT NULL,
    Date DATE NOT NULL DEFAULT CURRENT_DATE,
    DepartmentId INT NOT NULL,
    SponsorId INT NOT NULL,
    FOREIGN KEY (DepartmentId) REFERENCES Departments(Id),
    FOREIGN KEY (SponsorId) REFERENCES Sponsors(Id)
);

INSERT INTO Donations (Amount, DepartmentId, SponsorId) VALUES
    (5000, 1, 1),
    (7000, 2, 2),
    (6000, 3, 3);

--Відпустки (Vacations)
CREATE TABLE IF NOT EXISTS Vacations (
    Id SERIAL PRIMARY KEY,
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    DoctorId INT NOT NULL,
    FOREIGN KEY (DoctorId) REFERENCES Doctors(Id)
);

INSERT INTO Vacations (StartDate, EndDate, DoctorId) VALUES
    ('2024-05-01', '2024-05-10', 1),
    ('2024-06-15', '2024-07-05', 2),
    ('2024-08-20', '2024-08-31', 3);

--Палати (Wards)
CREATE TABLE IF NOT EXISTS Wards (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(20) NOT NULL UNIQUE,
    DepartmentId INT NOT NULL,
    FOREIGN KEY (DepartmentId) REFERENCES Departments(Id)
);

INSERT INTO Wards (Name, DepartmentId) VALUES
    ('Cardiology Ward A', 1),
    ('Neurology Ward B', 2),
    ('Orthopedics Ward C', 3);

CREATE TABLE Visits (
    Id SERIAL PRIMARY KEY,
    VisitDate DATE NOT NULL,
    DoctorId INT NOT NULL,
    FOREIGN KEY (DoctorId) REFERENCES Doctors(Id)
);

INSERT INTO Visits (VisitDate, DoctorId) VALUES
    ('2024-05-05', 1),
    ('2024-05-07', 2),
    ('2024-05-10', 3),
    ('2024-05-15', 1),
    ('2024-05-20', 2);

--1
SELECT CONCAT(D.Name, ' ', D.Surname) AS Full_Name, S.Name AS Specialization
FROM Doctors D
JOIN DoctorsSpecializations DS ON D.Id = DS.DoctorId
JOIN Specializations S ON DS.SpecializationId = S.Id;

--2
SELECT Surname, (Salary + Premium) AS Total_Salary
FROM Doctors
WHERE Id NOT IN (SELECT DoctorId FROM Vacations WHERE CURRENT_DATE BETWEEN StartDate AND EndDate);
--3
SELECT Name
FROM Wards
WHERE DepartmentId = (SELECT Id FROM Departments WHERE Name = 'Intensive Treatment');
--4
SELECT DISTINCT D.Name
FROM Departments D
JOIN Donations DN ON D.Id = DN.DepartmentId
JOIN Sponsors S ON DN.SponsorId = S.Id
WHERE S.Name = 'Umbrella Corporation';
--5
SELECT D.Name AS Department, S.Name AS Sponsor, Amount, DonationDate
FROM Donations DN
JOIN Departments D ON DN.DepartmentId = D.Id
JOIN Sponsors S ON DN.SponsorId = S.Id
WHERE DonationDate >= CURRENT_DATE - INTERVAL '1 MONTH';

--6
SELECT DISTINCT Doc.Surname AS Doctor_Surname, D.Name AS Department_Name
FROM Doctors Doc
JOIN Visits V ON Doc.Id = V.DoctorId
JOIN Departments D ON V.DepartmentId = D.Id
WHERE WEEKDAY(V.VisitDate) BETWEEN 0 AND 4;


--7
SELECT DISTINCT Dpt.Name AS Department_Name, D.Name AS Doctor_Name, D.Surname AS Doctor_Surname
FROM Departments Dpt
JOIN Doctors D ON Dpt.Id = D.DepartmentId
JOIN Donations Dn ON Dpt.Id = Dn.DepartmentId
WHERE Dn.Amount > 100000;
--8
SELECT DISTINCT Dpt.Name AS Department_Name
FROM Departments Dpt
WHERE NOT EXISTS (
    SELECT 1
    FROM Doctors D
    WHERE D.DepartmentId = Dpt.Id AND D.Premium > 0
);
--9
SELECT DISTINCT D.Name AS Department_Name, Dis.Name AS Disease_Name
FROM Departments D
JOIN Wards W ON D.Id = W.DepartmentId
JOIN Visits V ON W.Id = V.DoctorId
JOIN Diseases Dis ON V.DiseaseId = Dis.Id
WHERE V.VisitDate >= (CURRENT_DATE - INTERVAL '6 MONTH');





