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


if __name__ == '__main__':
    print(task_one((2, 123.4567, 10000, 12345.67)))
