#!/usr/bin/env python3
# Ian Letourneau
# 4/26/2018
# A script with various sequencing functions


def exchange_first_last(seq):
    """A function to exchange the first and last entries in a sequence"""
    return seq[-1:] + seq[1:-1] + seq[:1]


def remove_every_other(seq):
    """A function to remove every other entry in a sequence"""
    return seq[::2]


def remove_four(seq):
    """A function that removes the first 4 and last four entries in a sequence,
        and then removes every other entry in the remaining sequence"""
    return seq[4:-4:2]


def reverse(seq):
    """A function that reverses a seq"""
    return seq[::-1]


def thirds(seq):
    """A function that splits a sequence into thirds,
            then returns a new sequence using the last, first, and middle thirds"""
    length = len(seq)
    return seq[int(length/3*2):] + seq[0:int(len(seq)/3)] + seq[int(len(seq)/3):int(len(seq)/3*2)]


if __name__ == '__main__':
    """A testing block to ensure all functions are operating as expected"""
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 15, 22, 63, 75, 20, 8, 12, 5, 32)
    s_third = "123456789"
    t_third = (1, 2, 3, 4, 5, 6, 7, 8, 9)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (
        32, 54, 13, 15, 22, 63, 75, 20, 8, 12, 5, 2)

    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 22, 75, 8, 5)

    assert remove_four(a_string) == " sas"
    assert remove_four(a_tuple) == (22, 75)

    assert reverse(a_string) == "gnirts a si siht"
    assert reverse(a_tuple) == (32, 5, 12, 8, 20, 75, 63, 22, 15, 13, 54, 2)

    assert thirds(s_third) == "789123456"
    assert thirds(t_third) == (7, 8, 9, 1, 2, 3, 4, 5, 6)

    print("All tests passed my fellow coders!")
