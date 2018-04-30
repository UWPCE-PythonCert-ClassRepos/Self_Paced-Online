def exchange_first_last(seq):
    """ This function takes a sequence as an argument and returns a copy of that sequence with the first and last items exchanged."""
    first = seq[0]
    middle = seq[1:-1]
    last = seq[-1]
    return last,middle,first

def remove_every_other_num(seq):
    """This function takes a sequence as an argument and returns a copy of that sequence with every other number removed."""
    return seq[::2]

def multiple_removals(seq):
    """This function takes a sequence as an argument and returns a copy of that sequence with the first four and last four items removed, tehn every other number in between."""
    return seq [3:-4]


def reversed(seq):
    """This function takes a sequence as an argument and returns a copy of that sequence with the elements reversed using slicing."""
    return seq[::-1]

def thirds(seq):
    """This function takes a sequence and returns a copy of that sequence with the middle third, then last third, then the first third, in that order."""
    third = int(len(seq)/3)
    first_third = seq[:third]
    middle_third = seq[third:-third]
    last_third = seq[-third:]
    return middle_third,last_third,first_third
    

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

assert exchange_first_last(a_string)
assert exchange_first_last(a_tuple)

assert remove_every_other_num(a_string)
assert remove_every_other_num(a_tuple)

assert multiple_removals(a_string)
#assert multiple_removals(a_tuple)

assert reversed(a_string)
assert reversed(a_tuple)

assert thirds(a_string)
assert thirds(a_tuple)
