def fibonacci(n):
    """Return the nth value of the Fibonacci series."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib1 = 0
        fib2 = 1
        for it in range(1, n):
            fib = fib1 + fib2
            fib1 = fib2
            fib2 = fib
        return fib


def lucas(n):
    """Return the nth value of the Lucas series."""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        luc1 = 2
        luc2 = 1
        for it in range(1, n):
            luc = luc1 + luc2
            luc1 = luc2
            luc2 = luc
        return luc


def sum_series(n, val1=0, val2=1):
    """
    Return the nth value of a series f, such that f(n)=f(n-2)+f(n-1).
    :param n: The value of the series requested
    :param val1: First optional parameter.
                 The first value of the series (Default 0)
    :param val2: Second optional parameter.
                 The second value of the series (Default is 1)
    """
    if n == 0:
        return val1
    elif n == 1:
        return val2
    else:
        for it in range(1, n):
            valn = val1 + val2
            val1 = val2
            val2 = valn
        return valn


assert fibonacci(10) == 55
assert fibonacci(5) == 5
assert lucas(10) == 123
assert lucas(5) == 11
assert sum_series(10) == 55
assert sum_series(10, 2, 1) == 123
