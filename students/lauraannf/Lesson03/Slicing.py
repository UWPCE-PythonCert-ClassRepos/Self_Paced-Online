"""
Created on Fri Sep  7 12:57:43 2018

@author: Laura.Fiorentino
"""


def exchange_first_last(seq):
    return (seq[-1:] + seq[1:-1] + seq[0:1])


a_string = "you are a string"
a_tuple = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22)
assert exchange_first_last(a_string) == "gou are a striny"
assert exchange_first_last(a_tuple) == (22, 4, 6, 8, 10, 12, 14, 16, 18, 20, 2)


def every_other_removed(seq):
    return seq[0::2]


assert every_other_removed(a_string) == "yuaeasrn"
assert every_other_removed(a_tuple) == (2, 6, 10, 14, 18, 22)


def firstlastfour(seq):
    return seq[4:-4:2]


assert firstlastfour(a_string) == "aeas"
assert firstlastfour(a_tuple) == (10, 14)


def reverse(seq):
    return seq[-1::-1]


assert reverse(a_string) == "gnirts a era uoy"
assert reverse(a_tuple) == (22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2)


def thirds(seq):
    if len(seq) % 3 != 0:
        return ('the length of the sequence isn''t divisible by three and I'
                'don''t feel like deciding how to deal with that')
    else:
        n = int(len(seq) / 3)
        return (seq[n:n+n] + seq[n+n:] + seq[:n])


a_new_string = "you are a string!!"
a_new_tuple = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24)
assert thirds(a_new_string) == "e a string!!you ar"
assert thirds(a_new_tuple) == (10, 12, 14, 16, 18, 20, 22, 24, 2, 4, 6, 8)
