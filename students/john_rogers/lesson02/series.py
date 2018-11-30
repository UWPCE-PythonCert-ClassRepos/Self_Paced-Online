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
    :return: Call each function and print the results to screen
    """
    print(fibonacci(9))
    print(lucas(9))


def fibonacci(n):
    """
    Create a fibonacci series starting at 0 and 1
    :param n: any positive integer
    :return: return fibonacci value for input n
    """
    if n < 0:
        print('invalid input')
    elif n == 0 or n == 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """
    Create a Lucas series that start at 2 and 1
    :param n: any positive integer
    :return: return Lucas value for input n
    """
    if n < 0:
        print('invalid input')
    elif n == 0:
        return 2
    elif n == 1:
        return 1

    return lucas(n - 1) + lucas(n - 2)


if __name__ == '__main__':
    main()
