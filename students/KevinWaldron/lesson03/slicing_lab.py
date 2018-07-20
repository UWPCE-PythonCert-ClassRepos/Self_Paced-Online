def exchange_first_last(seq):
    """ Swaps the first and last value in seq """
    return seq[-1:] + seq[1:-1] + seq[:1]

def every_other_removed(seq):
    """ Removes every other item from the sequence """
    return seq[::2]

def first_last_four_every_other(seq):
    """ Removes the first and last 4 items and then returns every other item from the remaining sequence """
    return seq[4:-4:2]

def reverse(seq):
    """ Reverses the sequence """
    return seq[::-1]

def middle_last_first(seq):
    """ Returns the given sequence with the middle third, then last third, and then first third """
    third = len(seq) // 3
    return seq[third:-third] + seq[-third:] + seq[:third]


if __name__ == '__main__':
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    big_tuple = (1, 5, 8, 4, 0, 88, 92, 111, 43, 26, 24, 93, 101, 10, 18)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

    assert every_other_removed(a_string) == "ti sasrn"
    assert every_other_removed(a_tuple) == (2, 13, 5)

    assert first_last_four_every_other(a_string) == " sas"
    assert first_last_four_every_other(big_tuple) == (0, 92, 43, 24)

    assert reverse(a_string) == "gnirts a si siht"
    assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)

    assert middle_last_first(a_string) == "is a stringthis "
    assert middle_last_first(a_tuple) == (13, 12, 5, 32, 2, 54)