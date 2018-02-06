# Lesson 2 - Computing Fibonacci and Lucas Series

def fibonacci(n):
    """Compute Fibonacci Series, return the nth value"""
    return sum_series(n)


def lucas(n):
    """Compute Lucas Series, return the nth value"""
    return sum_series(n, 2, 1)


def sum_series(n, first = 0, second = 1):
    """Compute generalized series, return nth value"""
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return ( sum_series(n-1, first, second) + sum_series(n-2, first, second) )


# Add block of code to test your functions - write a series of 'assert' statements to accomplish this
