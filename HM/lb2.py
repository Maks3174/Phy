#1
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

arr = [12, 34, 54, 2, 3]
shell_sort(arr)
print("Відсортований список:", arr)
print()
#2
def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Відсортований список:", arr)
print()
#3
import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return quick_sort(less) + equal + quick_sort(greater)

arr = [12, 4, 5, 6, 7, 3, 1, 15]
print("Вхідний список:", arr)
sorted_arr = quick_sort(arr)
print("Відсортований список:", sorted_arr)
print()
#4
def flip(stack, k):
    return stack[:k+1][::-1] + stack[k+1:]

def pancake_sort(stack):
    n = len(stack)
    for size in range(n, 1, -1):
        k = random.randint(0, size - 1)
        stack = flip(stack, k)
        print(f"Крок {n - size + 1}: {stack}")
    return stack

stack = [3, 2, 4, 1, 5]
print("Вхідний стос:", stack)
sorted_stack = pancake_sort(stack)
print("Відсортований стос:", sorted_stack)