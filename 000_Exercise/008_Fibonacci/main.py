def fibonacci(arg):
    if arg <= 2:
        return 1
    return fibonacci(arg-1) + fibonacci(arg-2)


arg = 8
print(fibonacci(arg))
