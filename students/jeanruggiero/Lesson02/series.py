#!/usr/bin/env python3

# This script contains functions that compute sequences.

def fibonacci(n):
    """This function returns the nth value in the fibonacci series (starting with zero index)."""

    if n <= 1:
        return n
    else:
        # Call fibonacci function recursively to determine nth value
        return fibonacci(n-2) + fibonacci(n-1)


def lucas(n):
    """This function returns the nth value in the lucas series (starting with zero index)."""

    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        # Call lucas function recursively to determine nth value
        return lucas(n-2) + lucas(n-1)


def sum_series(n,x=0,y=1):
    """This function returns the nth value (starting with index zero) in of an
    additive series with first two numbers x and y."""

    if n == 0:
        return x
    elif n == 1:
        return y
    else:
        # Call sum_series function recursively to determine nth value
        return sum_series(n-2,x,y) + sum_series(n-1,x,y)

# Assert statements to test functions
assert fibonacci(10) == 55              # Tests fibonacci function against known value
assert lucas(7) == 29                   # Tests lucas function against known value
assert sum_series(20) == fibonacci(20)  # Tests sum_series against fibonacci
assert sum_series(13,2,1) == lucas(13)  # Tests sum_series against lucas
