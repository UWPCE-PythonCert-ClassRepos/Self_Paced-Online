"""
Write some functions that take a sequence as an argument, and return a copy of
that sequence:

with the first and last items exchanged.
with every other item removed.
with the first 4 and the last 4 items removed, and then every other item
in between.
with the elements reversed (just with slicing).
with the middle third, then last third, then the first third in the new order.
"""


def swap_first_and_last(seq):
    """exchange the first and last elements of a sequence"""
    new_sequence = seq[-1] + seq[1:-1] + seq[0]
    return new_sequence


def odd_index_extraction(seq):
    """remove every other element of a sequence"""
    new_sequence = seq[::2]
    return new_sequence


def everyOtherNoFirstOrLast4(seq):
    """remove first and last 4 items of sequence and every other in between"""
    new_sequence = seq[4:-4:2]
    return new_sequence


def reversal(seq):
    """reverse elements of a sequence"""
    new_sequence = seq[::-1]
    return new_sequence


def permute_thirds(seq):
    """present middle third, last third, then first third of a sequence
        If length not divisible by three, excess is allocated to new middle."""
    new_sequence = seq[len(seq)/3:] + seq[:len(seq)/3]
    return new_sequence


print(permute_thirds('123456789abcdef'))
