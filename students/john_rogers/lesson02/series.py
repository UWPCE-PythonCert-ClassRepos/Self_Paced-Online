#!/usr/bin/env python3
"""
Create a new module series.py in the lesson02 folder in your student folder.
In it, add a function called fibonacci.
The function should have one parameter, n.
The function should return the nth value in the fibonacci series (starting
with zero index)
Ensure that your function has a well-formed docstring
Author: JohnR
"""


def main():
    """
    Main script logic
     1) test some assertions against each function to insure validity
     2) call and print results of each function at least once
    :return: Call each function and print the results to screen (or
                assertion error)
    """
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18
    assert lucas(7) == 29
    print('*' * 25)
    print('all assertion tests have passed')
    print('*' * 25)
    print('the 7th element in the fibonacci series is ' + str(fibonacci(7)))
    print('the 5th element in the lucas series is ' + str(lucas(5)))
    print(sum_series(7))


def fibonacci(n):
    """
    Take the input value and return that element in the Fibonacci series.
    :param n: Any non-zero positive integer
    :return: return nth value in fibonacci series
    """
    if n < 0:
        print('invalid input')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """
    Take input value and return that element in a lucas series
    :param n: Any non-zero positive integer
    :return: return nth value from the lucas series
    """
    if n < 0:
        print('invalid input')
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, n0=0, n1=1):
    """
    Let user decide which series to use based on input; default to fibonacci
    :param n: Only required parameter, which element to return from the series
    :param n0: Optional parameter, defaults to 0.
    :param n1: Optional parameter, defaults to 1.
    :return: Return the nth value from a given series (Fibonacci, Lucas, other)
    """
    if n < 0:
        print('invalid input')
    elif n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        return sum_series(n - 1, n0, n1) + sum_series(n - 2, n0, n1)


if __name__ == '__main__':
    main()
