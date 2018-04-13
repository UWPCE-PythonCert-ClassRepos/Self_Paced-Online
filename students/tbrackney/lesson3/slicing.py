"""
File Name: slicing.py
Author: Travis Brackney
Class: Python 201 - Self paced online
Date Created 3/11/2018
Python Version: 3.6.4
"""


def swap_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]


def every_other(seq):
    return seq[0:-1:2]


def cut4(seq):
    return seq[4:-4:2]


def reverse(seq):
    return seq[::-1]


def thirds(seq):
    segment = len(seq)//3
    return seq[segment:-segment] + seq[-segment:] + seq[:segment]


a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

assert swap_first_last(a_string) == "ghis is a strint"
assert swap_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

assert every_other(a_string) == "ti sasrn"
assert every_other(a_tuple) == (2, 13, 5)

assert cut4(a_string) == " sas"
assert cut4(a_tuple) == ()

assert reverse(a_string) == "gnirts a si siht"
assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)

assert thirds(a_string) == 'is a stringthis '
assert thirds(a_tuple) == (13, 12, 5, 32, 2, 54)
