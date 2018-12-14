# slicing.py
#
#
# Coder: LouReis

def copy_sequence(seq):
    """Return a copy of the sequence entered"""
    return seq

def copy_first_last(seq):
    """Return the first and last items of the sequence entered"""
    return seq[0],seq[-1]

def copy_every_other(seq):
    """Return every other item in the sequence entered"""
    return seq[::2]

def copy_rem_first_4_last_4(seq):
    """Return the remaining every other items after removing first 4 & last 4."""
    return seq[4:-4:2]
