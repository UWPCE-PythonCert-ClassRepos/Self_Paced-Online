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


# print(fibonacci(0))


def lucas(n):
    """Return the nth term of the Lucas series for integer n >= 0."""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


print(lucas(7))
