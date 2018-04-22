# Brandon Henson
# Lesson 3
# Slicing
# 4/4/18


# with the first and last items exchanged
def exchange_first_last(seq):
    return(seq[-1:] + seq[1: -1] + seq[:1])


# with every other item removed
def every_other_removed(seq):
    return (seq[::2])


# the first 4 and the last 4 items removed, and then every other item
def first_last_removed_ev_other(seq):
    return (seq[4:-4:2])


# with the elements reversed (just with slicing)
def elements_reversed(seq):
    return (seq[-1::-1])


# the middle third, then last third, then the first third in the new order
def mid_last_first(seq):
    sections = len(seq) // 3
    firstsec = seq[:sections]
    middlesec = seq[sections:sections]
    lastsec = seq[sections:]
    return(middlesec + lastsec + firstsec)

# Tests
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
test_list = (1, 2, 3, 4, 5, 6, 7, 8, 9)
test_list2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
# Write a test or two like that for each of the above functions.
assert mid_last_first(test_list) == (4, 5, 6, 7, 8, 9, 1, 2, 3)
assert elements_reversed(test_list) == (9, 8, 7, 6, 5, 4, 3, 2, 1)
assert first_last_removed_ev_other(test_list2) == (5, 7, 9, 11)
assert every_other_removed(test_list) == (1, 3, 5, 7, 9)
