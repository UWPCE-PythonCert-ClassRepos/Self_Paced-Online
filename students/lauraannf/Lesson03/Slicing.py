# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 12:57:43 2018

@author: Laura.Fiorentino
"""

def exchange_first_last(seq):
    return (seq[-1:] + seq[1:-1] + seq[0:1])

a_string = "you are a string"
a_tuple = (2, 4, 6, 8, 10, 12,14,16,18,20,22)

assert exchange_first_last(a_string) == "gou are a striny"
assert exchange_first_last(a_tuple) == (22, 4, 6, 8, 10, 12, 14, 16, 18, 20, 2)


def eoremoved(seq):
    return seq[0::2]
    
assert eoremoved(a_string) == "yuaeasrn"
assert eoremoved(a_tuple) == (2,6,10,14,18,22)

def firstlastfour(seq):
    return seq[4:-4:2]

assert firstlastfour(a_string) == "aeas"
assert firstlastfour(a_tuple) == (10,14)
