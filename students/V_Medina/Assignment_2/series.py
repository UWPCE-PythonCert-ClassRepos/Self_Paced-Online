def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, a=0, b=1):
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return sum_series(n - 1, a, b) + sum_series(n - 2, a, b)


# Assertion test to validate fibonacci function

assert fib(0) == 0
assert fib(2) == 1
assert fib(4) == 3
assert fib(6) == 8
assert fib(7) == 13

# Assertion test to validate lucas function
assert lucas(0) == 2
assert lucas(2) == 3
assert lucas(4) == 7
assert lucas(6) == 18
assert lucas(7) == 29

# Assertion test to validate sum_series function 
assert sum_series(0) == fib(0)
assert sum_series(2) == fib(2)
assert sum_series(4) == fib(4)
assert sum_series(6) == fib(6)
assert sum_series(7) == fib(7)
assert sum_series(0, 2, 1) == lucas(0)
assert sum_series(2, 2, 1) == lucas(2)
assert sum_series(4, 2, 1) == lucas(4)
assert sum_series(6, 2, 1) == lucas(6)
assert sum_series(7, 2, 1) == lucas(7)
