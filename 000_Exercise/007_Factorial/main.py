def factorial1(number, times, arg):
    if times < arg:
        times += 1
        number *= times
        print(number)
        factorial(number, times, arg)
    return number


def factorial2(arg):
    if arg == 2:
        return 2
    return arg * factorial2(arg - 1)


number = 1
times = 0
arg = 5

factorial1(number, times, arg)
print(factorial2(arg))
