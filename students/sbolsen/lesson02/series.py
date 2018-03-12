def fib(n):
    """Returns a value from the Fibonacci Series."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
#print(fib(3))

def lucas(n):
    """Returns a value from the Lucas Series."""
    if n == 1:
        return 1
    elif n == 0:
        return 2
    else:
        return lucas(n - 1) + lucas(n - 2)
#print(lucas(5))

def sum_series(n, a = 0, b = 1):
    """Produces numbers from the Fibonacci and Lucas Series depending upon arguments."""
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        return sum_series(n - 1, a, b) + sum_series(n - 2, a, b)

assert sum_series(5) == sum_series(4) + sum_series(3)
assert sum_series(9, 2, 1) == sum_series(8, 2, 1) + sum_series(7, 2, 1)
