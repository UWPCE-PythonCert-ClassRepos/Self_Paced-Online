# Joshua Bone - UW Python 210 - Lesson 3
# 12/9/2018
# Slicing Lab Exercise


def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[0:1]


def remove_every_other(seq):
    return seq[::2]


def mid_last_first(seq):
    l = len(seq)
    a, b, c = seq[0:l//3], seq[l//3:2*l//3], seq[2*l//3:]
    return b + c + a


def mid_every_other(seq):
    return seq[4:-4][::2]


def reversed(seq):
    return seq[::-1]


if __name__ == "__main__":
    # Note: these test cases were copied from problem statement:
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert mid_last_first(a_string) == "is a stringthis "
    assert mid_last_first(a_tuple) == (13, 12, 5, 32, 2, 54)
    # Note: These test cases were written by the student:
    assert reversed(a_string) == "gnirts a si siht"
    assert reversed(a_tuple) == (32, 5, 12, 13, 54, 2)
    b_string = "A quick brown fox jumped over the lazy dog"
    b_tuple = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377)
    assert mid_every_other(b_string) == "ikbonfxjme vrtelz"
    assert mid_every_other(b_tuple) == (5, 13, 34)
    print("Tests passed.")

