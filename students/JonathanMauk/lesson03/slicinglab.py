def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]


def remove_every_other(seq):
    return seq[::2]


def remove_firstlast_four(seq):
    return seq[4:(len(a_tuple) - 4):2]


def reverse_slicing(seq):
    return seq[::-1]


a_string = "abcdefghij"
a_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

assert exchange_first_last(a_string) == "jbcdefghia"
assert exchange_first_last(a_tuple) == (9, 1, 2, 3, 4, 5, 6, 7, 8, 0)

assert remove_every_other(a_string) == "acegi"
assert remove_every_other(a_tuple) == (0, 2, 4, 6, 8)

assert remove_firstlast_four(a_string) == "e"
assert remove_firstlast_four(a_tuple) == (4,)

assert reverse_slicing(a_string) == "jihgfedcba"
assert reverse_slicing(a_tuple) == (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
