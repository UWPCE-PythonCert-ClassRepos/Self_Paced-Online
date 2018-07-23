#!/usr/bin/env python3

def task_one():
    return("file_{:0>3d}: {:.2f}, {:.2e}, {:.2e}".format( 2, 123.4567, 10000, 12345.67))

def task_two():
    nums = ( 2, 123.4567, 10000, 12345.67)
    return(f'file_{nums[0]:0>3}: {nums[1]:.2f}, {nums[2]:.2e}, {nums[3]:.2e}')

def task_three(in_tuple):
    size = len(in_tuple)
    form_string = "The "+ str(size) + " numbers are " + '{:d}, ' * (size-1) + '{:d}.'
    return(form_string.format(*in_tuple))

def task_four():
    return ("{3} {4} {2} {0} {1}".format( 4, 30, 2017, 2, 27))

def task_five():
    items = ['orange', 1.3, 'lemon', 1.1]
    return (f'The weight of an {items[0]} is {items[1]} and the weight of a {items[2]} is {items[3]}')
    return (f'The weight of an {items[0].upper()} is {items[1] * 1.2} and the weight of a {items[2].upper()} is {items[3] * 1.2}')
./