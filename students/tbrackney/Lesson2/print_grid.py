"""
File Name: print_grid.py
Author: Travis Brackney
Class: Python 201 - Self paced online
Date Created 2/3/2018
Python Version: 3.6.4
"""


def print_grid(n):
    """ Prints a simple grid"""
    spaces = n // 2
    segment = '+ ' + '- ' * spaces
    border = 2 * segment + '+'
    mid_segment = '| ' + (spaces * '  ')
    mid_line = 2 * mid_segment + '|'
    for i in range(2):
        print(border)
        for j in range(spaces):
            print(mid_line)
    print(border)


def print_grid2(cell_count, cell_length):
    spaces = cell_length
    segment = '+ ' + '- ' * spaces
    border = cell_count * segment + '+'
    mid_segment = '| ' + (spaces * '  ')
    mid_line = cell_count * mid_segment + '|'
    for i in range(cell_count):
        print(border)
        for j in range(spaces):
            print(mid_line)
    print(border)
