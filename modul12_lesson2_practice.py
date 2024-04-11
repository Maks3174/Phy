class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


class WebHistory:
    def __init__(self):
        self.stack = Stack()

    def visit_page(self, page):
        self.stack.push(page)
        print(f"Відвідана сторінка: {page}")

    def go_back(self):
        if not self.stack.is_empty():
            page = self.stack.pop()
            print(f"Повернулися на попередню сторінку: {page}")
        else:
            print("Немає попередньої сторінки для повернення")


def main():
    history = WebHistory()

    history.visit_page("https://www.example.com/page1")
    history.visit_page("https://www.example.com/page2")
    history.visit_page("https://www.example.com/page3")

    history.go_back()

    history.visit_page("https://www.example.com/page4")

    history.go_back()

    history.go_back()

    history.go_back()


if __name__ == "__main__":
    main()




def infix_to_reverse_polish(text):
    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '(': -100}
    characters = text.replace('(', '( ').replace(')', ' )').split()
    stack = []
    result = ''

    for char in characters:
        if char.isdigit():
            result += ' ' + char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result += ' ' + stack.pop()
            stack.pop()
        else:
            while stack and priority.get(stack[-1], 0) >= priority.get(char, 0):
                result += ' ' + stack.pop()
            stack.append(char)

    while stack:
        result += ' ' + stack.pop()

    return result


def evaluate_reverse_polish(expression):
    stack = []

    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_operation(token, operand1, operand2)
            stack.append(result)

    return stack.pop()


def perform_operation(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2


def main():
    expression = '12 + 2 * ((3 * 4) + (10 / 5))'
    reverse_polish_expression = infix_to_reverse_polish(expression)
    print("Вираз у польському інверсному записі:", reverse_polish_expression)

    result = evaluate_reverse_polish(reverse_polish_expression)
    print("Результат обчислення виразу:", result)


if __name__ == "__main__":
    main()
