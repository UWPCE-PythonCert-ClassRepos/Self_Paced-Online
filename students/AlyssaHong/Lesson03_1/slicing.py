"""
Author: Alyssa Hong
Date: 10/22/2018
Update: 10/24/2018
Lesson3 Assignments > Slicing Lab Exercise
"""
#Get the basics of sequence slicing downself.

#Test items:
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

#1 with the first and last items exchanged.
def exchange_first_last(seq):
    a_new_sequence = seq[-1:] + seq[1:-1] + seq[:1]
    print("result #1:", a_new_sequence)
    return a_new_sequence

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)


#2 with every other item removed.
def every_other_item_remove(seq):
    a_new_sequence = seq[::2]
    print("result #2:", a_new_sequence)
    return a_new_sequence

assert every_other_item_remove(a_string) == "ti sasrn"
assert every_other_item_remove(a_tuple) == (2, 13, 5)

#3 with the first 4 and the last 4 items removed, and then every other item
# in between.
def select_item_and_remove(seq):
    a_new_sequence = seq[4:-4]
    print("result #3:", a_new_sequence)
    return a_new_sequence

assert select_item_and_remove(a_string) == " is a st"
assert select_item_and_remove(a_tuple) == ()

#4 with the elements reversed (just with slicing).
def elements_reverse(seq):
    a_new_sequence = seq[::-1]
    print("result #4:", a_new_sequence)
    return a_new_sequence

assert elements_reverse(a_string) == "gnirts a si siht"
assert elements_reverse(a_tuple) == (32, 5, 12, 13, 54, 2)

#5 with the middle third, then last third, then the first third in the new order.
def each_third_reorder(seq):
    dividend = len(seq)
    quotient = int(dividend/3)
    middle_third = seq[quotient:quotient+quotient]
    last_third = seq[quotient+quotient:dividend]
    first_third = seq[:quotient]
    a_new_sequence = middle_third + last_third + first_third
    print("result #5:", a_new_sequence)
    return a_new_sequence

assert each_third_reorder(a_string) == "is a stringthis "
assert each_third_reorder(a_tuple) == (13, 12, 5, 32, 2, 54)
