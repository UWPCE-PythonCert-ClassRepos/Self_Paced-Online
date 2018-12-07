#!/usr/bin/env python3
"""
Write some functions that take a sequence as an argument, and return a copy of that sequence:
with the first and last items exchanged.
with every other item removed.
with the first 4 and the last 4 items removed, and then every other item in between.
with the elements reversed (just with slicing).
with the middle third, then last third, then the first third in the new order.

Author: JohnR
Version: 0.1
Date: 12/6/2018
"""


def main():
    """
    Basic script logic and assertion tests.
    :return: Output of assertion tests and call each function.
    """

    # TODO: Create and test assertions for each function
    # assert exchange_first_last(a_string) == "ghis is a strint"
    # assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    # assert mid_last_first(a_string) == "is a stringthis "
    # assert mid_last_first(a_tuple) == (13, 12, 5, 32, 2, 54)
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    print('Swap first and last elements:')
    print(exchange_first_last(a_string))
    print(exchange_first_last(a_tuple))

    print()
    print('Every other element removed:')
    print(every_other_removed(a_string))
    print(every_other_removed(a_tuple))

    print()
    print('Removed first four, last four, and every other element:')
    print(first_four_last_four(a_string))
    print(first_four_last_four(a_tuple))

    print()
    print('Elements reversed:')
    print(reversed_slicing(a_string))
    print(reversed_slicing(a_tuple))

    print()


def exchange_first_last(seq):
    """
    Exchange the first and last items.
    :param seq: String to manipulate.
    :return: String with first and last elements reversed.
    """
    return seq[-1:] + seq[1:-1] + seq[:1]


def every_other_removed(seq):
    """
    Remove every other item.
    :param seq: String to manipulate.
    :return: String with every other element removed.
    """
    return seq[0::2]


def first_four_last_four(seq):
    """
    Remove the first four, last four, and every other item in between.
    :param seq: String to manipulate.
    :return: String with first and last four items removed along with every
    other item in between.
    """
    result = seq[4:-4]
    return result[0::2]


def reversed_slicing(seq):
    """
    Reverse the items by using a slice.
    :param seq: String to manipulate.
    :return: String with elements reversed.
    """
    return seq[::-1]


# TODO: Code and test middle/last/first function
def middle_last_first(seq):
    """
    Slice into thirds and then return middle, last and first.
    :param seq: String to manipulate.
    :return: String in order of middle, last then first.
    """
    pass


if __name__ == '__main__':
    main()
