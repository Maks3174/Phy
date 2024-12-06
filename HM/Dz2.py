#1
def custom_sort(lst):
    avg = sum(lst) / len(lst)
    first_part = sorted(lst[:len(lst)//3*2] if avg > 0 else lst[:len(lst)//3])
    second_part = lst[len(first_part):][::-1]
    return first_part + second_part

my_list = [3, -2, 5, 1, -4, 8, -6, 7]
result = custom_sort(my_list)
print("Відсортований список:", result)
print()
#2
def display_grades(grades):
    print("Оцінки студента:", grades)

def rearrange_grade(grades):
    index = int(input("Введіть номер оцінки, яку потрібно перескласти: "))
    new_grade = int(input("Введіть нову оцінку: "))
    grades[index - 1] = new_grade
    print("Оцінка перескладена.")

def get_scholarship(grades):
    average_grade = sum(grades) / len(grades)
    if average_grade >= 10.7:
        print("Студент отримує стипендію.")
    else:
        print("Студент не отримує стипендію.")

def sort_grades(grades, order):
    sorted_grades = sorted(grades, reverse=(order == 'за спаданням'))
    print("Відсортований список оцінок:", sorted_grades)

def main():
    grades = []
    for i in range(10):
        grade = int(input(f"Введіть оцінку {i + 1}: "))
        grades.append(grade)

    while True:
        print("\nМеню:")
        print("1. Виведення оцінок")
        print("2. Перескладання іспиту")
        print("3. Отримання стипендії")
        print("4. Виведення відсортованого списку оцінок за зростанням")
        print("5. Виведення відсортованого списку оцінок за спаданням")
        print("6. Вихід")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            display_grades(grades)
        elif choice == '2':
            rearrange_grade(grades)
        elif choice == '3':
            get_scholarship(grades)
        elif choice == '4':
            sort_grades(grades, 'за зростанням')
        elif choice == '5':
            sort_grades(grades, 'за спаданням')
        elif choice == '6':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()

print()
#3
def bubble_sort(arr):
    n = len(arr)
    swaps = 0

    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        if not swapped:
            break

    return swaps

my_list = [64, 34, 25, 12, 22, 11, 90]
swaps = bubble_sort(my_list)
print("Відсортований масив:", my_list)
print("Кількість перестановок:", swaps)
