def memoized_add_to_80():
    cache = {}

    def inner(n):
        if n in cache:
            return cache[n]
        else:
            print("long time")
            cache[n] = n + 80
            return cache[n]

    return inner


memoized = memoized_add_to_80()

print("1", memoized(5))
print("2", memoized(5))
