# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 20:17:59 2018

@author: denni
"""

plus = '+'
minus = '-'
pipe = '|'
space = ' '
#function to create grid for part 1
def grid_part1():
    hor_edge = plus + minus * 4 + plus + minus * 4 + plus
    ver_edge = pipe + space * 4 + pipe + space * 4 + pipe
    print(hor_edge)
    print(ver_edge)
    print(ver_edge)
    print(ver_edge)
    print(ver_edge)
    print(hor_edge)
    print(ver_edge)
    print(ver_edge)
    print(ver_edge)
    print(ver_edge)
    print(hor_edge)
    
#function to create grid for part 2
def print_grid(a):
    hor_edge = plus + minus * a + plus + minus * a + plus
    ver_edge = pipe + space * a + pipe + space * a + pipe
    print(hor_edge)
    for i in range(a):
        print(ver_edge)
    print(hor_edge)
    for i in range(a):
        print(ver_edge)
    print(hor_edge)

print_grid(7)    
#grid_part1()