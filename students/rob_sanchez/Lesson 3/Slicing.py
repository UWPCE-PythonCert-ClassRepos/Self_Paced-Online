#!/usr/bin/env python3
import sys

# Returns a string with the first and last items exchanged
def exchange_first_last(seq):
    first_item = seq[:1]
    last_item = seq[-1:]
    in_between = seq[1:-1]
    new_seq = last_item + in_between + first_item
    return new_seq


# Removes every other item from the sequence
def remove_every_other(seq):
    new_seq = seq[::2]
    return new_seq


# Removes the first and last four items from a sequence, then removes every
# other item.
def remove_first_last_four(seq):
    first_four = seq[4:]
    last_four = first_four[:-4]
    new_seq = remove_every_other(last_four)
    return new_seq


# Reverses all elements in the sequence
def reverse_sequence(seq):
    new_seq = seq[::-1]
    return new_seq


# Divides the sequence into thirds and returns the middle, last,
# and first third of the sequence
def mid_last_first(seq):
    length = len(seq)//3
    mid = seq[length:-length]
    last = seq[-length:]
    first = seq[:length]
    new_seq = mid + last + first
    return new_seq


# Test values
nums = (99, 32, 51, 47, 23, 93, 18)
str = "Difficult roads often lead to beautiful destinations"

# Assert statements
assert exchange_first_last(nums) == (18, 32, 51, 47, 23, 93, 99)
assert exchange_first_last(str) == "sifficult roads often lead to beautiful destinationD"

assert remove_every_other(nums) == (99, 51, 23, 18)
assert remove_every_other(str) == "Dfiutrasotnla obatfldsiain"

assert remove_first_last_four(nums) == ()
assert remove_first_last_four(str) == "iutrasotnla obatfldsia"

assert reverse_sequence(nums) == (18, 93, 23, 47, 51, 32, 99)
assert reverse_sequence(str) == "snoitanitsed lufituaeb ot dael netfo sdaor tluciffiD"

assert mid_last_first(nums) == (51, 47, 23, 93, 18, 99, 32)
assert mid_last_first(str) == "ften lead to beautiful destinationsDifficult roads o"
