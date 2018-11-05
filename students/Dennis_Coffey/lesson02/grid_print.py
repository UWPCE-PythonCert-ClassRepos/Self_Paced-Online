# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 20:17:59 2018

@author: dennis
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

#function to return each row of grid
def grid_row(a,b,edge,middle):
    c = edge
    for i in range(a):
        c += middle * b + edge
    return c

#function to create grid for part 3
def print_grid2(a,b):
    
    print(grid_row(a,b,plus,minus))
    for i in range(a):
        for j in range(b):
            print(grid_row(a,b,pipe,space))
        print(grid_row(a,b,plus,minus)) 

print('Grid for Part 1')
grid_part1()

print('Grid for Part 2')
print_grid(7)    

print('Grid for Part 3')
print_grid2(5,3)
