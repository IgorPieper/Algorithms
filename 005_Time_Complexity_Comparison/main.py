a = ["a", "b", "c", "x"]
b = ["z", "y", "x"]


def first_try(a, b):
    for x in a:
        for y in b:
            if x == y:
                return True
    return False
# O(n^2)


def second_try(a, b):
    for x in a:
        if x in b:
            return True
    return False
# O(n^2) looking like O(n)


def third_try(a, b):
    return bool(set(a) & set(b))
# O(n + m)
