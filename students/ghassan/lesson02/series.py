#!/usr/bin/env python3


def fib(n):
    """ returns fibonacci series """
    return sum_series(n)


def luc(n):
    """ Returns Lucas series """
    return sum_series(n, 2, 1)


def sum_series(n, i=0, j=1):
    if n == 1:
        return i
    elif n == 2:
        return j
    else:
        return sum_series(n - 1, i, j) + sum_series(n - 2, i, j)


assert sum_series(7) == sum_series(6)+sum_series(5)
assert sum_series(7, 2, 1) == sum_series(6, 2, 1)+sum_series(5, 2, 1)
