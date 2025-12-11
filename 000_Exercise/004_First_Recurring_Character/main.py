# O(n²)
def first_recurring_character(arr):
    b = []

    for aa in arr:
        if aa not in b:
            b.append(aa)
        else:
            return aa


# O(n)
def better_first_recurring_character(arr):
    b = {}

    for i in range(len(arr)):
        if arr[i] in b:
            return arr[i]
        else:
            b[arr[i]] = i

        print(b)

    return None


arr = [2, 5, 1, 2, 3, 5, 1, 2, 4]

print("First Recurring Character: ", first_recurring_character(arr))
