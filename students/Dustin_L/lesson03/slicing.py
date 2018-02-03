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


def remove_every_other(seq):
    """Remove every other item from sequence

    Args:
        seq (list): Sequence to be operated upon

    Returns:
        list: Copy of sequence with every other item removed
    """
    return seq[::2]


def first_last_four_every_other(seq):
    """Remove first and last four items and return every other item from the remaining items.

    Args:
        seq (list): Sequence to be operated upon.

    Returns:
        list: Copy of sequence with first and last four items removed and every
        other remaining item selected.
    """
    return seq[4:-4:2]


def reverse(seq):
    """Reverse the sequence.

    Args:
        seq (list): Sequence to be operated upon.

    Returns:
        list: Copy of reversed sequence.
    """
    return seq[::-1]



if __name__ == '__main__':
    test_string = 'This is my test string'

    assert(first_and_last_swap(test_string) == 'ghis is my test strinT'), \
        'first_and_last_swap() failed'
    assert(remove_every_other(test_string) == 'Ti sm etsrn'), \
        'remove_every_other() failed'
    assert(first_last_four_every_other(test_string) == ' sm ets'), \
        'first_last_four_every_other() failed'
    assert(reverse(test_string) == 'gnirts tset ym si sihT'), \
        'reverse() failed'
