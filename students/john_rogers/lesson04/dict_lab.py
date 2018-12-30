#!/usr/bin/env python3
"""
Ungraded practice assignment for dictionaries and sets.
Author: JohnR
Version: 1.0
Date: 12/27/2018
Notes:
"""


def main():
    """
    Core script logic, global variables, various function calls
    :return:
    """

    my_dictionary = dict_1()
    print()
    print('results of the first dictionary: ')
    print(my_dictionary)
    new_dict = dict_2(my_dictionary)
    print()
    print('second dictionary looks like this: ')
    print(new_dict)
    set_1()

    print()
    set_2()


def dict_1():
    """
    Create a dictionary containing name, city, cake for chris from Seattle
    Display dictionary
    Delete entry for cake
    Display dictionary
    Add entry for fruit with mango, and display again
    Display keys, then values
    Display whether or not cake is a key in the dictionary
    Display whether or not mango is a value in the dict
    :return: Dictionary
    """
    db = {
        'name': 'chris',
        'city': 'seattle',
        'cake': 'chocolate',
        'car': 'Toyota',
        'book': 'catcher in the rye',
    }

    print(db)
    del db['cake']
    print(db)
    db['fruit'] = 'mango'
    print(db)
    print(db.keys())
    print(db.values())
    if 'cake' in db.keys():
        print('yes, cake is in the dictionary')
    else:
        print('sorry, no cake in this dictionary')

    if 'mango' in db.values():
        print('si, tengo mango hoy')
    else:
        print('no tengo mango mi amigo')

    return db


def dict_2(data):
    """
    Use dictionary from dict_1 using the same keys but with the number
    of 't's in each value as the value; remember to check for upper
    and lower case.
    Display new dictionary.
    :return: New dictionary with updated values
    """
    db2 = {}
    for k, v in data.items():
        t_count = v.lower().count('t')
        db2[k] = t_count

    return db2


def set_1():
    """
    Create sets s2, s3 and s4 that contain numbers from 0-40, divisible
    by 2, 3 and 4.
    Display the sets.
    Display if s3 is a subset of s2 (false)
    Display if s4 is a subset of s2 (true)
    :return: None
    """
    s2 = set()
    for i in range(1, 21):
        if i % 2 == 0:
            s2.update([i])

    s3 = set()
    for i in range(1, 21):
        if i % 3 == 0:
            s3.update([i])

    s4 = set()
    for i in range(1, 21):
        if i % 4 == 0:
            s4.update([i])

    print(s2)
    print(s3)
    print(s4)

    if s3.issubset(s2):
        print('True')
    else:
        print('false')

    if s4.issubset(s2):
        print('Yes, s4 is in s2.')
    else:
        print('negative')


def set_2():
    """
    Create a set with the letters in Python and add 'i' to the set.
    Create a frozenset with the letters in 'marathon'.
    Display the union and intersection of the two sets.
    :return:
    """
    sp = set()
    for c in 'python':
        sp.update(c)
    print(sp)
    sp.add('i')
    print()
    print(sp)

    fr_set = set()
    for c in 'marathon':
        fr_set.update(c)

    print(fr_set)

    foo = fr_set.intersection(sp)
    print(foo)

    bar = sp.union(fr_set)
    print(bar)


if __name__ == '__main__':
    main()
