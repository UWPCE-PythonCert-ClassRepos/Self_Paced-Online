#!/usr/bin/env python

"""This module runs the dictionary and set lab script.
"""


def defined_dict():
    """Return a defined dictionary."""
    return {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}


def dict1():
    """Return the Dictionary 1 assignment."""
    # Create a dictionary containing “name”, “city”, and “cake” for “Chris”
    # from “Seattle” who likes “Chocolate” (so the keys should be: “name”,
    # etc, and values: “Chris”, etc.)
    d = defined_dict()
    # Display the dictionary.
    print(d)
    # Delete the entry for “cake”.
    del d['cake']
    # Display the dictionary
    print(d)
    # Add an entry for “fruit” with “Mango” and display the dictionary.
    d['fruit'] = 'Mango'
    print(d)
    # Display the dictionary keys.
    print(d.keys())
    # Display the dictionary values.
    print(d.values())
    # Display whether or not “cake” is a key in the dictionary (i.e. False)
    # (now).
    print('cake key is in the dictionary: {}'.format('cake' in d))
    # Display whether or not “Mango” is a value in the dictionary (i.e. True).
    print('Mango value is in the dictionary: {}'.format('Mango' in d.values()))


def dict2():
    """Return the Dictionary 2 assignment."""
    # Using the dictionary from item 1: Make a dictionary using the same keys
    # but with the number of ‘t’s in each value as the value (consider upper
    # and lower case?).
    d = defined_dict()
    print(d)
    for key, val in d.items():
        d[key] = val.lower().count('t')
    print(d)

    # Sets 1
    # Create sets s2, s3 and s4 that contain numbers from zero through twenty,
    # divisible by 2, 3 and 4.
    # Display the sets.
    number_tuple = tuple(range(21))
    d = {'s2': set(), 's3': set(), 's4': set()}
    for key in d.keys():
        div_by = int(key[-1:])
        d[key] = set(divisible(number_tuple, div_by))
        print(key, d[key])
    # Display if s3 is a subset of s2 (False)
    # and if s4 is a subset of s2 (True).
    print('s3 is a subset of s2: {}'.format(d['s3'].issubset(d['s2'])))
    print('s4 is a subset of s2: {}'.format(d['s4'].issubset(d['s2'])))


def divisible(number_tuple, div_by):
    """Return the value that is divisible by some integer."""
    div_list = []
    for num in number_tuple:
        if num % div_by == 0:
            div_list.append(num)
    return div_list

if __name__ == '__main__':
    dict1()
    dict2()