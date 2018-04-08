"""
Write some functions that take a sequence as an argument, and return
a copy of that sequence:

with the first and last items exchanged.
with every other item removed.
with the first 4 and the last 4 items removed, and then every other item
in between.
with the elements reversed (just with slicing).
with the middle third, then last third, then the first third in the new
order.
"""


def exchange_first_last(seq):
    """exchange first and last elements of a sequence of length >= 2."""
    return seq[-1] + seq[1:-1] + seq[0]


def remove_every_other(seq):
    """remove every other element of a sequence of length >= 2."""
    return seq[::2]


def remove_first_last_4_and_every_other(seq):
    """remove first and last 4 items and every other item in between of a
       sequence of length >=9."""
    return seq[4:-4:2]


def reversal(seq):
    """reverse elements of a sequence of length >=1."""
    return seq[::-1]


def permute_thirds(seq):
    """present middle third, last third, then first third of a sequence
       of length >=3.
       If length not divisible by three, new middle receives excess."""
    return seq[len(seq)//3:] + seq[:len(seq)//3]


if __name__ == "__main__":
    assert exchange_first_last('ab') == 'ba'
    assert exchange_first_last('abc') == 'cba'
    assert exchange_first_last('abcdef') == 'fbcdea'
    assert remove_every_other('abc') == 'ac'
    assert remove_every_other('abcdef') == 'ace'
    assert remove_first_last_4_and_every_other('012345678') == '4'
    assert remove_first_last_4_and_every_other('0123456789') == '4'
    assert remove_first_last_4_and_every_other('0123456789abcd') == '468'
    assert reversal('a') == 'a'
    assert reversal('ab') == 'ba'
    assert reversal('abc') == 'cba'
    assert permute_thirds('abc') == 'bca'
    assert permute_thirds('0123456789abcdef') == '56789abcdef01234'
    assert permute_thirds('0123456789abcdefg') == '56789abcdefg01234'

    print("tests passed")
