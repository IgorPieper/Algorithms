# O(n log n) Version where pivot is always the last number
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    right = []

    for i in range(len(arr) - 1):
        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(quick_sort(numbers))
