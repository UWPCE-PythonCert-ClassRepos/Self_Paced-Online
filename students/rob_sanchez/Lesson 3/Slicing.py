import sys

#Returns a string with the first and last items exchanged
def exchange_first_last(seq):
    first_item = seq[:1]
    last_item = seq[-1:]
    in_between = seq[1:-1]
    new_seq = last_item + in_between + first_item
    return new_seq

#Removes every other item from the sequence
def remove_every_other(seq):
    new_seq = seq[::2]
    return new_seq

#Removes the first and last four items from a sequence, then removes every other item.
def remove_first_last_four(seq):
    first_four = seq[4:]
    last_four = first_four[:-4]
    new_seq = remove_every_other(last_four)
    return new_seq

#Reverses all elements in the sequence
def reverse_sequence(seq):
    new_seq = seq[::-1]
    return new_seq
#Divides the sequence into thirds and returns the middle, last, and first third.
def mid_last_first(seq):
    l=len(seq)/3
    mid = seq[l:-l]
    last = seq[-l:]
    first = seq[:l]
    new_seq = mid + last + first
    return new_seq
