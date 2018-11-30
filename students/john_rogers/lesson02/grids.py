#!/usr/bin/env python3
# create basic grid structures
# Author: JohnR


def main():
    print('no user input')
    g()
    print()
    print('single input, size')
    grid(3)
    print()
    print('two inputs, size and number of columns/rows')
    multiple_grids(3, 4)


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
    wall = '| '
    vertical_size = size * 2

    horizontal = (plus + dash * size) * boxes + plus
    vertical = (wall + " " * vertical_size) * boxes + wall
    print(horizontal)
    for i in range(boxes):
        print((vertical + '\n') * size + horizontal)


if __name__ == '__main__':
    main()

