"""
Instructions
Computing the Fibonacci and Lucas Series
Goal:
The Fibonacci Series is a numeric series starting with the integers 0 and 1.
In this series, the next integer is determined by summing the previous two.
This gives us:
0, 1, 1, 2, 3, 5, 8, 13, ...
We will write a function that computes this series – then generalize it.

"""

"""
Step 1
Create a new module series.py in the lesson02 folder in your student folder.
In it, add a function called fibonacci.
The function should have one parameter, n.
The function should return the nth value in the fibonacci series (starting with zero index)
Ensure that your function has a well-formed docstring
Note that the fibinacci series is naturally recursive – the value is defined by previous values:

fib(n) = fib(n-2) + fib(n-1)
"""


def fibonacci(n):
    """
   returns the nth value in the lucas fibonacci series
    """
    """if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)"""
    return sum_series(n)


def lucas(n):
    """returns the nth value in the lucas numbers series"""
    """if n == 0:
        return 2
    elif n == 1:
        return 1
    return lucas(n-2) + lucas(n-1)"""
    return sum_series(n, 2, 1)


def sum_series(n, optional_1=0, optional_2=1):
    """generalized function to return nth value of a series. Default is fibonacci. """
    if n < 0:
        return -1
    elif n == 0:
        return optional_1
    elif n == 1:
        return optional_2
    return sum_series(n-2, optional_1, optional_2) + sum_series(n-1, optional_1, optional_2)


if __name__ == '__main__':
    # testing fibonacci
    assert (fibonacci(2) == 1), "Fib Test One Failed"
    assert (fibonacci(4) == 3), "Fib Test Two Failed"
    assert (fibonacci(8) == 21), "Fib Test Three Failed"
    # testing lucas
    assert (lucas(2) == 3), "Lucas Test One Failed"
    assert (lucas(4) == 7), "Lucas Test Two Failed"
    assert (lucas(8) == 47), "Lucas Test Three Failed"

    # testing sum series
    assert (sum_series(10, 0, 1) == fibonacci(10)), "Series Test One Failed"
    assert (sum_series(21, 2, 1) == lucas(21)), "Series Test Two Failed"
    assert (sum_series(3) == fibonacci(3)), "Series Test Three Failed"
    assert (sum_series(8, 5, 4) == 149), "Series Test Four Failed"
