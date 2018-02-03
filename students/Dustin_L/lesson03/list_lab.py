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


def series_two(lst):
    """Performs a set of operations on list of fruit.

    A deepy copy is made of the passed list. The last item is removed from this
    copy. The user is then prompted to selet an item to be removed from list and
    all specified items are removed. If none are found, the user is continually
    prompted until the item is found in the list.

    Args:
        lst (list): List to be operated upon.

    Returns:
        list: Modified list.
    """
    l = copy.deepcopy(lst)
    print(l)

    # Remove last item
    l.pop()
    print(l)

    # Prompt user for fruit and then delete all occurences from list
    l *= 2
    while True:
        usr_in      = input('Enter fruit to remove from list' + PROMPT)
        removed_lst = [i for i in l if i.lower() != usr_in.lower()]

        if removed_lst != l:
            l = removed_lst
            print(l)
            break
        else:
            print('Specified fruit is NOT in list!')

    return l


def series_three(lst):
    """Performs a set of operations on a list of fruit.

    A deep copy is made of the passed list. The user is then prompted to specify
    which fruits in the list they like. For all that they do not like, those
    fruits are removed from the list.

    Args:
        lst (list): List to be operated upon.

    Returns:
        list: Modified list
    """
    l = copy.deepcopy(lst)

    for fruit in lst:
        usr_in = input(f'Do you like {fruit.lower()} (Yes / No)?' + PROMPT).lower()

        while (usr_in[0] != 'y') and (usr_in[0] != 'n'):
            usr_in = input('Please enter "Yes" or "No"' + PROMPT).lower()

        if usr_in.startswith('n'):
            l.remove(fruit)

    print(l)
    return l


if __name__ == '__main__':
    fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']

    series_one(fruit_list)
    series_two(fruit_list)
    series_three(fruit_list)
