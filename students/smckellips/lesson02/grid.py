#! /usr/bin/env python
def grid():
    row = '+ - - - - + - - - - +'
    column = '|         |         |\n'
    print(row)
    print(column * 4,end='')
    print(row)
    print(column * 4,end='')
    print(row)
grid()