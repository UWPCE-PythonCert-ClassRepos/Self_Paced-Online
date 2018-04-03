'''
    File Name: series.py
    Author: Matt Hudgins
    Date created: 4/2/2018
    Date last modified: 4/2/2018
    Python Version 3.6.4
'''


def fibonacci(n):
    """This function calculates the nth number of the Fibonacci
    Series"""
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n < 0:
        print("Invalid Input")
        return 0
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


def lucas(n):
    """This function calculates the nth number of the Lucas Numbers"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n < 0:
        print("Invalid Input")
        return 0
    else:
        return lucas(n - 2) + lucas(n - 1)

def sum_series(n, x = 0, y = 0):
    """Depending on the input parameters this function will either
    calculate the nth number of the Fibonacci Series or the Lucas
    numbers"""
    if x == 0 or y == 0:
        return fibonacci(n)
    else:
        return lucas(n)

# The following series of assertions test the above functions

# Fibonacci function test


assert fibonacci(2) == 1
assert fibonacci(5) == 5
assert fibonacci(8) == 21

# Lucas function test


assert lucas(2) == 3
assert lucas(5) == 11
assert lucas(8) == 47

# Sum_Series function test for Fibonacci parameters


assert sum_series(2, 0, 0) == 1
assert sum_series(5, 0, 0) == 5
assert sum_series(8, 0, 0) == 21

# Sum_Series function test for Fibonacci parameters


assert sum_series(2, 2, 5) == 3
assert sum_series(5, 2, 5) == 11
assert sum_series(8, 2, 5) == 47
