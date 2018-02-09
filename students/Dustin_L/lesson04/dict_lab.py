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


if __name__ == '__main__':
    dictionaries_one()
