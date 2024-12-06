import json
import pickle
#1
def export_orders(orders, filename):
    with open(filename, 'w') as f:
        json.dump(orders, f)

def main():
    orders = [
        {"id": 1, "product": "Laptop", "quantity": 1},
        {"id": 2, "product": "Mouse", "quantity": 2},
        {"id": 3, "product": "Keyboard", "quantity": 1}
    ]
    filename = "orders.json"
    export_orders(orders, filename)
    print("Дані про замовлення експортовано у файл 'orders.json'.")

if __name__ == "__main__":
    main()
def load_orders(filename):
    with open(filename, 'r') as f:
        orders = json.load(f)
    return orders

def process_orders(orders):
    print("Завантажені замовлення:")
    for order in orders:
        print(f"ID: {order['id']}, Товар: {order['product']}, Кількість: {order['quantity']}")

def main():
    filename = "orders.json"
    orders = load_orders(filename)
    if orders:
        process_orders(orders)
    else:
        print("Помилка: не вдалося завантажити дані про замовлення.")

if __name__ == "__main__":
    main()

#2
def load_survey(filename):
    try:
        with open(filename, 'r') as f:
            survey = json.load(f)
        return survey
    except FileNotFoundError:
        return None

def save_survey(survey, filename):
    with open(filename, 'w') as f:
        json.dump(survey, f)

def take_survey():
    survey = {}
    question = input("Введіть питання для опитування: ")
    options = []
    while True:
        option = input("Введіть варіант відповіді (або Enter для завершення): ")
        if option:
            options.append(option)
        else:
            break
    survey['question'] = question
    survey['options'] = options
    return survey

def record_responses(survey):
    responses = []
    while True:
        response = []
        print("\n" + survey['question'])
        for index, option in enumerate(survey['options'], 1):
            print(f"{index}. {option}")
        user_input = input("Виберіть варіант відповіді (або Enter для завершення): ")
        if user_input:
            try:
                choice = int(user_input)
                if 1 <= choice <= len(survey['options']):
                    response.append(survey['options'][choice - 1])
                    responses.append(response)
                else:
                    print("Невірний вибір. Спробуйте ще раз.")
            except ValueError:
                print("Невірний вибір. Спробуйте ще раз.")
        else:
            break
    return responses

def main():
    filename = "survey.json"
    survey = load_survey(filename)

    if not survey:
        print("Опитування не знайдено. Створення нового опитування:")
        survey = take_survey()
        save_survey(survey, filename)

    print("\nПроведення опитування:")
    responses = record_responses(survey)

    print("\nВідповіді користувачів:")
    for index, response in enumerate(responses, 1):
        print(f"{index}. {', '.join(response)}")

if __name__ == "__main__":
    main()


#3
class Stadium:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __repr__(self):
        return f"Stadium(name={self.name}, capacity={self.capacity})"

    def to_json(self):
        return json.dumps({'name': self.name, 'capacity': self.capacity})

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(name=data['name'], capacity=data['capacity'])

    def to_pickle(self):
        return pickle.dumps(self)

    @classmethod
    def from_pickle(cls, pickle_data):
        return pickle.loads(pickle_data)

stadium = Stadium(name="Camp Nou", capacity=99000)

json_data = stadium.to_json()
print("JSON-дані:", json_data)
restored_stadium_json = Stadium.from_json(json_data)
print("Відновлений з JSON:", restored_stadium_json)

pickle_data = stadium.to_pickle()
print("Pickle-дані:", pickle_data)
restored_stadium_pickle = Stadium.from_pickle(pickle_data)
print("Відновлений з pickle:", restored_stadium_pickle)
