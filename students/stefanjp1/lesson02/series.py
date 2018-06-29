
def fibonacci(n):
    """Return the nth value of the fibonacci series starting with 0 index."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """Return the nth value of the lucas series starting with 0 index."""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, n_0 = 0, n_1 = 1):
    """
    Return the nth value of the series specified in n_0 and n_1.
    :param n_0=0: An optional parameter. The value to return when the recursion reaches 0
    :param n_1=1: An optional parameter. The value to return when the recursion reaches 1
    """
    if n == 0:
        return n_0
    elif n == 1:
        return n_1
    else:
        return sum_series(n-1, n_0, n_1) + sum_series(n-2, n_0, n_1)


def fibonacci(n):
    """Return the nth value of the fibonacci series starting with 0 index."""
    return sum_series(n)
    
def lucas(n):
    """Return the nth value of the lucas series starting with 0 index."""
    return sum_series(n, n_0 = 2, n_1 = 1)


# Using default optional parameters, 
# sum_series should return 13 for the 8th fibonacci number (7 using 0 indexing)
assert sum_series(7) == 13

# Changing the optional parameters to match lucas numbering, 
# sum_series should return 18 for the 7th lucas number (6 using 0 indexing)
assert sum_series(6, n_0 = 2, n_1 = 1)

# The 8th fibonacci number (7 using 0 indexing) is 13
assert fibonacci(7) == 13

# The 7th lucas number (6 using 0 indexing) is 18
assert lucas(6) == 18

