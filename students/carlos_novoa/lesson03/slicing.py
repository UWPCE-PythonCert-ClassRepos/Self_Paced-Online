#!/usr/bin/env python

"""
Lesson3, Slicing Lab Exercise
"""


def exchange_first_last(seq):
    """first and last items exchanged"""
    return seq[-1:] + seq[1:-1] + seq[:1]


def remove_every_other(seq):
    """every other item removed"""
    return seq[::2]


def remove_ends4_every_other(seq):
    """first 4 and last 4 items removed, and every other in between"""
    return seq[4:-4:2]


def reversed(seq):
    """elements reversed (just with slicing)"""
    return seq[::-1]


def thirds(seq):
    """order: middle third, last third, first third """
    return seq[int(len(seq) / 3):int((len(seq) / 3) * 2)] +\
        seq[-int(len(seq) / 3):] +\
        seq[:int(len(seq) / 3)]


"""
Assertions
"""
a_string = "abcdefghijkl"
a_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

assert exchange_first_last(a_string) == "lbcdefghijka"
assert exchange_first_last(a_tuple) == (12, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1)
assert exchange_first_last(a_list) == [12, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1]

assert remove_every_other(a_string) == "acegik"
assert remove_every_other(a_tuple) == (1, 3, 5, 7, 9, 11)
assert remove_every_other(a_list) == [1, 3, 5, 7, 9, 11]

assert remove_ends4_every_other(a_string) == "eg"
assert remove_ends4_every_other(a_tuple) == (5, 7)
assert remove_ends4_every_other(a_list) == [5, 7]

assert reversed(a_string) == "lkjihgfedcba"
assert reversed(a_tuple) == (12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
assert reversed(a_list) == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

assert thirds(a_string) == "efghijklabcd"
assert thirds(a_tuple) == (5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4)
assert thirds(a_list) == [5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4]
