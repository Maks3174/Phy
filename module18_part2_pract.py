from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DECIMAL, ForeignKey, inspect, text
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

# Функції для завдання 1
def insert_row(table_name, data):
    table = Table(table_name, metadata, autoload_with=engine)
    insert_stmt = table.insert().values(data)
    session.execute(insert_stmt)
    session.commit()
    print(f"Row inserted into {table_name}")

def update_rows(table_name, update_values, condition=None):
    table = Table(table_name, metadata, autoload_with=engine)
    update_stmt = table.update()
    if condition:
        update_stmt = update_stmt.where(text(condition))
    update_stmt = update_stmt.values(update_values)
    session.execute(update_stmt)
    session.commit()
    print(f"Rows updated in {table_name}")

def delete_rows(table_name, condition=None):
    table = Table(table_name, metadata, autoload_with=engine)
    delete_stmt = table.delete()
    if condition:
        delete_stmt = delete_stmt.where(text(condition))
    session.execute(delete_stmt)
    session.commit()
    print(f"Rows deleted from {table_name}")

def confirm_action(message):
    confirm = input(message + " (yes/no): ")
    return confirm.lower() in ['yes', 'y']

# Функції для завдання 2
def report_doctors_specializations():
    result = session.execute(text("""
        SELECT doctors.surname, specializations.name
        FROM doctors
        JOIN doctor_specializations ON doctors.id = doctor_specializations.doctor_id
        JOIN specializations ON doctor_specializations.specialization_id = specializations.id
    """)).fetchall()
    for row in result:
        print(f"{row.surname}: {row.name}")

def report_doctors_salaries():
    result = session.execute(text("""
        SELECT surname, (salary + allowance) as total_salary
        FROM doctors
        WHERE vacation = false
    """)).fetchall()
    for row in result:
        print(f"{row.surname}: {row.total_salary}")

def report_wards_in_department(department_name):
    result = session.execute(text("""
        SELECT wards.name
        FROM wards
        JOIN departments ON wards.department_id = departments.id
        WHERE departments.name = :dept_name
    """), {'dept_name': department_name}).fetchall()
    for row in result:
        print(row.name)

def report_donations_by_month(month):
    result = session.execute(text("""
        SELECT departments.name as department, sponsors.name as sponsor, donations.amount, donations.date
        FROM donations
        JOIN departments ON donations.department_id = departments.id
        JOIN sponsors ON donations.sponsor_id = sponsors.id
        WHERE EXTRACT(MONTH FROM donations.date) = :month
    """), {'month': month}).fetchall()
    for row in result:
        print(f"Department: {row.department}, Sponsor: {row.sponsor}, Amount: {row.amount}, Date: {row.date}")

def report_departments_by_sponsor(sponsor_name):
    result = session.execute(text("""
        SELECT DISTINCT departments.name
        FROM departments
        JOIN donations ON departments.id = donations.department_id
        JOIN sponsors ON donations.sponsor_id = sponsors.id
        WHERE sponsors.name = :sponsor_name
    """), {'sponsor_name': sponsor_name}).fetchall()
    for row in result:
        print(row.name)

# Функції для завдання 3 (Робота зі структурою бази даних)
def show_tables():
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print("Tables in the database:")
    for table in tables:
        print(table)

def show_columns(table_name):
    inspector = inspect(engine)
    columns = inspector.get_columns(table_name)
    print(f"Columns in table {table_name}:")
    for column in columns:
        print(column['name'])

def show_columns_and_types(table_name):
    inspector = inspect(engine)
    columns = inspector.get_columns(table_name)
    print(f"Columns and their types in table {table_name}:")
    for column in columns:
        print(f"{column['name']} - {column['type']}")

def show_relationships():
    inspector = inspect(engine)
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
        print("\nDatabase Management System for 'Hospital'")
        print("1. Insert a row into a table")
        print("2. Update rows in a table")
        print("3. Delete rows from a table")
        print("4. Generate reports")
        print("5. Database structure operations")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            table_name = input("Enter the table name: ")
            data = input("Enter data as key=value pairs separated by commas: ")
            data_dict = dict(pair.split('=') for pair in data.split(','))
            insert_row(table_name, data_dict)

        elif choice == '2':
            table_name = input("Enter the table name: ")
            update_values = input("Enter update values as key=value pairs separated by commas: ")
            update_dict = dict(pair.split('=') for pair in update_values.split(','))
            condition = input("Enter condition (or leave blank to update all rows): ")
            if not condition:
                if confirm_action("Are you sure you want to update all rows in the table?"):
                    update_rows(table_name, update_dict)
                else:
                    print("Update canceled.")
            else:
                update_rows(table_name, update_dict, condition)

        elif choice == '3':
            table_name = input("Enter the table name: ")
            condition = input("Enter condition (or leave blank to delete all rows): ")
            if not condition:
                if confirm_action("Are you sure you want to delete all rows in the table?"):
                    delete_rows(table_name)
                else:
                    print("Delete canceled.")
            else:
                delete_rows(table_name, condition)

        elif choice == '4':
            print("1. Report doctors and their specializations")
            print("2. Report doctors and their salaries (excluding those on vacation)")
            print("3. Report wards in a specific department")
            print("4. Report donations for a specific month")
            print("5. Report departments sponsored by a specific company")
            report_choice = input("Enter your choice: ")
            if report_choice == '1':
                report_doctors_specializations()
            elif report_choice== '2':
                report_doctors_salaries()
            elif report_choice == '3':
                department_name = input("Enter the department name: ")
                report_wards_in_department(department_name)
            elif report_choice == '4':
                month = input("Enter the month (as a number): ")
                report_donations_by_month(month)
            elif report_choice == '5':
                sponsor_name = input("Enter the sponsor company name: ")
                report_departments_by_sponsor(sponsor_name)
            else:
                print("Invalid choice.")

        elif choice == '5':
            print("1. Show tables")
            print("2. Show columns of a table")
            print("3. Show columns and their types of a table")
            print("4. Show foreign key relationships")
            print("5. Create a new table")
            print("6. Drop a table")
            print("7. Add a column to a table")
            print("8. Drop a column from a table")
            operation_choice = input("Enter your choice: ")
            if operation_choice == '1':
                show_tables()
            elif operation_choice == '2':
                table_name = input("Enter the table name: ")
                show_columns(table_name)
            elif operation_choice == '3':
                table_name = input("Enter the table name: ")
                show_columns_and_types(table_name)
            elif operation_choice == '4':
                show_relationships()
            elif operation_choice == '5':
                table_name = input("Enter the new table name: ")
                columns = input("Enter columns and their types separated by commas (e.g., id:Integer,name:String): ")
                create_table(table_name, columns.split(','))
            elif operation_choice == '6':
                table_name = input("Enter the table name to drop: ")
                drop_table(table_name)
            elif operation_choice == '7':
                table_name = input("Enter the table name to add column: ")
                column_name = input("Enter the new column name: ")
                column_type = input("Enter the column type (Integer/String/DECIMAL): ")
                add_column(table_name, column_name, column_type)
            elif operation_choice == '8':
                table_name = input("Enter the table name to drop column: ")
                column_name = input("Enter the column name to drop: ")
                drop_column(table_name, column_name)
            else:
                print("Invalid choice.")

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main_menu()

