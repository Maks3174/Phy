from sqlalchemy import create_engine, Column, Integer, String, DECIMAL, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

with open('config.json', 'r') as f:
    data = json.load(f)
    db_user = data['user']
    db_password = data['password']

db_url = f'postgresql+psycopg2://{db_user}:{db_password}@localhost:5432/Title'
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Department(Base):
    __tablename__ = 'departments'
    Id = Column(Integer, primary_key=True)
    Building = Column(Integer, nullable=False)
    Financing = Column(DECIMAL(10, 2), nullable=False, default=0)
    Name = Column(String(100), nullable=False, unique=True)
    __table_args__ = (
        CheckConstraint('Building >= 1 AND Building <= 5'),
        CheckConstraint('Financing >= 0'),
    )


Base.metadata.create_all(engine)


def insert_department(building, financing, name):
    new_department = Department(Building=building, Financing=financing, Name=name)
    session.add(new_department)
    session.commit()


def update_department(department_id, building=None, financing=None, name=None):
    department = session.query(Department).filter_by(Id=department_id).first()
    if department:
        if building is not None:
            department.Building = building
        if financing is not None:
            department.Financing = financing
        if name is not None:
            department.Name = name
        session.commit()


def update_all_departments(building=None, financing=None, name=None):
    confirmation = input("Are you sure you want to update all rows in Departments? (yes/no): ")
    if confirmation.lower() != 'yes':
        print("Operation cancelled.")
        return

    departments = session.query(Department).all()
    for department in departments:
        if building is not None:
            department.Building = building
        if financing is not None:
            department.Financing = financing
        if name is not None:
            department.Name = name
    session.commit()


def delete_department(department_id):
    department = session.query(Department).filter_by(Id=department_id).first()
    if department:
        session.delete(department)
        session.commit()


def delete_all_departments():
    confirmation = input("Are you sure you want to delete all rows in Departments? (yes/no): ")
    if confirmation.lower() != 'yes':
        print("Operation cancelled.")
        return

    session.query(Department).delete()
    session.commit()


def main_menu():
    while True:
        print("\nHospital Database Management")
        print("1. Insert Department")
        print("2. Update Department")
        print("3. Update All Departments")
        print("4. Delete Department")
        print("5. Delete All Departments")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            building = int(input("Enter building number (1-5): "))
            financing = float(input("Enter financing amount: "))
            name = input("Enter department name: ")
            insert_department(building, financing, name)
            print("Department inserted successfully.")

        elif choice == '2':
            department_id = int(input("Enter department ID to update: "))
            building = input("Enter new building number (leave blank to keep current): ")
            financing = input("Enter new financing amount (leave blank to keep current): ")
            name = input("Enter new department name (leave blank to keep current): ")

            update_department(
                department_id,
                building=int(building) if building else None,
                financing=float(financing) if financing else None,
                name=name if name else None
            )
            print("Department updated successfully.")

        elif choice == '3':
            building = input("Enter new building number for all departments (leave blank to keep current): ")
            financing = input("Enter new financing amount for all departments (leave blank to keep current): ")
            name = input("Enter new name for all departments (leave blank to keep current): ")

            update_all_departments(
                building=int(building) if building else None,
                financing=float(financing) if financing else None,
                name=name if name else None
            )
            print("All departments updated successfully.")

        elif choice == '4':
            department_id = int(input("Enter department ID to delete: "))
            delete_department(department_id)
            print("Department deleted successfully.")

        elif choice == '5':
            delete_all_departments()
            print("All departments deleted successfully.")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main_menu()

#2
from sqlalchemy import create_engine, Column, Integer, String, DECIMAL, Boolean, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import json

with open('config.json', 'r') as f:
    data = json.load(f)
    db_user = data['user']
    db_password = data['password']

db_url = f'postgresql+psycopg2://{db_user}:{db_password}@localhost:5432/Title'
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Department(Base):
    __tablename__ = 'departments'
    Id = Column(Integer, primary_key=True)
    Building = Column(Integer, nullable=False)
    Financing = Column(DECIMAL(10, 2), nullable=False, default=0)
    Name = Column(String(100), nullable=False, unique=True)

class Doctor(Base):
    __tablename__ = 'doctors'
    Id = Column(Integer, primary_key=True)
    Name = Column(String(255), nullable=False)
    Phone = Column(String(10))
    Salary = Column(DECIMAL(10, 2), nullable=False)
    Surname = Column(String(255), nullable=False)
    OnVacation = Column(Boolean, nullable=False, default=False)
    Allowance = Column(DECIMAL(10, 2), nullable=False, default=0)

class Specialization(Base):
    __tablename__ = 'specializations'
    Id = Column(Integer, primary_key=True)
    Name = Column(String(100), nullable=False, unique=True)

class DoctorSpecialization(Base):
    __tablename__ = 'doctorsspecializations'
    DoctorId = Column(Integer, ForeignKey('doctors.Id'), primary_key=True)
    SpecializationId = Column(Integer, ForeignKey('specializations.Id'), primary_key=True)

class Ward(Base):
    __tablename__ = 'wards'
    Id = Column(Integer, primary_key=True)
    Building = Column(Integer, nullable=False)
    Floor = Column(Integer, nullable=False)
    Name = Column(String(20), nullable=False, unique=True)
    DepartmentId = Column(Integer, ForeignKey('departments.Id'))

class Donation(Base):
    __tablename__ = 'donations'
    Id = Column(Integer, primary_key=True)
    DepartmentId = Column(Integer, ForeignKey('departments.Id'), nullable=False)
    Sponsor = Column(String(100), nullable=False)
    Amount = Column(DECIMAL(10, 2), nullable=False)
    DonationDate = Column(Date, nullable=False)

Base.metadata.create_all(engine)

def get_doctors_specializations():
    results = session.query(Doctor.Surname, Specialization.Name).\
              join(DoctorSpecialization, Doctor.Id == DoctorSpecialization.DoctorId).\
              join(Specialization, Specialization.Id == DoctorSpecialization.SpecializationId).all()
    for surname, specialization in results:
        print(f"Doctor: {surname}, Specialization: {specialization}")

def get_doctors_salaries_not_on_vacation():
    results = session.query(Doctor.Surname, (Doctor.Salary + Doctor.Allowance).label('TotalSalary')).\
              filter(Doctor.OnVacation == False).all()
    for surname, total_salary in results:
        print(f"Doctor: {surname}, Total Salary: {total_salary}")

def get_wards_in_department(department_id):
    results = session.query(Ward.Name).filter(Ward.DepartmentId == department_id).all()
    for ward_name in results:
        print(f"Ward: {ward_name}")

def get_donations_by_month(year, month):
    results = session.query(Department.Name, Donation.Sponsor, Donation.Amount, Donation.DonationDate).\
              join(Department, Department.Id == Donation.DepartmentId).\
              filter(Donation.DonationDate.between(f'{year}-{month}-01', f'{year}-{month}-31')).all()
    for department_name, sponsor, amount, donation_date in results:
        print(f"Department: {department_name}, Sponsor: {sponsor}, Amount: {amount}, Date: {donation_date}")

def get_departments_by_sponsor(sponsor):
    results = session.query(Department.Name).\
              join(Donation, Donation.DepartmentId == Department.Id).\
              filter(Donation.Sponsor == sponsor).distinct().all()
    for department_name in results:
        print(f"Department: {department_name}")

def main_menu():
    while True:
        print("\nHospital Database Reports")
        print("1. Show Doctors and their Specializations")
        print("2. Show Doctors' Surnames and Salaries (not on vacation)")
        print("3. Show Ward Names in a Department")
        print("4. Show Donations by Month")
        print("5. Show Departments Sponsored by a Company")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            get_doctors_specializations()

        elif choice == '2':
            get_doctors_salaries_not_on_vacation()

        elif choice == '3':
            department_id = int(input("Enter department ID: "))
            get_wards_in_department(department_id)

        elif choice == '4':
            year = int(input("Enter year (YYYY): "))
            month = int(input("Enter month (MM): "))
            get_donations_by_month(year, month)

        elif choice == '5':
            sponsor = input("Enter sponsor name: ")
            get_departments_by_sponsor(sponsor)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main_menu()


#3
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DECIMAL
from sqlalchemy.orm import sessionmaker
import json

with open('config.json', 'r') as f:
    data = json.load(f)
    db_user = data['user']
    db_password = data['password']

db_url = f'postgresql+psycopg2://{db_user}:{db_password}@localhost:5432/Title'
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData(bind=engine)

def show_tables():
    tables = engine.table_names()
    print("Tables in the database:")
    for table in tables:
        print(table)

def show_columns(table_name):
    table = Table(table_name, metadata, autoload_with=engine)
    print(f"Columns in table {table_name}:")
    for column in table.columns:
        print(column.name)

def show_columns_and_types(table_name):
    table = Table(table_name, metadata, autoload_with=engine)
    print(f"Columns and their types in table {table_name}:")
    for column in table.columns:
        print(f"{column.name} - {column.type}")

def show_relationships():
    inspector = engine.dialect.get_inspector(engine)
    print("Foreign key relationships:")
    for table_name in inspector.get_table_names():
        foreign_keys = inspector.get_foreign_keys(table_name)
        for fk in foreign_keys:
            print(f"Table {table_name} has a foreign key to {fk['referred_table']}")

def create_table(table_name, columns):
    columns_definitions = []
    for column in columns:
        col_name, col_type = column.split(':')
        if col_type == 'Integer':
            columns_definitions.append(Column(col_name, Integer))
        elif col_type == 'String':
            columns_definitions.append(Column(col_name, String))
        elif col_type == 'DECIMAL':
            columns_definitions.append(Column(col_name, DECIMAL))
        else:
            print(f"Unsupported column type: {col_type}")
            return
    new_table = Table(table_name, metadata, *columns_definitions)
    new_table.create()
    print(f"Table {table_name} created successfully.")

def drop_table(table_name):
    table = Table(table_name, metadata, autoload_with=engine)
    table.drop()
    print(f"Table {table_name} dropped successfully.")

def add_column(table_name, column_name, column_type):
    table = Table(table_name, metadata, autoload_with=engine)
    if column_type == 'Integer':
        new_column = Column(column_name, Integer)
    elif column_type == 'String':
        new_column = Column(column_name, String)
    elif column_type == 'DECIMAL':
        new_column = Column(column_name, DECIMAL)
    else:
        print(f"Unsupported column type: {column_type}")
        return
    new_column.create(table)
    print(f"Column {column_name} added to table {table_name}.")

def drop_column(table_name, column_name):
    table = Table(table_name, metadata, autoload_with=engine)
    column = table.c[column_name]
    column.drop()
    print(f"Column {column_name} dropped from table {table_name}.")

def main_menu():
    while True:
        print("\nDatabase Structure Management")
        print("1. Show all tables")
        print("2. Show columns in a table")
        print("3. Show columns and their types in a table")
        print("4. Show relationships between tables")
        print("5. Create a table")
        print("6. Drop a table")
        print("7. Add a column to a table")
        print("8. Drop a column from a table")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_tables()

        elif choice == '2':
            table_name = input("Enter the table name: ")
            show_columns(table_name)

        elif choice == '3':
            table_name = input("Enter the table name: ")
            show_columns_and_types(table_name)

        elif choice == '4':
            show_relationships()

        elif choice == '5':
            table_name = input("Enter the table name: ")
            columns = input("Enter columns (name:type, separated by commas): ").split(',')
            create_table(table_name, columns)

        elif choice == '6':
            table_name = input("Enter the table name: ")
            drop_table(table_name)

        elif choice == '7':
            table_name = input("Enter the table name: ")
            column_name = input("Enter the column name: ")
            column_type = input("Enter the column type (Integer, String, DECIMAL): ")
            add_column(table_name, column_name, column_type)

        elif choice == '8':
            table_name = input("Enter the table name: ")
            column_name = input("Enter the column name: ")
            drop_column(table_name, column_name)

        elif choice == '9':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main_menu()
