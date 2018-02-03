#!/usr/bin/env python3
"""Slicing Module

This module contains various slicing functions.
"""


def first_and_last_swap(seq):
    """Swap first and last item of a sequence

    Args:
        seq (list): Sequence to be operated upon

    Returns:
        list: Copy of sequence with first and last items swapped
    """
    return seq[-1:] + seq[1:-1] + seq[:1]


if __name__ == '__main__':
    test_string = 'This is my test string'

    assert (first_and_last_swap(test_string) == 'ghis is my test strinT'), \
        "first_and_last_swap() failed"
