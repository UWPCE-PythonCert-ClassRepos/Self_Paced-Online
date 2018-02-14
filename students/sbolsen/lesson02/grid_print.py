#!/usr/bin/env python

def grid(size, multi):
    plus = '+ '
    minus = '- '
    pipe = '| '

    horizontal = (plus + minus * size) * multi + plus
    vertical = (pipe + (('  ' * size) + pipe) * size)
    print(horizontal)
    for i in range(size):
        print((vertical + '\n') * size + horizontal)

grid(1,1)
grid(3,3)
grid(5,5)
