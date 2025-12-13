def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(bubble_sort(numbers))
