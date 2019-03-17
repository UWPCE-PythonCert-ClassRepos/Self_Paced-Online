#! /usr/bin/env python
def grid():
    plus = '+'
    minus = '-'
    wall = '|'
    row = plus + (' ' + minus) * 4 + ' ' + plus + (' ' + minus) * 4 + ' ' + plus
    column = wall + ' ' * 9 + wall + ' ' * 9 + wall + '\n'
    print(row)
    print(column * 4,end='')
    print(row)
    print(column * 4,end='')
    print(row)
grid()