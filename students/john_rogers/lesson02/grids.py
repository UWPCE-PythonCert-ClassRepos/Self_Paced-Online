#!/usr/bin/env python3
# create basic grid structures
# Author: JohnR


def g():
    """Print a grid with no user input"""
    horizontal_line = '+ - + - +'
    vertical_line = '|   |   |'
    print(horizontal_line)
    print(vertical_line)
    print(horizontal_line)
    print(vertical_line)
    print(horizontal_line)


g()


def grid(num):
    """Simple grid with single input, the size of the boxes"""
    if num >= 2:
        num = round(num / 2)
    else:
        num = 1
    print('+', '-' * num, '+', '-' * num, '+')
    for i in range(num):
        print('|', " " * num, '|', " " * num, '|')
    print('+', '-' * num, '+', '-' * num, '+')
    for i in range(num):
        print('|', " " * num, '|', " " * num, '|')
    print('+', '-' * num, '+', '-' * num, '+')


grid(15)


# TODO: Fix this ugly mess
def multiple_grids(boxes, size):
    """ take in two values, number of boxes and size of each box"""
    plus = '+ '
    dash = '- '
    wall = '|'

    horizontal = (plus + dash * size) * boxes + plus
    vertical = (wall + ((' ' * size) + wall) * boxes)
    print(horizontal)
    for i in range(size):
        print((vertical + '\n') * size + horizontal)


multiple_grids(2, 6)









