import tkinter as tk
from tkinter import messagebox, simpledialog
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, func, text
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import date
import json
import os

with open('config.json', 'r') as f:
    data = json.load(f)
    db_user = data['user']
    db_password = data['password']

db_url = f'postgresql+psycopg2://{db_user}:{db_password}@localhost:5432/academy'
engine = create_engine(db_url)

Base = declarative_base()

class Department(Base):
    __tablename__ = 'Departments'
    DepartmentID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String, nullable=False)

class Teacher(Base):
    __tablename__ = 'Teachers'
    TeacherID = Column(Integer, primary_key=True, autoincrement=True)
    FirstName = Column(String, nullable=False)
    LastName = Column(String, nullable=False)
    DepartmentID = Column(Integer, ForeignKey('Departments.DepartmentID'))

class Group(Base):
    __tablename__ = 'Groups'
    GroupID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String, nullable=False)
    DepartmentID = Column(Integer, ForeignKey('Departments.DepartmentID'))

class Subject(Base):
    __tablename__ = 'Subjects'
    SubjectID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String, nullable=False)
    DepartmentID = Column(Integer, ForeignKey('Departments.DepartmentID'))

class Lecture(Base):
    __tablename__ = 'Lectures'
    LectureID = Column(Integer, primary_key=True, autoincrement=True)
    TeacherID = Column(Integer, ForeignKey('Teachers.TeacherID'))
    SubjectID = Column(Integer, ForeignKey('Subjects.SubjectID'))
    GroupID = Column(Integer, ForeignKey('Groups.GroupID'))

# Initialize database
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

class AcademyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Academy Database Management")
        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        data_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Data", menu=data_menu)
        data_menu.add_command(label="Insert", command=self.insert_data)
        data_menu.add_command(label="Update", command=self.update_data)
        data_menu.add_command(label="Delete", command=self.delete_data)

        report_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Reports", menu=report_menu)
        report_menu.add_command(label="View All Groups", command=self.view_all_groups)
        report_menu.add_command(label="View All Teachers", command=self.view_all_teachers)
        report_menu.add_command(label="View All Departments", command=self.view_all_departments)
        report_menu.add_command(label="View Teachers by Group", command=self.view_teachers_by_group)
        report_menu.add_command(label="View Departments and Groups", command=self.view_departments_and_groups)
        report_menu.add_command(label="Department with Max Groups", command=self.department_with_max_groups)
        report_menu.add_command(label="Department with Min Groups", command=self.department_with_min_groups)
        report_menu.add_command(label="Subjects by Teacher", command=self.subjects_by_teacher)
        report_menu.add_command(label="Departments by Subject", command=self.departments_by_subject)
        report_menu.add_command(label="Groups by Faculty", command=self.groups_by_faculty)
        report_menu.add_command(label="Subjects and Teachers with Most Lectures", command=self.subjects_and_teachers_with_most_lectures)
        report_menu.add_command(label="Subject with Fewest Lectures", command=self.subject_with_fewest_lectures)
        report_menu.add_command(label="Subject with Most Lectures", command=self.subject_with_most_lectures)

    def insert_data(self):
        table = simpledialog.askstring("Input", "Enter table name (Departments, Teachers, Groups, Subjects, Lectures):")
        if table == "Departments":
            name = simpledialog.askstring("Input", "Enter Department Name:")
            new_department = Department(Name=name)
            session.add(new_department)
        elif table == "Teachers":
            first_name = simpledialog.askstring("Input", "Enter First Name:")
            last_name = simpledialog.askstring("Input", "Enter Last Name:")
            department_id = simpledialog.askinteger("Input", "Enter Department ID:")
            new_teacher = Teacher(FirstName=first_name, LastName=last_name, DepartmentID=department_id)
            session.add(new_teacher)
        elif table == "Groups":
            name = simpledialog.askstring("Input", "Enter Group Name:")
            department_id = simpledialog.askinteger("Input", "Enter Department ID:")
            new_group = Group(Name=name, DepartmentID=department_id)
            session.add(new_group)
        elif table == "Subjects":
            name = simpledialog.askstring("Input", "Enter Subject Name:")
            department_id = simpledialog.askinteger("Input", "Enter Department ID:")
            new_subject = Subject(Name=name, DepartmentID=department_id)
            session.add(new_subject)
        elif table == "Lectures":
            teacher_id = simpledialog.askinteger("Input", "Enter Teacher ID:")
            subject_id = simpledialog.askinteger("Input", "Enter Subject ID:")
            group_id = simpledialog.askinteger("Input", "Enter Group ID:")
            new_lecture = Lecture(TeacherID=teacher_id, SubjectID=subject_id, GroupID=group_id)
            session.add(new_lecture)
        else:
            messagebox.showerror("Error", "Invalid table name")
            return
        session.commit()
        messagebox.showinfo("Success", "Data inserted successfully")

    def update_data(self):
        table = simpledialog.askstring("Input", "Enter table name (Departments, Teachers, Groups, Subjects, Lectures):")
        row_id = simpledialog.askinteger("Input", f"Enter {table[:-1]} ID:")
        if table == "Departments":
            department = session.query(Department).filter(Department.DepartmentID == row_id).first()
            if department:
                name = simpledialog.askstring("Input", "Enter new Department Name:", initialvalue=department.Name)
                department.Name = name
        elif table == "Teachers":
            teacher = session.query(Teacher).filter(Teacher.TeacherID == row_id).first()
            if teacher:
                first_name = simpledialog.askstring("Input", "Enter new First Name:", initialvalue=teacher.FirstName)
                last_name = simpledialog.askstring("Input", "Enter new Last Name:", initialvalue=teacher.LastName)
                department_id = simpledialog.askinteger("Input", "Enter new Department ID:", initialvalue=teacher.DepartmentID)
                teacher.FirstName = first_name
                teacher.LastName = last_name
                teacher.DepartmentID = department_id
        elif table == "Groups":
            group = session.query(Group).filter(Group.GroupID == row_id).first()
            if group:
                name = simpledialog.askstring("Input", "Enter new Group Name:", initialvalue=group.Name)
                department_id = simpledialog.askinteger("Input", "Enter new Department ID:", initialvalue=group.DepartmentID)
                group.Name = name
                group.DepartmentID = department_id
        elif table == "Subjects":
            subject = session.query(Subject).filter(Subject.SubjectID == row_id).first()
            if subject:
                name = simpledialog.askstring("Input", "Enter new Subject Name:", initialvalue=subject.Name)
                department_id = simpledialog.askinteger("Input", "Enter new Department ID:", initialvalue=subject.DepartmentID)
                subject.Name = name
                subject.DepartmentID = department_id
        elif table == "Lectures":
            lecture = session.query(Lecture).filter(Lecture.LectureID == row_id).first()
            if lecture:
                teacher_id = simpledialog.askinteger("Input", "Enter new Teacher ID:", initialvalue=lecture.TeacherID)
                subject_id = simpledialog.askinteger("Input", "Enter new Subject ID:", initialvalue=lecture.SubjectID)
                group_id = simpledialog.askinteger("Input", "Enter new Group ID:", initialvalue=lecture.GroupID)
                lecture.TeacherID = teacher_id
                lecture.SubjectID = subject_id
                lecture.GroupID = group_id
        else:
            messagebox.showerror("Error", "Invalid table name")
            return
        session.commit()
        messagebox.showinfo("Success", "Data updated successfully")

    def delete_data(self):
        table = simpledialog.askstring("Input", "Enter table name (Departments, Teachers, Groups, Subjects, Lectures):")
        row_id = simpledialog.askinteger("Input", f"Enter {table[:-1]} ID:")
        if table == "Departments":
            department = session.query(Department).filter(Department.DepartmentID == row_id).first()
            if department:
                session.delete(department)
        elif table == "Teachers":
            teacher = session.query(Teacher).filter(Teacher.TeacherID == row_id).first()
            if teacher:
                session.delete(teacher)
        elif table == "Groups":
            group = session.query(Group).filter(Group.GroupID == row_id).first()
            if group:
                session.delete(group)
        elif table == "Subjects":
            subject = session.query(Subject).filter(Subject.SubjectID == row_id).first()
            if subject:
                session.delete(subject)
        elif table == "Lectures":
            lecture = session.query(Lecture).filter(Lecture.LectureID == row_id).first()
            if lecture:
                session.delete(lecture)
        else:
            messagebox.showerror("Error", "Invalid table name")
            return
        session.commit()
        messagebox.showinfo("Success", "Data deleted successfully")


if __name__ == "__main__":
    root = tk.Tk()
    app = AcademyApp(root)
    root.mainloop()

