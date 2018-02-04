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


if __name__ == '__main__':
    print(task_one((2, 123.4567, 10000, 12345.67)))
    print(task_two((2, 123.4567, 10000, 12345.67)))
    print(task_three((1, 2, 3, 4, 5, 6, 7, 3, 1, 0, 100)))
