from sqlalchemy import create_engine, Column, Integer, String, Date, text
from sqlalchemy.orm import declarative_base, sessionmaker
import json
from datetime import date
import os

with open('config.json', 'r') as f:
    data = json.load(f)
    db_user = data['user']
    db_password = data['password']

db_url = f'postgresql+psycopg2://{db_user}:{db_password}@localhost:5432/peopledb'
engine = create_engine(db_url)

Base = declarative_base()


class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    city = Column(String(50))
    country = Column(String(50))
    birth_date = Column(Date)


Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


def populate_data():
    people_data = [
        People(first_name='John', last_name='Doe', city='New York', country='USA', birth_date=date(1990, 5, 15)),
        People(first_name='Jane', last_name='Smith', city='Los Angeles', country='USA', birth_date=date(1985, 6, 20)),
        People(first_name='Maria', last_name='Garcia', city='Madrid', country='Spain', birth_date=date(1992, 7, 10)),
        People(first_name='Anna', last_name='Müller', city='Berlin', country='Germany', birth_date=date(1988, 3, 5))
    ]

    session.bulk_save_objects(people_data)
    session.commit()
    print("Таблиця заповнена даними.")


populate_data()


#3,4
def display_all_people():
    query = "SELECT * FROM people"
    execute_select_query(query)


def display_people_by_filters(city=None, country=None):
    conditions = []
    params = {}

    if city:
        conditions.append("city = :city")
        params["city"] = city
    if country:
        conditions.append("country = :country")
        params["country"] = country

    if conditions:
        query = f"SELECT * FROM people WHERE {' OR '.join(conditions)}"
    else:
        query = "SELECT * FROM people"

    execute_select_query(query, params)


#1
def execute_select_query(query, params=None):
    with engine.connect() as connection:
        if params:
            result = connection.execute(text(query), params)
        else:
            result = connection.execute(text(query))

        results = result.fetchall()
        for row in results:
            print(row)
        return results


#6
def save_results_to_file(results, filename):
    with open(filename, 'w') as f:
        for row in results:
            f.write(f"{row}\n")
    print(f"Результати збережено у файл {filename}")


# 2
def execute_query(query):
    allowed_commands = ['select', 'insert', 'update', 'delete']
    command = query.strip().split()[0].lower()

    if command not in allowed_commands:
        raise ValueError("Тільки SELECT, INSERT, UPDATE та DELETE запити дозволені.")

    if 'people' not in query.lower():
        raise ValueError("Запит має стосуватися тільки таблиці 'people'.")

    if (command == 'delete' or command == 'update') and 'where' not in query.lower():
        raise ValueError("DELETE та UPDATE запити мають містити умову WHERE.")

    with engine.connect() as connection:
        result = connection.execute(text(query))

        if command == 'select':
            results = result.fetchall()
            for row in results:
                print(row)
            return results
        else:
            print(f"Запит '{command.upper()}' виконано успішно.")


if __name__ == "__main__":
    results = None
    while True:
        print("\nВиберіть опцію:")
        print("1. Відображення всіх людей")  #3
        print("2. Відображення людей з фільтрами")  #3, 4
        print("3. Додати нову людину")  #5
        print("4. Оновити інформацію про людину")  #5
        print("5. Видалити людину")  #5
        print("6. Зберегти результати у файл")  #6
        print("7. Вихід")

        choice = input("Ваш вибір: ").strip()

        if choice == '1':
            results = display_all_people()
        elif choice == '2':
            city = input("Введіть назву міста (або залиште порожнім): ").strip()
            country = input("Введіть назву країни (або залиште порожнім): ").strip()
            results = display_people_by_filters(city if city else None, country if country else None)
        elif choice == '3':
            first_name = input("Введіть ім'я: ").strip()
            last_name = input("Введіть прізвище: ").strip()
            city = input("Введіть місто: ").strip()
            country = input("Введіть країну: ").strip()
            birth_date = input("Введіть дату народження (YYYY-MM-DD): ").strip()
            query = f"INSERT INTO people (first_name, last_name, city, country, birth_date) VALUES ('{first_name}', '{last_name}', '{city}', '{country}', '{birth_date}')"
            execute_query(query)
        elif choice == '4':
            person_id = input("Введіть ID людини, яку ви хочете оновити: ").strip()
            column = input(
                "Введіть назву колонки для оновлення (first_name, last_name, city, country, birth_date): ").strip()
            new_value = input(f"Введіть нове значення для {column}: ").strip()
            query = f"UPDATE people SET {column} = '{new_value}' WHERE id = {person_id}"
            execute_query(query)
        elif choice == '5':
            person_id = input("Введіть ID людини, яку ви хочете видалити: ").strip()
            query = f"DELETE FROM people WHERE id = {person_id}"
            execute_query(query)
        elif choice == '6':
            if not results:
                print("Немає результатів для збереження.")
            else:
                filename = input("Введіть назву файлу для збереження результатів: ").strip()
                save_results_to_file(results, filename)
        elif choice == '7':
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")
