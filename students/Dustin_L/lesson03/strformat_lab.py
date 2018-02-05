#!/usr/bin/env python3
"""String Format Lab

This module contains all of the functions for the String Format Lab.
"""


def task_one(quad):
    """Return formatted string.

    Args:
        quad (tuple): Tuple of 4 elements.

    Returns:
        str: Formatted string.
    """
    fmt_str = 'file_{:0>3d}: {:.2f}, {:.2e}, {:.3e}'
    return fmt_str.format(*quad)


def task_two(quad):
    """Return formatted string.

    Args:
        quad (tuple): Tuple of 4 elements.

    Returns:
        str: Formatted string.
    """
    return f'file_{quad[0]:0>3d}: {quad[1]:.2f}, {quad[2]:.2e}, {quad[3]:.3e}'


def task_three(input_tup):
    """Return formatted string containing all values from the passed tuple.

    The string format is: 'the x numbers are: a, b, c...'

    Args:
        input_tup (tuple): Tuple containing values to be entered in string.

    Returns:
        str: Formatted string.
    """
    l = len(input_tup)
    num_fmt = ('{:d}, ' * (l - 1)) + '{:d}'
    num_str = num_fmt.format(*input_tup)

    return f'the {l} numbers are: {num_str}'


def task_four(input_tuple):
    """Return formatted string containing values from a tuple of size 5.

    Args:
        input_tuple (tuple): Tuple of size of digits.

    Returns:
        str: Formatted string if corrrect tuple size, empty string if not.
    """
    if len(input_tuple) != 5:
        return ''

    return '{3:02d} {4:02d} {2:04d} {0:02d} {1:02d}'.format(*input_tuple)


def task_five():
    """Return a formatted f-string."""
    data = ['oranges', 1.3, 'lemons', 1.1]
    return f'The weight of an {data[0][:-1]} is {data[1]} and the weight of '\
           f'a {data[2][:-1]} is {data[3]}'


def task_five_alt():
    """Return a formatted f-string."""
    data = ['oranges', 1.3, 'lemons', 1.1]
    return f'The weight of an {data[0][:-1].upper()} is {data[1] * 1.2} '\
           f'and the weight of a {data[2][:-1].upper()} is {data[3] * 1.2}'


def task_six():
    """Print a formatted table of local data.

    Data will be printed with 4 rows and 3 columns all evenly aligned.
    """
    data = [['Bert',     33, '-$150,000'],\
            ['Angelina', 37, '-$1,500,000.42'],\
            ['Batman',   1,  '$10,000'],\
            ['Lucy',     5,  '$35,500.99']]

    max_name = len(max([name[0] for name in data], key=len))
    max_cost = len(max([cost[2] for cost in data], key=len))
    max_age  = 3

    str_fmt = '{:<' + f'{max_name + 5}' + '}{:<' + f'{max_age + 5}' +\
              '}{:<' + f'{max_cost + 5}' + '}'

    for row in data:
        print(str_fmt.format(row[0], row[1], row[2]))


def task_six_extra(input_tuple):
    """Return a string with each tuple element evenly spaced by 5."""
    return ('{:5}' * len(input_tuple)).format(*input_tuple)


if __name__ == '__main__':
    print(task_one((2, 123.4567, 10000, 12345.67)))
    print(task_two((2, 123.4567, 10000, 12345.67)))
    print(task_three((1, 2, 3, 4, 5, 6, 7, 3, 1, 0, 100)))
    print(task_four((4, 30, 2017, 2, 27)))
    print(task_five())
    print(task_five_alt())
    task_six()
    print(task_six_extra((3, 2, 5, 4, 7, 1, 8, 9, 2, 10)))
