#! /usr/bin/env python
plus = '+'
minus = '-'
wall = '|'

def grid():
    row = plus + (' ' + minus) * 4 + ' ' + plus + (' ' + minus) * 4 + ' ' + plus
    column = wall + ' ' * 9 + wall + ' ' * 9 + wall + '\n'
    print(row)
    print(column * 4,end='')
    print(row)
    print(column * 4,end='')
    print(row)

def grid_n(n):
    minus = ' -'
    row = plus + minus * n + plus + minus * n + plus
    column = wall + '  ' * n + wall + '  ' * n + wall + '\n'
    print(row)
    print(column * n, end = '')
    print(row)
    print(column * n, end = '')
    print(row)
grid_n(5)
grid_n(10)
