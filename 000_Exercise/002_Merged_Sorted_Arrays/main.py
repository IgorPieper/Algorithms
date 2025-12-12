def merge_sorted_arrays(a, b):
    c = []
    a_len = 0
    b_len = 0

    while True:
        if a_len < len(a) and b_len < len(b):
            if a[a_len] > b[b_len]:
                c.append(b[b_len])
                b_len += 1
            else:
                c.append(a[a_len])
                a_len += 1

        elif a_len < len(a):
            c.extend(a[a_len:])
            break

        elif b_len < len(b):
            c.extend(b[b_len:])
            break

    return c


a = [1, 2, 8, 16, 999, 1000]
b = [5, 7, 13, 75, 1021]
print(merge_sorted_arrays(a, b))
