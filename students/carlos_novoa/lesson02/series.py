#!/usr/bin/env python

"""
Lesson2, Computing the Fibonacci and Lucas Series
"""


def fibonacci():
    """Return a list containing a fibonacci series (starting at 0, 1)"""
    return sum_series(False, 0, 1)


def lucas():
    """Return a list containing a lucas series (starting at 2, 1)"""
    return sum_series(False, 2, 1)


def sum_series(n, a=0, b=1):
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

    def series_int(n, a=0, b=1):
        for i in range(n):
            a, b = b, a + b
        return a

    series_range = 10  # limit 10 to avoid maximum recursion error
    for i in range(series_range):
        si = series_int(i, a, b)
        sequence.append(si)

    if n and n <= series_range and n >= 0:
        # print is possible
        print(sequence[n])
        return True

    return sequence


# fibonacci() returns list that matches correct
# sequence of Fibonacci numbers (starting at 0, 1)
assert fibonacci() == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# lucas() returns list that matches correct
# sequence of Lucas numbers (starting at 2, 1)
assert lucas() == [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]


# sum_series(index) returns explicit True if element prints
# (prints sequence num in console)
assert sum_series(3) is True


# sum_series(False, 0, 1) returns correct
# sequence of Fibonacci numbers (given 0, 1 args)
assert sum_series(False, 0, 1) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# sum_series(False, 2, 1) returns correct
# sequence of Lucas numbers (given 2, 1 args)
assert sum_series(False, 2, 1) == [2, 1, 3, 4, 7, 11, 18, 29, 47, 76]


# sum_series(False, 4, 8) returns a list of a different series
assert isinstance(sum_series(False, 4, 8), list)
