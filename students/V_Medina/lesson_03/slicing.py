#!/usr/bin/env python3
"""
Victor Medina
1/12/2019
Lesson 3: Slicing Lab
"""


def exchange_first_last(seq):
    # Need to check what type of sequence is being inputted. Depending on the sequence different approaches are used to
    # switch the first and last element
    if type(seq) == str:
        return seq[-1] + seq[1:-1] + seq[0]
    elif type(seq) == tuple:
        seq = list(seq)
        seq[0], seq[-1] = seq[-1], seq[0]
        seq = tuple(seq)
        return seq
    else:
        seq[0], seq[-1] = seq[-1], seq[0]
        return seq


def every_other_item_removed(seq):
    return seq[::2]


def first_last_4_removed_every_other_item_removed(seq):
    new_seq = seq[4:-4]
    return new_seq[::2]


def reversed_seq(seq):
    return seq[::-1]


def mid_last_first(seq):
    seq_length = len(seq)
    mid = seq[int(seq_length / 3):int(2 * seq_length / 3)]
    first = seq[:int(seq_length / 3)]
    last = seq[int(2 * seq_length / 3):]
    return mid + last + first


"""Assertion Tests """
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

assert every_other_item_removed(a_string) == 'ti sasrn'
assert every_other_item_removed(a_tuple) == (2, 13, 5)

assert first_last_4_removed_every_other_item_removed(a_string) == ' sas'
assert first_last_4_removed_every_other_item_removed([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == [5, 7, 9]

assert reversed_seq(a_string) == 'gnirts a si siht'
assert reversed_seq(a_tuple) == (32, 5, 12, 13, 54, 2)

assert mid_last_first(a_string) == "is a stringthis "
assert mid_last_first(a_tuple) == (13, 12, 5, 32, 2, 54)
