# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 18:03:31 2018

@author: Karl M. Snyder
"""

def grid():
    """prints a 2x2 grid (4 cells)"""
    plus = "+"
    dash = " -" * 4 + " "
    pipe = "|"
    space = " " * 8 + " "
    line1 = plus + dash + plus + dash + plus
    line2 = pipe + space + pipe + space + pipe
    line2_rep = line2 + '\n' + line2 + '\n' + line2 + '\n' + line2
    print(line1)
    print(line2_rep)
    print(line1)
    print(line2_rep)
    print(line1)
grid()

def print_grid(num):
    """prints a 2x2 block grid (4 cells).  Parameter 'num' is the number of
    - vertical and | horizontal symbols for each cell"""
    plus = "+"
    dash = " -" * num + " "
    pipe = "|"
    space = " " * (num*2) + " "
    line1 = plus + dash + plus + dash + plus
    line2 = pipe + space + pipe + space + pipe
    line2_rep = (line2 + '\n') * num
    print(line1)
    print(line2_rep, end= '')
    print(line1)
    print(line2_rep, end= '')
    print(line1)
print_grid(5)

def print_grid(row_col, num):
    """prints a 2x2 block grid (4 cells).  Parameter 'num' is the number of
    - vertical and | horizontal symbols for each cell"""
    plus = "+"
    dash = " -" * num + " "
    pipe = "|"
    space = " " * (num*2) + " "
    
    line_1 = plus + dash + plus
    line_2 = pipe + space + pipe
    line_2_rep = (line_2 + '\n') * num
    
    line_1_add = dash + plus
    line_2_add_rep = ((pipe + space) * row_col) + pipe
    
    if row_col == 1:
        print(line_1)
        print(line_2_rep, end= '')
        print(line_1)
    else:
        print(line_1 + (line_1_add*(row_col-1)))
        for i in range(row_col):
            print((line_2_add_rep + '\n') * num, end='')
            print(line_1 + (line_1_add*(row_col-1)))
        
print_grid(3, 7)