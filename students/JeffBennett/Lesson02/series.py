"""
Write various functions to return the nth term of the Fibonacci
and Lucas series.
"""


def fibonacci(n):
    """return the nth term of the Fibonacci series for integer n >= 0."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """return the nth term of the Lucas series for integer n >= 0."""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n0, n1=0, n2=1):
    """
    compute the nth value of a summation series for n >=0.

    :param n0=0: value of zeroth element in the series
    :param n1=1: value of first element in the series

    if n0 == 0 and n1 == 1, the result is the Fibbonacci series

    if n0 == 2 and n1 == 1, the result is the Lucas series
    """
    if n0 == 0:
        return n1
    elif n0 == 1:
        return n2
    else:
        return sum_series(n0-1, n1, n2) + sum_series(n0-2, n1, n2)


if __name__ == "__main__":
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(4) == 7

    assert sum_series(5) == fibonacci(5)
    assert sum_series(5, 2, 1) == lucas(5)

    print("tests passed")
