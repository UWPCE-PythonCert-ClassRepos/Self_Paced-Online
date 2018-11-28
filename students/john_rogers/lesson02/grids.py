#!/usr/bin/env python3
# create basic grid structures
# Author: JohnR


def grid(num):
    """Simple grid with single input"""
    print('+', '-' * num, '+', '-' * num, '+')
    for i in range(num):
        print('|', " " * num, '|', " " *num, '|')
    print('+', '-' * num, '+', '-' * num, '+')
    for i in range(num):
        print('|', " " * num, '|', " " *num, '|')
    print('+', '-' * num, '+', '-' * num, '+')


grid(8)


def multi_grid(boxes, size):
    
