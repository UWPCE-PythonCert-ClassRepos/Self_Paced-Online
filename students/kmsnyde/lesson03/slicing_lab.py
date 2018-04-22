# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 16:34:45 2018

@author: Karl M. Snyder
"""

a_string = 'this is a string'
a_tuple = (2, 54, 13, 12, 5, 32)
a_list = [1,2,3,4,5,6,7,8,9]
b_string = 'This is a little longer string for testing'
num_tuple = (1,2,3,4,5,6,7,8,9)

def exchange_first_last(seq):
    return seq[-1] + seq[1:-1] + seq[0]

#change any equality string to get AssertionError
assert exchange_first_last(a_string) == 'ghis is a strint'

def every_other_item_removed(seq):
    return seq[::2]

assert every_other_item_removed(a_string) == 'ti sasrn'

def rm_first4_last4_by2(seq):
    return seq[4:-4:2]

assert rm_first4_last4_by2(b_string) == ' saltl ogrsrn o e'

def reverse_seq(seq):
    return seq[::-1]

assert reverse_seq(a_tuple) == (32, 5, 12, 13, 54, 2)

def new_order(seq):
    seq_length = len(seq)
    one_third = int(seq_length/3)
    print(seq[one_third:] + seq[:one_third]) # show result
    return seq[one_third:] + seq[:one_third]

assert new_order(list(range(20))) == [6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                16, 17, 18, 19, 0, 1, 2, 3, 4, 5]
assert new_order(list(range(10))) == [3,4,5,6,7,8,9,0,1,2]