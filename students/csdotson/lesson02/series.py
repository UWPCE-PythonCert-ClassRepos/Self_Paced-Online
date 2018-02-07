# Lesson 2 - Computing Fibonacci and Lucas Series

def fibonacci(n):
    """Compute Fibonacci Series, return the nth value"""
    return sum_series(n)


def lucas(n):
    """Compute Lucas Series, return the nth value"""
    return sum_series(n, 2, 1)


def sum_series(n, first = 0, second = 1):
    """Compute generalized series, return nth value"""
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return ( sum_series(n-1, first, second) + sum_series(n-2, first, second) )


# Assertion testing - Fibonacci series (providing one argument)
assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(5) == 5

# Assertion testing - Lucas series
assert lucas(3) == 4
assert lucas(0) == 2

# Assertion testing - providing random inputs
assert sum_series(3, 4, 2) == 8
assert sum_series(1, 7, 8) == 8

print("All tests passed!")
