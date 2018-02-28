#!/usr/bin/env python3

# ------------------------------------------- #
# Student:   Tri Nguyen
# Instructor: Natasha Aleksandrova
# Date:  21-Feb-2018
# ------------------------------------------- #

import os

# Declare functions


def dict_one():
    ''' practice Python dictionary '''

    a_dict = {'name': 'Tri', 'city': 'Seattle', 'cake': 'cheese'}

    # Display the dictionary

    print(a_dict, '\n')

    # Delete the entry for cake

    del a_dict['cake']

    print(a_dict, '\n')

    # Add an entry for fruit with mango

    a_dict['fruit'] = 'Mango'

    print(a_dict, '\n')

    # Display the dictionary keys
    print('Keys of "a_dict" dictionary are:')

    for key in a_dict:
        print('+', key)

    # Display the dictionary values
    print('\nValues of "a_dict" dictionary are:')

    for value in a_dict.values():
        print('+', value)

    # Check if "cake" is a key

    if 'cake' in a_dict:
        print('\nYes, there is cake.')
    else:
        print('\nNo, there is no cake')

    # Check if "Mango" is a value

    value_list = list(a_dict.values())

    if 'Mango' in value_list:
        print('\nYes, there is mango.')
    else:
        print('\nNo, there is no mango.')


def dict_two():
    ''' practice Python dictionary '''

    a_dict = {'name': 'Tri', 'city': 'Seattle', 'cake': 'cheese'}

    new_dict = {'name': a_dict['name'] + ('t'.upper() * 3),
                'city': a_dict['city'] + ('t' * 3),
                'cake': a_dict['cake'] + ('t'.upper() * 3)}
    print('\n', new_dict, '\n')


def set_one():
    ''' practice Python sets '''

    s2 = set(range(0, 21, 2))
    s3 = set(range(0, 21, 3))
    s4 = set(range(0, 21, 4))

    print('s2 =', s2, '\n')
    print('s3 =', s3, '\n')
    print('s4 =', s4, '\n')

    print('s3 is subset of s2:', s3.issubset(s2), '\n')
    print('s4 is subset of s2:', s4.issubset(s2), '\n')


def set_two():
    ''' practice Python sets '''

    a_set = set('Python')
    a_set.add('i')

    frozen_set = frozenset('marathon')

    print('Union of two sets =', a_set.union(frozen_set), '\n')
    print('Intersection of two sets =', a_set.intersection(frozen_set), '\n')


def print_full_path():
    ''' this function prints the full path
        for all files in the current directory '''

    print('Full path for all files in the current directory:')
    current_dir = os.getcwd()
    for file in os.listdir(current_dir):
        if os.path.isfile(os.path.join(current_dir, file)):
            print(os.path.join(current_dir, file))
        else:
            print(os.path.join(current_dir, file), 'is not a file.')


def copy_bin(source, destination):
    ''' this function copies a file from a source
        to a destination without using shutil, or the OS copy'''

    with open(source, 'rb') as f_source:
        with open(destination, 'wb') as f_destination:
            for data in f_source:
                f_destination.write(data)

# End of function definition

# Presentation
dict_one()

dict_two()

set_one()

set_two()

print_full_path()

copy_bin(r'C:\Users\TriNguyen\Pictures\captainAmerica.jpg', r'C:\Program Files\Git\Self_Paced-Online\students\tri_nguyen\lesson04\test.jpg')

copy_bin(r'F:\STUFF\Python Programs\secu.txt', r'C:\Program Files\Git\Self_Paced-Online\students\tri_nguyen\lesson04\test_secu.txt')
