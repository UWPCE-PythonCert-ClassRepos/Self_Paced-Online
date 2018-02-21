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

# Task5

def print_fruits(input):
    """Print fruits in input in 2 ways specified in the assignment"""
    print(f'The weight of an {input[0][:-1]} is {input[1]} and the '
          f'weight of an {input[2][:-1]} is {input[3]}')
    print(f'The weight of an {input[0][:-1].upper()} is {input[1] * 1.2} and '
          f'the weight of an {input[2][:-1].upper()} is {input[3] * 1.2}')


def table_format(input):
    """Prints formatted table from input list of tuples"""
    print('Name      Age     Cost')
    for row in input:
        print(f'{row[0]:<10}{row[1]:<8}{row[2]:<8}')



def print_consecutive_tuples(input):
    """Print elements of input tuple in 5 character columns"""
    print(('{:<5}'*len(input)).format(*input))