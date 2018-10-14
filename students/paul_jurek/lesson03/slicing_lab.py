"""# Instructions
## Goal
Get the basics of sequence slicing down.
## Tasks
* Write some functions that take a sequence as an argument, and return a copy
    of that sequence:
** with the first and last items exchanged.
** with every other item removed.
** with the first 4 and the last 4 items removed, and then every other item
    in between.
** with the elements reversed (just with slicing).
** with the middle third, then last third, then the first third in the new order.
NOTE: These should work with ANY sequence – but you can use strings to test, if you like.
Your functions should look like:
def exchange_first_last(seq):
    return a_new_sequence"""


def exchange_first_last(seq):
    """return sequence with first and last items switched"
    args:
        seq: sequence to be modified
    returns:
        modifited sequence"""
    # adding catch for 0 or 1 length to return original seq
    if len(seq) < 2:
        return seq

    start = seq[:1]
    mid = seq[1:-1]
    end = seq[-1:]

    return end + mid + start


def remove_every_other(seq):
    """return sequence with every other item removed.
        First item in sequence remains
    args:
        seq: sequence to be modified
    returns:
        copy of sequence with every other item removed"""

    return seq[::2]


def mid_every_other(seq):
    """return sequence with first 4 and last 4 items removed then every other of what remains.
        In cases of sequences less than 8 characters, empty sequence of input type is returned.
    args:
        seq: sequence to be modified
    returns:
        copy of sequence with front and end removed then every other item removed"""

    return seq[4:-4:2]


def reverse_elements(seq):
    """reverse elements in string with slicing"""
    return seq[::-1]


def mid_last_first(a_string):
    pass


if __name__ == '__main__':
    a_empty_list = []
    a_simple_list = [1]
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_longer_tuple = (2, 54, 13, 12, 5, 32, 2, 54, 13, 12, 5, 32)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert exchange_first_last(a_empty_list) == a_empty_list
    assert exchange_first_last(a_simple_list) == a_simple_list

    assert remove_every_other(a_empty_list) == a_empty_list
    assert remove_every_other(a_simple_list) == a_simple_list
    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 5)

    assert mid_every_other(a_empty_list) == a_empty_list
    assert mid_every_other(a_simple_list) == []
    assert mid_every_other(a_string) == " sas"
    assert mid_every_other(a_tuple) == ()
    assert mid_every_other(a_longer_tuple) == (5, 2)

    assert reverse_elements(a_empty_list) == a_empty_list
    assert reverse_elements(a_simple_list) == a_simple_list
    assert reverse_elements(a_string) == "gnirts a si siht"
    assert reverse_elements(a_tuple) == (32, 5, 12, 13, 54, 2)

    """
    assert mid_last_first(a_string) == "is a stringthis "
    assert mid_last_first(a_tuple) == (13, 12, 5, 32, 2, 54)
    """
