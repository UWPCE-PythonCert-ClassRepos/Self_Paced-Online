"""# Instructions
## Goal
Get the basics of sequence slicing down.
## Tasks
* Write some functions that take a sequence as an argument, and return a copy of that sequence:
** with the first and last items exchanged.
** with every other item removed.
** with the first 4 and the last 4 items removed, and then every other item in between.
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
    pass

def remove_every_other(seq):
    """return sequence with every other item removed.  First item in sequence remains
    args:
        seq: sequence to be modified
    returns:
        copy of sequence with every other item removed"""
    pass

def mid_last_first(a_string):
    pass

if __name__ == '__main__':
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert mid_last_first(a_string) == "is a stringthis "
    assert mid_last_first(a_tuple) == (13, 12, 5, 32, 2, 54)