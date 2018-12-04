"""
Slicing Excercise

Tasks

Write some functions that take a sequence as an argument, and return a copy of that sequence:

-with the first and last items exchanged. - -with every other item removed. - -with the first 4 and the last 4 items removed, and then every other item in between. - -with the elements reversed (just with slicing). - -with the middle third, then last third, then the first third in the new order.

Your functions should look like:

def exchange_first_last(seq):
return a_new_sequence

Tests:

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

assert mid_last_first(a_string) == "is a stringthis "
assert mid_last_first(a_tuple) == (13, 12, 5, 32, 2, 54)

Write a test or two like that for each of the above functions. 
"""

a_string = "this is a string"  
a_tuple = (2, 54, 13, 12, 5, 32) 

#first and last items exchanged

def exchange_first_last(seq):
    if len(seq) == 1:
        return seq
    elif len(seq) == 2:
        return seq[-1:]+seq[0:1]
    else:
        return seq[-1:]+seq[1:-1]+seq[0:1]

#tests
assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2) 

#every other item removed

def every_other_item(seq):
    return seq[::2]

#
assert every_other_item(a_string) == 'ti sasrn'
assert every_other_item(a_tuple) == (2,13,5)

#with the first 4 and the last 4 items removed, and then every other item in between.  
#string = " sast"
#tuple = 

def first_last_four_every_other(seq):
    return seq[4:-4:2]

assert first_last_four_every_other(a_string) == " sas"
assert first_last_four_every_other(a_tuple) == ()

#with the elements reversed (just with slicing)

def reverse(seq):
    return seq[::-1]

assert reverse(a_string) == "gnirts a si siht"
assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)

#with the middle third, then last third, then the first third in the new order. 
#string = "this is a string", middle 5, last 6, first 5 = 'is a ','string','this '
#tuple = (2, 54, 13, 12, 5, 32), middle 2, last 2, first 2 = (13,12,5,32,2,54)

def thirds(seq):
    th = round(len(seq)/3)
    return seq[th:]+seq[:th]

assert thirds(a_string) == "is a stringthis "
assert thirds(a_tuple) == (13,12,5,32,2,54) 

