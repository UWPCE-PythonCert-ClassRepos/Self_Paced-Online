#!/usr/bin/env python3
"""Slicing Module

This module contains various slicing functions.
"""


def first_and_last_swap(seq):
    """Swap first and last item of a sequence

    Args:
        seq (sequence): Sequence to be operated upon

    Returns:
        sequence: Copy of sequence with first and last items swapped
    """
    return seq[-1:] + seq[1:-1] + seq[:1]


def remove_every_other(seq):
    """Remove every other item from sequence

    Args:
        seq (sequence): Sequence to be operated upon

    Returns:
        sequence: Copy of sequence with every other item removed
    """
    return seq[::2]


def first_last_four_every_other(seq):
    """Remove first and last four items and return every other item from the remaining items.

    Args:
        seq (sequence): Sequence to be operated upon.

    Returns:
        sequence: Copy of sequence with first and last four items removed and every
        other remaining item selected.
    """
    return seq[4:-4:2]


def reverse(seq):
    """Reverse the sequence.

    Args:
        seq (sequence): Sequence to be operated upon.

    Returns:
        sequence: Copy of reversed sequence.
    """
    return seq[::-1]


def arrange_thirds(seq):
    """Arrange sequence by middle third, last third and first third.

    Args:
        seq (sequence): Sequence to be operated upon.

    Returns:
        sequence: Copy of arranged sequence
    """
    third = int(len(seq) / 3)
    return seq[third:third * 2] + seq[third * 2:] + seq[:third]


if __name__ == '__main__':
    test_string = 'This is my test string'
    test_tuple  = (4, 3, 9, 10, 23)

    assert(first_and_last_swap(test_string) == 'ghis is my test strinT'), \
        'first_and_last_swap() failed'
    assert(first_and_last_swap(test_tuple) == (23, 3, 9, 10, 4)), \
        'first_and_last_swap() failed'

    assert(remove_every_other(test_string) == 'Ti sm etsrn'), \
        'remove_every_other() failed'
    assert(remove_every_other(test_tuple) == (4, 9, 23)), \
        'remove_every_other() failed'

    assert(first_last_four_every_other(test_string) == ' sm ets'), \
        'first_last_four_every_other() failed'
    assert(first_last_four_every_other(test_tuple) == ()), \
        'first_last_four_every_other() failed'

    assert(reverse(test_string) == 'gnirts tset ym si sihT'), \
        'reverse() failed'
    assert(reverse(test_tuple) == (23, 10, 9, 3, 4)), \
        'reverse() failed'

    assert(arrange_thirds(test_string) == ' my test stringThis is'), \
        'arrange_thirds() failed'
    assert(arrange_thirds(test_tuple) == (3, 9, 10, 23, 4)), \
        'arrange_thirds() failed'
