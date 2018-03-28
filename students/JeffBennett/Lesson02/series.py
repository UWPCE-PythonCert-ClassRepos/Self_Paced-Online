"""
Write various functions to return the nth term of the Fibonacci
and Lucas series.
"""


def fibonacci(n):
    """Return the nth term of the Fibonacci series for integer n >= 0."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """Return the nth term of the Lucas series for integer n >= 0."""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n0, n1=0, n2=1):
    """Return the n0-th term of the Fibonacci or Lucas series for integer n >= 0.
    Default values return Fibonacci while n1=2 and n2=1 return Lucas. """
    if n0 == 0:
        return n1
    elif n0 == 1:
        return n2
    else:
        return sum_series(n0-1, n1, n2) + sum_series(n0-2, n1, n2)


print(sum_series(10))
