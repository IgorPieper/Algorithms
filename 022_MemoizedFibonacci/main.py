def fibonacci():
    cache = {}

    def inner(n):
        if n in cache:
            return cache[n]

        if n <= 2:
            return 1

        cache[n] = inner(n - 1) + inner(n - 2)
        return cache[n]

    return inner


fibonacci = fibonacci()

arg = 995
print(fibonacci(arg))
