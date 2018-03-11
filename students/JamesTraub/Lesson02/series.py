# Create a new module series.py in the lesson02 folder in your student folder.
# In it, add a function called fibonacci.
# The function should have one parameter, n.
# The function should return the nth value in the fibonacci series (starting with zero index)
# Ensure that your function has a well-formed docstring
# Note that the fibonacci series is naturally recursive – the value is defined by previous values:

# fib(n) = fib(n-2) + fib(n-1)

# def fibonacci(n):
#     """
#     Return the nth value in the Fibonacci series. If parameter
#     is greater than 1 use recursion to find the nth value
#     shown in the else statement below.
#     """
#     if n == 1:
#         print(0)
#         return 0
#     elif n == 2:
#         print(1)
#         return 1
#     else:
#         return fibonacci(n-2) + fibonacci(n-1)
#
#
# fibonacci(4)
#
#
# def lucas(n):
#     """
#     Return the nth value in the Lucas series. If parameter
#     is greater than 1 use recursion to find the nth value
#     shown in the else statement below.
#     """
#     if n == 1:
#         print(2)
#         return 2
#     elif n == 2:
#         print(1)
#         return 1
#     else:
#         return lucas(n-2) + lucas(n-1)
#
#
# lucas(4)


def sum_series(n, param1=0, param2=1):
    """Return the nth value in the Fibonacci or Lucas series based on parameter input"""
    if n == 1:
        print(param1)
        return param1
    elif n == 2:
        print(param2)
        return param2
    else:
        return sum_series(n - 2, param1, param2) + sum_series(n - 1, param1, param2)


sum_series(6, 0, 1)
