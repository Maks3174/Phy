#1
def bubble_sort(arr, reverse=False):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if reverse:
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                else:
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [8, 3, 5, 6, 2, 1]
bubble_sort(arr)
print(arr)

arr = [8, 3, 5, 6, 2, 1]
bubble_sort(arr, reverse=True)
print(arr)
print()
#2
def insertion_sort(arr):
    operations = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            operations += 1
        arr[j + 1] = key
    return arr, operations

arr = [12, 11, 13, 5, 6]
sorted_arr, insertion_count = insertion_sort(arr)
print("Відсортований список:", sorted_arr)
print("Кількість операцій вставки:", insertion_count)
print()
#3
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        if len(left_half) > 100:
            left_half = insertion_sort(left_half)
        else:
            left_half = merge_sort(left_half)

        if len(right_half) > 100:
            right_half = insertion_sort(right_half)
        else:
            right_half = merge_sort(right_half)

        arr = merge(left_half, right_half)

    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

arr = [12, 11, 13, 5, 6, 7, 9, 3, 2, 1, 8, 4, 10]
sorted_arr = merge_sort(arr)
print("Відсортований список:", sorted_arr)
