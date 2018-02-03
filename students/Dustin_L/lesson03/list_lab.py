#!/usr/bin/env python3
"""List Lab

This module contains all of the functions for the List lab.
"""

import copy

PROMPT = ' --> '


def series_one(lst):
    """Perform a set of operations on a list of fruit.

    A deep copy is made of the passed list. A series of modifications are made
    to this copy and the copy is finally returned.

    Args:
        lst (list): List to be operated upon.

    Returns:
        list: Modified list.
    """
    l = copy.deepcopy(lst)
    print(l)

    # Prompt user for fruit and add to list
    usr_in = input('Enter fruit to add to list' + PROMPT)
    l.append(usr_in)
    print(l)

    # Prompt user for number and reply with associated fruit
    usr_in = int(input('Enter a number' + PROMPT))
    if usr_in <= len(l) and usr_in != 0:
        print(l[usr_in - 1])
    else:
        print('Invalid number!')

    # Add fruit using '+' operator
    l += ['Grape']
    print(l)

    # Add fruit using 'insert()' function
    l.insert(0, 'Mango')
    print(l)

    # Display all fruit that start with 'P'
    for fruit in l:
        if fruit.startswith('P'):
            print(fruit)

    return l


if __name__ == '__main__':
    fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']

    series_one(fruit_list)
