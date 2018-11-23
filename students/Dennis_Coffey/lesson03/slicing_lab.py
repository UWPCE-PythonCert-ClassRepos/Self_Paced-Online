# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 17:46:01 2018

@author: denni
"""

"""Lesson 3 - Slicing Lab assignment"""

a_list1 = [1,2,3,4,5]
a_list2 = ['string', 'sequence','test']
a_list3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
a_tuple = ('string', 'sequence','test')
a_string = 'this that and the other'

#Function that returns sequence with the first and last items exchanged
def exchange_first_last(seq):
    #Check to make sure len is greater than 1
    if len(seq) < 2:
        new_sequence = seq
    else:
        new_sequence = seq[-1:] + seq[1:-1] + seq[:1]
    return new_sequence

#print(exchange_first_last(a_string))

#Function that returns sequence with every other item removed
def every_other_removed(seq):
    new_sequence = seq[::2]
    return new_sequence

#print(every_other_removed((1,2,3)))

#Function that returns sequence with the elements reversed
def elements_reversed(seq):
    new_sequence = seq[::-1]
    return new_sequence

#print(elements_reversed([]))

#Function that returns sequence with the first 4 and the last 4 items removed,
#and then every other item in between
def first4_last4_every_other_removed(seq):
    new_sequence = every_other_removed(seq[4:-4])
    return new_sequence

#print(first4_last4_every_other_removed(a_string))

#Function that returns sequence with the middle third, then last third, 
#then the first third in the new order
def mid_last_first(seq):
    thirdsize = len(seq)//3
    new_sequence = seq[thirdsize:-thirdsize] + seq[-thirdsize:] + seq[:thirdsize]
    return new_sequence

#print(mid_last_first(a_list3))
    
if __name__ == "__main__":
    """Tests for validating slicing functions are working properly"""
    print('Running tests')
    
    #test exchange_first_last function
    assert exchange_first_last(a_string) == "rhis that and the othet"
    assert exchange_first_last(a_tuple) == ('test', 'sequence','string')
    assert exchange_first_last(a_list1) == [5,2,3,4,1]
    assert exchange_first_last(a_list2) == ['test', 'sequence','string']
    assert exchange_first_last([1]) == [1]

    #test every_other_removed function
    assert every_other_removed(a_string) == "ti htadteohr"
    assert every_other_removed(a_tuple) == ('string', 'test')
    assert every_other_removed(a_list1) == [1,3,5]
    assert every_other_removed(a_list2) == ['string', 'test']
    assert every_other_removed([1]) == [1]

    #test elements_reversed function
    assert elements_reversed(a_string) == "rehto eht dna taht siht"
    assert elements_reversed(a_tuple) == ('test', 'sequence','string')
    assert elements_reversed(a_list1) == [5,4,3,2,1]
    assert elements_reversed(a_list2) == ['test', 'sequence','string']
    assert elements_reversed([7,6,8,9,0,1]) == [1,0,9,8,6,7]

    #test first4_last4_every_other_removed function
    assert first4_last4_every_other_removed(a_string) == " htadteo"
    assert first4_last4_every_other_removed(a_tuple) == ()
    assert first4_last4_every_other_removed(a_list3) == [5,7,9,11]
    assert first4_last4_every_other_removed(a_list2) == []
    assert first4_last4_every_other_removed([7,6,8,9,0,1,'a','dog',4,10,3,'w',5,15,'hh',88,'m']) == [0,'a',4,3,5]

    #test mid_last_first function
    assert mid_last_first(a_string) == "at and the otherthis th"
    assert mid_last_first(a_tuple) == ('sequence', 'test','string')
    assert mid_last_first(a_list3) == [6,7,8,9,10,11,12,13,14,15,1,2,3,4,5]
    assert mid_last_first(a_list2) == ['sequence', 'test','string']
    assert mid_last_first([7,6,8,9,0,1]) == [8,9,0,1,7,6]

    print('Tests passed')