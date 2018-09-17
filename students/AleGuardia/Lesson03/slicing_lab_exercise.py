# Slicing Lab Exercise - Lesson 3 - by Alejandro Guardia


def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[0:1]


def remove_every_other_item(seq):
    return seq[::2]


def first_last_four_remove_every_other(seq):
    return seq[4:-4][::2]


def reverse_elements(seq):
    return seq[-1::-1]


def mid_last_first(seq):
    third = len(seq)//3
    return seq[third:-third] + seq[-third:] + seq[:third]


a_string = "this is a string"
a_tuple = (2,54,13,12,5,32)


assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

assert remove_every_other_item(a_string) == "ti sasrn"
assert remove_every_other_item(a_tuple) == (2,13,5)

assert first_last_four_remove_every_other(a_string) == " sas"
assert first_last_four_remove_every_other(a_tuple) == ()

assert reverse_elements(a_string) == "gnirts a si siht"
assert reverse_elements(a_tuple) == (32,5,12,13,54,2)

assert mid_last_first(a_string) == "is a stringthis "
assert mid_last_first(a_tuple) == (13, 12, 5, 32, 2, 54)




