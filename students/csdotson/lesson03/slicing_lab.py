# Lesson 3 - Slicing Lab Excercise

def exchange_first_last(seq):
    # Returns copy of sequence where first and last items exchanged
    return seq[-1:] + seq[1:-1] + seq[:1]


def every_other_removed(seq):
    # Returns copy of sequence with every other item removed
    return seq[::2]


def first_4_last_4(seq):
    # Returns copy of sequence where the first 4 and the last 4 items removed, and then every other item in between
    return seq[4:-4:2]


def reverse_seq(seq):
    # Returns copy of sequence with the elements reversed
    return seq[::-1]


def shuffle_thirds(seq):
    # Returns copy of sequence with the middle third, then last third, then the first third in the new order
    n = len(seq)
    first_third = int(n/3)
    second_third = int(n/3 * 2)

    return seq[first_third:second_third] + seq[second_third:n] + seq[0:first_third]



# Assertion Testing
a_string = "this is a string"
a_long_string = "thequickbrownfox"
a_tuple = (2, 54, 13, 12, 5, 32)
a_list = [1, 9, 2, 8, 3, 7, 4, 6, 5]

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert exchange_first_last(a_list) ==  [5, 9, 2, 8, 3, 7, 4, 6, 1]

assert every_other_removed(a_list) == [1, 2, 3, 4, 5]
assert every_other_removed(a_tuple) == (2, 13, 5)

assert first_4_last_4(a_list) == [3]
assert first_4_last_4(a_long_string) == 'ucbo'

assert reverse_seq(a_long_string) == 'xofnworbkciuqeht'
assert reverse_seq(a_tuple) == (32, 5, 12, 13, 54, 2)

assert shuffle_thirds(a_tuple) == (13, 12, 5, 32, 2, 54)
assert shuffle_thirds(a_list) == [8, 3, 7, 4, 6, 5, 1, 9, 2]
assert shuffle_thirds(a_string) == 'is a stringthis '

print("All tests have passed!")
