"""
Victor Medina
Assignment 2: Series.py
Three functions:
The fibonacci function is a function determining the nth value of the fibonacci series.

The lucas function is a function determining the nth value of the lucas series.

The sum series function is a function that if takes two optional arguments. If left at default, it will calculate the
nth value of the fibonacci series. If changed to a=2 and b=1 it'll find the nth value of the Lucas series.
Anything else will determine the nth value of its own series.
"""


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


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

assert fibonacci(0) == 0
assert fibonacci(2) == 1
assert fibonacci(4) == 3
assert fibonacci(6) == 8
assert fibonacci(7) == 13

# Assertion test to validate lucas function
assert lucas(0) == 2
assert lucas(2) == 3
assert lucas(4) == 7
assert lucas(6) == 18
assert lucas(7) == 29

# Assertion test to validate sum_series function
assert sum_series(0) == fibonacci(0)
assert sum_series(2) == fibonacci(2)
assert sum_series(4) == fibonacci(4)
assert sum_series(6) == fibonacci(6)
assert sum_series(7) == fibonacci(7)
assert sum_series(0, 2, 1) == lucas(0)
assert sum_series(2, 2, 1) == lucas(2)
assert sum_series(4, 2, 1) == lucas(4)
assert sum_series(6, 2, 1) == lucas(6)
assert sum_series(7, 2, 1) == lucas(7)
