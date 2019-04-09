"""Reorder sequences using slicing only"""

import copy
#I am intentionally using copy instead of sequence_copy = sequence[:]
#because I don't like the shallow copy behavior that allows changing
#elements in a list of lists to effect the original
#I want to get in the habit of using copy remembering that this can happen

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
a_long_tuple = (2, 54, 13, 12, 5, 32)*2

def exchange_last_first(sequence):
    """Reorder sequence switching the first and last elements"""
    new_sequence = copy.copy(sequence)
    first = new_sequence[:1]
    last = new_sequence[-1:]
    center = new_sequence[1:-1]
    return last+center+first

def skip_every_other(sequence):
    """Remove every other element in the sequence"""
    new_sequence = copy.copy(sequence)
    return new_sequence[::2]

def center_skip_every_other(sequence):
    """Remove first 4 and the last 4 items removed, and then every other item"""
    new_sequence = copy.copy(sequence)
    return new_sequence[4:-4][::2]

def reverse(sequence):
    """Reverse the sequence"""
    new_sequence = copy.copy(sequence)
    return new_sequence[::-1]

def mid_last_first(sequence):
    """Move the first third of the sequence to the end"""
    new_sequence = copy.copy(sequence)
    third_length = round(len(sequence)/3)
    return new_sequence[third_length:]+new_sequence[:third_length]

def tests():
    """Test the ________ functions"""
    assert exchange_last_first(a_string) == "ghis is a strint"
    assert exchange_last_first(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert skip_every_other(a_string) == "ti sasrn"
    assert skip_every_other(a_tuple) == (2, 13, 5)
    assert center_skip_every_other(a_string) == " sas"
    assert center_skip_every_other(a_long_tuple) == (5, 2)
    assert reverse(a_string) == "gnirts a si siht"
    assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert mid_last_first(a_string) == "is a stringthis "
    assert mid_last_first(a_tuple) == (13, 12, 5, 32, 2, 54)

def exercise_demo(func_in, string_in = a_string, tuple_in = a_tuple):
    print(f'Lesson3: Slicing Exercise - {func_in.__doc__}')
    print(f'{string_in} becomes {func_in(string_in)}')
    print(f'{tuple_in} becomes {func_in(tuple_in)}')
    print('')

if __name__ == "__main__":
    tests()
    print('Lesson3: Slicing Exercise')
    exercise_demo(exchange_last_first)
    exercise_demo(skip_every_other)
    exercise_demo(center_skip_every_other, tuple_in = a_long_tuple)
    exercise_demo(reverse)
    exercise_demo(mid_last_first)
