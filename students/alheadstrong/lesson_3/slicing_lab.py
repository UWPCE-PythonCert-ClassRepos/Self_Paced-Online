def exchange_first_last(seq):
    """Return sequence with first and last items exchanged."""
    return seq[-1:]+seq[1:-1]+seq[0:1]


def every_other(seq):
    """Return sequence with every other item removed."""
    return seq[::2]


def first_last_chop(seq):
    """Return sequence with the first 4 and the last 4 items removed, and then every other item in between."""
    return seq[4:-4:2]


def reverse(seq):
    """Return sequence with the elements reversed."""
    return seq[::-1]


def third_reorder(seq):
    """Return sequence with the first, middle and last thirds reordered"""
    third = len(seq)//3
    return seq[third:-third]+seq[-third:]+seq[:third]


if __name__ == '__main__':
    """used as test block"""
    a_string = 'this is a string'
    a_tuple = (2, 54, 13, 12, 5, 32)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

    assert every_other(a_string) == "ti sasrn"
    assert every_other(a_tuple) == (2, 13, 5)

    assert first_last_chop(a_string) == " sas"
    assert first_last_chop(a_tuple) == ()

    assert reverse(a_string) == "gnirts a si siht"
    assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)

    assert third_reorder(a_string) == "is a stringthis "
    assert third_reorder(a_tuple) == (13, 12, 5, 32, 2, 54)

    print("tests passed")
