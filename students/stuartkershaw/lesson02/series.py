def fibonacci(n):
    """Take integer input and return corresponding fibonacci value"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))


def lucas(n):
    """Take integer input and return corresponding lucas value"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


print(lucas(6))


def sum_series(n, x=0, y=1):
    """Take integer value and sequencing inputs and return value"""
    if n == 0:
        return x
    elif n == 1:
        return y
    else:
        return sum_series(n - 1, x, y) + sum_series(n - 2, x, y)


print(sum_series(6, 2))
