

'''
function with the first and last items exchanged
'''
def exchange_first_last(seq):
    a_new_sequence = seq[-1:]+seq[1:-1]+seq[:1]
    return a_new_sequence

'''
function with every other item removed
'''
def remove_other(seq):
    a_new_sequence = seq[0:len(seq):2]
    return a_new_sequence

'''
function with the first 4 and the last 4 items removed, and then every other item in between
'''
def remove_first_last_four(seq):
    a_new_sequence = seq[0:-4][4:]
    another_sequence = remove_other(a_new_sequence)
    return another_sequence

'''
function with the elements reversed (just with slicing)
'''
def reverse_seq(seq):
    a_new_sequence = seq[::-1]
    return a_new_sequence

'''
function with the middle third, then last third, then the first third in the new order
'''
def switch_third(seq):
    third = int(len(seq)/3)
    a_new_sequence = seq[third:len(seq)]+seq[0:third]
    return a_new_sequence



a_string = "this is a string"
a_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (9, 2, 3, 4, 5, 6, 7, 8, 1)
assert switch_third(a_string) == "is a stringthis "
assert switch_third(a_tuple) == (4, 5, 6, 7, 8, 9, 1, 2, 3)