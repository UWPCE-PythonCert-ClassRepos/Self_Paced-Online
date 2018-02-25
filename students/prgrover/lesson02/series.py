def fibonacci(n):
    """
    This function uses recursion to calculate a Fibonacci Series.

    Args: 
    n:  Calculate up to the nth value of the Fibonacci Series.

    Returns:
    The nth value in the Fibonacci Series.
    """

    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
    


def lucas(n):
    """
    This function uses recursion to calculate a Lucas Number series.

    Args:
    n: Calculate up to the nth value of the Lucas Number series.

    Returns:
    The nth value in the Lucas Number series.
    """

    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return (lucas(n-1) + lucas(n-2))



def sum_series(n, y=0, z=1):
    """
    Generalized function that calculates a number series based on the provided parameters.

    Calling this function with no optional parameters will produce numbers from the fibonacci series. Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers. Other values for the optional parameters will produce other series.

    Args:
    n:  Required. Calculate up the nth value of numeric series.
    y:  Optional. The first value of the series to be produced. Default value is 0.
    z:  Optional. The second value of the series to be produced. Default valie is 1.

    Returns:
    The nth value of the Lucas Number series.
    """

    if n == 0:
        return y
    elif n == 1:
        return z
    else:
        return (sum_series(n-1, y, z) + sum_series(n-2, y, z))


"""
fibonacci(n) tests

Known values of the Fibonacci Numbers series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
"""
assert fibonacci(0) == 0
assert fibonacci(8) == 21


"""
lucas(n) tests

Known values of the Lucas Numbers series: 2, 1, 3, 4, 7, 11, 18, 29, 47, 76
"""
assert lucas(2) == 3
assert lucas(9) == 76

"""
sum_series(n,,z) tests

The provided paramters should correctly match either the fibonacci or lucas series calculated values
"""

assert sum_series(0) == fibonacci(0)
assert sum_series(8) == fibonacci(8)
assert sum_series(9, 0, 1) == fibonacci(9)
assert sum_series(6, 2, 1) == lucas(6)
