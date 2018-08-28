def fibonacci(n):
    """return the nth value of the Fibonacci series"""
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


def 