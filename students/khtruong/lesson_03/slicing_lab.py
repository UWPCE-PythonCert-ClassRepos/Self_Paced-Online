"""Sample module docstrings text
"""


def exchange_seq(seq):
    """Return a copy of sequence with the first and last items exchanged."""
    mod_seq = seq[-1:] + seq[1:-1] + seq[:1]
    return mod_seq


def remove_seq(seq):
    """Return a copy of sequence with every other item removed."""
    mod_seq = seq[::2]
    return mod_seq


def remove_seq_v2(seq):
    """Return a copy of sequence with the first 4 and the last 4 items removed,
    and then every other item in between."""
    mod_seq = remove_seq(seq[4:-4])
    return mod_seq


def reverse_seq(seq):
    """Return a copy of sequence with the elements reversed
    (just with slicing)."""
    mod_seq = seq[::-1]
    return mod_seq


def reorder_seq(seq):
    """Return a copy of sequence with the middle third, then last third,
    then the first third in the new order."""
    third = int(len(seq) / 3)
    mod_seq = seq[third:] + seq[:third]
    return mod_seq


a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

# exchange first and last check
assert exchange_seq(a_string) == "ghis is a strint"
assert exchange_seq(a_tuple) == (32, 54, 13, 12, 5, 2)

# remove every other item check
assert remove_seq(a_string) == "ti sasrn"
assert remove_seq(a_tuple) == (2, 13, 5)

# remove first 4, last 4, and every other item in between check
assert remove_seq_v2(a_string) == " sas"
assert remove_seq_v2(a_tuple) == ()

# reverse check
assert reverse_seq(a_string) == "gnirts a si siht"
assert reverse_seq(a_tuple) == (32, 5, 12, 13, 54, 2)

# reorder check
assert reorder_seq(a_string) == "is a stringthis "
assert reorder_seq(a_tuple) == (13, 12, 5, 32, 2, 54)
