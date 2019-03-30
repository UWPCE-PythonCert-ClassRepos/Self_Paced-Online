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

def grid_n_o(n,o):
    row = plus + ((' ' + minus) * o + ' ' + plus) * n
    column = wall + (' ' * 2 * o + ' ' + wall) * n + '\n'
    print(row)
    for i in range(1,o + 1):
        print(column * n, end = '')
        print(row)
grid_n_o(2,3)
grid_n_o(3,2)


