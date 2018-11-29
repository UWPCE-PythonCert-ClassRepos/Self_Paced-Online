#!/usr/bin/env python3
# create basic grid structures
# Author: JohnR


def main():
    print('simple grid, no user input')
    g()
    print()
    print('simple grid, single input')
    grid(15)
    print()
    print('grid with two inputs, size and number of columns/rows')
    multiple_grids(3, 6)


def g():
    """Print a grid with no user input"""
    horizontal_line = '+ - + - +'
    vertical_line = '|   |   |'
    print(horizontal_line)
    print(vertical_line)
    print(horizontal_line)
    print(vertical_line)
    print(horizontal_line)


def grid(num):
    """Simple grid with single input, the size of the boxes"""
    print('+', '-' * num, '+', '-' * num, '+')
    for i in range(num):
        print('|', " " * num, '|', " " * num, '|')
    print('+', '-' * num, '+', '-' * num, '+')
    for i in range(num):
        print('|', " " * num, '|', " " * num, '|')
    print('+', '-' * num, '+', '-' * num, '+')


def multiple_grids(boxes, size):
    """Take in two values, number of boxes and size of each box"""
    plus = '+ '
    dash = '- '
    wall = '|'

    horizontal = (plus + dash * size) * boxes + plus
    vertical = (wall + ((' ' * size) + wall) * boxes)
    print(horizontal)
    for i in range(size):
        print((vertical + '\n') * size + horizontal)


if __name__ == '__main__':
    main()







