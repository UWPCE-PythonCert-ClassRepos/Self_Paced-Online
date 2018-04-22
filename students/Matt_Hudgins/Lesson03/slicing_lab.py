'''
    File Name: series.py
    Author: Matt Hudgins
    Date created: 4/2/2018
    Date last modified: 4/2/2018
    Python Version 3.6.4
'''
# The following sequences will be used for the slicing lab exercise
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
string = 'The first ten digits of pi!'


def exchange_first_last(seq):
    """ This function when called will exchange the first and last
    items of the sequence"""
    return(seq[-1:] + seq[1:-1] + seq[0:1])


def every_other_removed(seq):
    """ This function when called will remove every other item in the
    sequence"""
    return(seq[::2])


def every_other_remove_with_firstlast4_removed_aswell(seq):
    """ This function when called will remove the first and last items
    of the sequence and in addition remove every other item in the
    sequence"""
    firstlast4removed = seq[4:-4]
    return(firstlast4removed[::2])


def a_quick_switch_aroo(seq):
    """ This function when called will reverse the items in the
    sequence"""
    return(seq[::-1])


def another_swith_aroo(seq):
    """ This function when called will switch the middle third then
    last third, then the first third in the new order."""
    first_third = int(len(seq) / 3)
    second_third = int(2 * len(seq) / 3)
    new_seq_5 = seq[second_third:] + seq[first_third:] + seq[:first_third]
    return(new_seq_5)


# A quick check that the functions are working properly


exchange_first_last(data)
exchange_first_last(string)
every_other_removed(data)
every_other_removed(string)
every_other_remove_with_firstlast4_removed_aswell(data)
every_other_remove_with_firstlast4_removed_aswell(string)
a_quick_switch_aroo(data)
a_quick_switch_aroo(string)
another_swith_aroo(data)
another_swith_aroo(string)


# A quick test that the funcitons are working properly

assert exchange_first_last(data) == [5, 1, 4, 1, 5, 9, 2, 6, 5, 3, 3]
assert exchange_first_last(string) == '!he first ten digits of piT'
assert every_other_removed(data) == [3, 4, 5, 2, 5, 5]
assert every_other_removed(string) == 'Tefrttndgt fp!'
assert every_other_remove_with_firstlast4_removed_aswell(data) == [5, 2]
assert every_other_remove_with_firstlast4_removed_aswell(string) == 'frttndgt f'
assert a_quick_switch_aroo(data) == [5, 3, 5, 6, 2, 9, 5, 1, 4, 1, 3]
assert a_quick_switch_aroo(string) == '!ip fo stigid net tsrif ehT'
assert another_swith_aroo(data) == [6, 5, 3, 5, 1, 5, 9, 2, 6, 5, 3, 5, 3, 1, 4]
assert another_swith_aroo(string) == 'ts of pi! ten digits of pi!The first'

















