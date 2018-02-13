#!/usr/bin/env python3

# Task1

def format_filenames(s):
    """Make properly formatted filename given 4-element tuple"""
    element1 = 'file_{:0>3d}: '.format(s[0])
    element2 = '{:.2f}'.format(s[1])
    element3 = '{:.2e}'.format(s[2])
    element4 = '{:.2e}'.format(s[3])
    return element1 + ', '.join([element2, element3, element4])

# Task2

def format_filenames_2(s):
    """Repeat formatted filename using fstring method"""
    return f'file_{s[0]:0>3d}: {s[1]:.2f}, {s[2]:.2e}, {s[3]:.2e}'


# Task3

def formatter(in_tuple):
    """Given tuple of varied length returns string printing values"""
    return (f"The {len(in_tuple)} numbers are: "
    f"{', '.join([str(num) for num in in_tuple])}")

# Task4

def format_tuple(input):
    """Print formatted numbers in input tuple"""
    return (f'{input[3]:0>2d} {input[4]} {input[2]} {input[0]:0>2d}'
             f' {input[1]}' )