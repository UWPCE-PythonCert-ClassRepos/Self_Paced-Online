#!/usr/bin/env python3
"""
Write some functions that take a sequence as an argument, and return a copy of that sequence:
with the first and last items exchanged.
with every other item removed.
with the first 4 and the last 4 items removed, and then every other item in between.
with the elements reversed (just with slicing).
with the middle third, then last third, then the first third in the new order.

Author: JohnR
Version: 1.2
Date: 12/7/2018
Notes: Added third assertion test for each function.
"""


def main():
    """
    Basic script logic and assertion tests.
    :return: Output of assertion tests and call/print each function.
    """

    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_test = "1 2 3 4 5 6 7 8 9 0"

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert exchange_first_last(a_test) == "0 2 3 4 5 6 7 8 9 1"
    assert every_other_removed(a_string) == "ti sasrn"
    assert every_other_removed(a_tuple) == (2, 13, 5)
    assert every_other_removed(a_test) == "1234567890"
    assert first_four_last_four(a_string) == " sas"
    assert first_four_last_four(a_tuple) == ()
    assert first_four_last_four(a_test) == "345678"
    assert reversed_slicing(a_string) == "gnirts a si siht"
    assert reversed_slicing(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert reversed_slicing(a_test) == "0 9 8 7 6 5 4 3 2 1"
    assert middle_last_first(a_string) == "is a stringthis "
    assert middle_last_first(a_tuple) == (13, 12, 5, 32, 2, 54)
    assert middle_last_first(a_test) == "4 5 6 7 8 9 01 2 3 "

    print('*' * 40)
    print('All assertion tests have passed.')
    print('*' * 40)

    print('Original string: ' + a_string)
    print('Original tuple: ' + str(a_tuple))
    print('Original test: ' + a_test)
    print('*' * 40)
    print('Swap first and last elements:')
    print(exchange_first_last(a_string))
    print(exchange_first_last(a_tuple))
    print(exchange_first_last(a_test))
    print('*' * 40)

    print('Every other element removed:')
    print(every_other_removed(a_string))
    print(every_other_removed(a_tuple))
    print(every_other_removed(a_test))
    print('*' * 40)

    print('Removed first four, last four, and every other element:')
    print(first_four_last_four(a_string))
    print(first_four_last_four(a_tuple))
    print(first_four_last_four(a_test))
    print('*' * 40)

    print('Elements reversed:')
    print(reversed_slicing(a_string))
    print(reversed_slicing(a_tuple))
    print(reversed_slicing(a_test))
    print('*' * 40)

    print('Middle third - last third - first third: ')
    print(middle_last_first(a_string))
    print(middle_last_first(a_tuple))
    print(middle_last_first(a_test))


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


def middle_last_first(seq):
    """
    Slice into thirds and then return middle, last and first.
    :param seq: String to manipulate.
    :return: String in order of middle, last then first.
    """
    third = len(seq)//3
    return seq[third:-third] + seq[-third:] + seq[:third]


if __name__ == '__main__':
    main()
