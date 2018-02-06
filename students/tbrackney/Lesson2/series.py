"""
File Name: series.py
Author: Travis Brackney
Class: Python 201 - Self paced online
Date Created 2/3/2018
Python Version: 3.6.4
"""


def fibbonaci(n):
    """Prints the value in the fibbonaci sequence at position n"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibbonaci(n-2) + fibbonaci(n-1)


def lucas(n):
    """Prints the value in the lucas sequence at position n"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-2) + lucas(n-1)


def sum_series(n, first=0, second=1):
    """
    Returns the value of a position in a summation series with variable
    beginning values
    """
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n-2, first, second) + sum_series(n-1, first, second)


fib_series = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
lucas_series = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]

for i in range(10):
    # Compares output of fibbonaci(n) to known values of Fibbonaci series
    assert fibbonaci(i) == fib_series[i]
    # Compares output of lucas(n) to known values of lucas series
    assert lucas(i) == lucas_series[i]
    # sum_series should be able to duplicate lucas and fibbonaci series
    assert sum_series(i, 0, 1) == fibbonaci(i)
    assert sum_series(i, 2, 1) == lucas(i)
    # differeing starting values should change result
    assert sum_series(i, 3, 5) != lucas(i)
