# ------------------------------------------------- #
# Title: Lesson 2, pt 3/3, Fibonacci Series Exercise
# Dev:   Craig Morton
# Date:  8/14/2018
# Change Log: CraigM, 8/14/2018, Fibonacci Series Exercise
#  ------------------------------------------------ #


def fibonacci(n):
    """Return the nth value of the Fibonacci sequence"""
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


def lucas(n):
    """Return the nth value in the Lucas series"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 2) + lucas(n - 1)


def sum_series(n, x=0, y=0):
    """Process the nth number of the Fibonacci sequence or Lucas series"""
    if x == 0 or y == 0:
        return fibonacci(n)
    else:
        return lucas(n)


# Assertion testing for Fibonacci sequence
assert fibonacci(5) == 5
assert fibonacci(10) == 55

# Assertion testing for Lucas series
assert lucas(0) == 2
assert lucas(6) == 18

# Assertion testing for sum_series with Fibonacci sequence
assert sum_series(2, 0, 0) == 1
assert sum_series(6, 0, 0) == 8

# Assertion testing for sum_series with Lucas series
assert sum_series(2, 2, 5) == 3
assert sum_series(5, 2, 5) == 11
