#!/usr/bin/env python3
"""Dictionary Lab Module

Contains all functions for the Dictionary Lab Module.
"""


def dictionaries_one():
    """Test basic dictionary operations"""
    d1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
    print(d1)

    # del d1['cake']
    d1.pop('cake')
    print(d1)

    d1['fruit'] = 'Mango'
    print(d1)

    print(d1.keys())
    print(d1.values())
    if 'cake' in d1:
        print(True)
    else:
        print(False)
    if 'Mango' in d1.values():
        print(True)
    else:
        print(False)


def dictionaries_two():
    """Find number of "t's" in a dictionary"""
    d1 = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
    d2 = {}

    for k, v in d1.items():
        d2[k] = v.lower().count('t')

    print(d2)


def sets_one():
    """Test basic set operations"""
    s2 = set(range(0, 21, 2))
    s3 = set(range(0, 21, 3))
    s4 = set(range(0, 21, 4))

    print(s2)
    print(s3)
    print(s4)

    if s3.issubset(s2):
        print(True)
    else:
        print(False)
    if s4.issubset(s2):
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    dictionaries_one()
    dictionaries_two()
    sets_one()
