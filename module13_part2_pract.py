#1
import json
import time

def save_timer_state(timer_state, filename):
    with open(filename, 'w') as f:
        json.dump(timer_state, f)

def load_timer_state(filename):
    try:
        with open(filename, 'r') as f:
            timer_state = json.load(f)
        return timer_state
    except FileNotFoundError:
        return None

def main():
    filename = "timer_state.json"
    timer_state = load_timer_state(filename)

    if timer_state:
        start_time = timer_state['start_time']
        elapsed_time = timer_state['elapsed_time']
        print(f"Завантажений стан таймера. Початковий час: {start_time}, Пройдений час: {elapsed_time} секунд.")
    else:
        start_time = time.time()
        elapsed_time = 0
        print("Стан таймера не знайдено")

    while True:
        input("Натисніть Enter, щоб позначити час.")
        end_time = time.time()
        elapsed_time += end_time - start_time
        start_time = end_time
        print(f"Пройдений час: {elapsed_time} секунд.")

        choice = input("Продовжити (Enter) або завершити (q): ")
        if choice.lower() == 'q':
            break

    timer_state = {'start_time': start_time, 'elapsed_time': elapsed_time}
    save_timer_state(timer_state, filename)
    print("Стан таймера збережено.")

if __name__ == "__main__":
    main()

#2
def load_tasks(filename):
    try:
        with open(filename, 'r') as f:
            tasks = json.load(f)
        return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename):
    with open(filename, 'w') as f:
        json.dump(tasks, f)

def main():
    filename = "tasks.json"
    tasks = load_tasks(filename)

    print("Програма для додавання, видалення та відстеження завдань/заміток.")
    while True:
        print("\nМеню:")
        print("1. Показати завдання")
        print("2. Додати завдання")
        print("3. Видалити завдання")
        print("4. Вийти")

        choice = input("Оберіть опцію: ")

        if choice == '1':
            if tasks:
                print("Список завдань:")
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")
            else:
                print("Список завдань порожній.")
        elif choice == '2':
            new_task = input("Введіть нове завдання: ")
            tasks.append(new_task)
            save_tasks(tasks, filename)
            print("Завдання додано.")
        elif choice == '3':
            if tasks:
                print("Список завдань:")
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")
                index_to_delete = int(input("Введіть номер завдання для видалення: ")) - 1
                if 0 <= index_to_delete < len(tasks):
                    del tasks[index_to_delete]
                    save_tasks(tasks, filename)
                    print("Завдання видалено.")
                else:
                    print("Невірний номер завдання.")
            else:
                print("Список завдань порожній.")
        elif choice == '4':
            print("Дякую за використання програми!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
