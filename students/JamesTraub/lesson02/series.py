# Create a function called fibonacci.
# The function should have one parameter, n.
# The function should return the nth value in the fibonacci series (starting with zero index)
# Ensure that your function has a well-formed docstring
# Note that the fibonacci series is naturally recursive – the value is defined by previous values:

# fib(n) = fib(n-2) + fib(n-1)


def fibonacci(n):
    """
    Return the nth value in the Fibonacci series. If parameter
    is greater than 1 use recursion to find the nth value
    shown in the else statement below.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)


# print(fibonacci(4))


def lucas(n):
    """
    Return the nth value in the Lucas series. If parameter
    is greater than 1 use recursion to find the nth value
    shown in the else statement below.
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-2) + lucas(n-1)


# print(lucas(4))


def sum_series(n, param1=0, param2=1):
    """
    Return the nth value in the Fibonacci or Lucas series based on parameter input.
    Default values are defined in parameters 2 and 3 and can be overwritten by
    adding them to the function call. They are optional parameters but will be used
    if none are entered in the function call.
    """
    if n == 0:
        return param1
    elif n == 1:
        return param2
    else:
        return sum_series(n-2, param1, param2) + sum_series(n-1, param1, param2)


# print(sum_series(3, 2, 1))


"""
assert statements to test the functions
"""
assert fibonacci(6) == 8  # test the fibonacci function for correct return value
assert fibonacci(1) == 1  # test the fibonacci function for correct return value
assert lucas(6) == 18  # test the lucas function for correct return value
assert lucas(1) == 1  # test the lucas function for correct return value
assert sum_series(6) == 8  # test the sum_series function for correct return value when optional parameters not given
assert sum_series(7, 2, 1) == 29  # test the sum_series function for correct return value based on parameters
