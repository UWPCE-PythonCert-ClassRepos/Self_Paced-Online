#!/usr/bin/env python

"""
Lesson2, Computing the Fibonacci and Lucas Series
"""


def fibonacci():
    """Return a list containing a fibonacci series (starting at 0, 1)"""
    return sum_series(a=0, b=1)


def lucas():
    """Return a list containing a lucas series (starting at 2, 1)"""
    return sum_series(a=2, b=1)


def sum_series(n=None, a=0, b=1):
    """
    Print or return numbers in a fibonacci/lucas series

    :param n: Print option or index of element in series list
    :param a: First number in series
    :param b: Second number in series
    :type n: bool or int
    :type a: int
    :type b: int
    :returns: fibonacci/lucas number(s)
    :rtype: list
    """

    if a == 0 and b == 0:
        return False

    sequence = []

    def fib_series(r, a=0, b=1):
        for i in range(r):
            a, b = b, a + b
        return a

    def fib(n):
        a, b = 1, 1
        for i in range(n - 1):
            a, b = b, a + b
        return a

    #  Single Fibonnacci number
    if n:
        fb = fib(n)
        print(fb)
        return fb

    #  Fibonnacci sequence
    series_range = 10  # limit 10 to avoid maximum recursion error
    for i in range(series_range):
        si = fib_series(i, a, b)
        sequence.append(si)

    return sequence


# fibonacci() returns list of Fibonacci numbers (starting at 0, 1)
assert fibonacci() == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# lucas() returns list of Lucas numbers (starting at 2, 1)
assert lucas() == [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]


# sum_series(index) returns and prints corresponding fibonacci number
assert sum_series(9) == 34


# sum_series(a=0, b=1) returns correct sequence of Fibonacci numbers
assert sum_series(a=0, b=1) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# sum_series(2, 1) returns correct sequence of Lucas numbers
assert sum_series(a=2, b=1) == [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]


# sum_series(a=4, b=8) returns a list of a different series
assert isinstance(sum_series(a=4, b=8), list)
