#1
class StringStack:
    def __init__(self):
        self.stack = []

    def push(self, string):
        self.stack.append(string)
        print(f"Рядок '{string}' успішно додано до стеку.")

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("Стек порожній. Неможливо виштовхнути рядок.")
            return None

    def count(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def clear(self):
        self.stack = []
        print("Стек очищено.")

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            print("Стек порожній. Немає верхнього рядка.")
            return None

def main():
    stack = StringStack()

    while True:
        print("\nМеню:")
        print("1. Додати рядок до стеку")
        print("2. Виштовхнути рядок зі стеку")
        print("3. Підрахунок кількості рядків у стеку")
        print("4. Перевірити, чи порожній стек")
        print("5. Очистити стек")
        print("6. Отримати верхній рядок без виштовхування")
        print("7. Вийти")
        choice = input("Оберіть операцію: ")

        if choice == '1':
            string = input("Введіть рядок для додавання: ")
            stack.push(string)
        elif choice == '2':
            popped_string = stack.pop()
            if popped_string:
                print("Виштовхнуто рядок:", popped_string)
        elif choice == '3':
            print("Кількість рядків у стеку:", stack.count())
        elif choice == '4':
            if stack.is_empty():
                print("Стек порожній.")
            else:
                print("Стек не порожній.")
        elif choice == '5':
            stack.clear()
        elif choice == '6':
            top_string = stack.peek()
            if top_string:
                print("Верхній рядок у стеку:", top_string)
        elif choice == '7':
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()

#2
class TowerOfHanoi:
    def move_disks(self, n, source, target, auxiliary):
        if n == 1:
            print(f"Перемісти диск 1 з вежі {source} на вежу {target}")
            return
        self.move_disks(n-1, source, auxiliary, target)
        print(f"Перемісти диск {n} з вежі {source} на вежу {target}")
        self.move_disks(n-1, auxiliary, target, source)

def main():
    n = int(input("Введіть кількість дисків: "))
    tower_of_hanoi = TowerOfHanoi()
    tower_of_hanoi.move_disks(n, 'A', 'C', 'B')

if __name__ == "__main__":
    main()
