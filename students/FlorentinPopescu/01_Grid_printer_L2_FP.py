# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 18:43:06 2019
@author: Florentin Popescu
"""

#=============LESSON_02======================
#-------------Grid printer exercise ---------
#============================================ 

#--------------------------------------------
# PART A - Simple 2x2 grid
#--------------------------------------------
for i in range(2):
    print('+', '-'*4, '+', '-'*4, '+', end = ' ')
    print()
    for j in range(4):    
        print('|', ' '*4, '|', ' '*4, '|', end = ' ')
        print()
print('+', '-'*4, '+', '-'*4, '+', end = ' ')
#----------------------------------------------

#--------------------------------------------
# PART B - Expandable 2x2 grid via one-argument function
#--------------------------------------------
def print_grid(n):
    # gardians
    if not isinstance(n, int):
        print('Number of cell size must be integer! \nPlease enter an integer argument.')
        return None  
    elif n <= 0:
        print ('Cell size cannot be negative or zero! \nPlease enter a positive argument.')
        return None
    
    for i in range(2):
        print('+', '-'*n, '+', '-'*n, '+', end = ' ')
        print()
        for j in range(n):    
            print('|', ' '*n, '|', ' '*n, '|', end = ' ')
            print()
    print('+', '-'*n, '+', '-'*n, '+', end = ' ')
    print()
    
print_grid(3)
print_grid(15)
#----------------------------------------------

#----------------------------------------------
# PART C - Expandable muiti-gid grid via two-argument function
#----------------------------------------------

# Option 1 - using nested for loops
def print_grid2(m, n):
    # gardians
    if not (isinstance(m, int) and isinstance(n, int)):
        print('Number of cells and cell size must be integeres! \nPlease enter integer arguments.')
        return None  
    elif (m <= 0 or n <= 0):
        print ('Number of cells and cell size cannot be negative or zero! \nPlease enter positive arguments.')
        return None
    
    for i in range(m):
        print(('+' + '-'*n)*m +'+', end = ' ')
        #print(('+' + ' -'*n)*m +'+', end = ' ') #un-comment for square
        print()
        for j in range(n):    
            print(('|' + ' '*n)*(m+1), end = ' ')
            #print(('|' + '  '*n)*(m+1), end = ' ') #un-comment for square
            print()
    print(('+' + '-'*n)*m + '+', end = ' ')
    #print(('+' + ' -'*n)*m + '+', end = ' ') #un-comment for square
    print()
    
print_grid2(3, 4)
print_grid2(5, 3)

#---------------------------------------------
# Option 2 - using drowing functions
from __future__ import print_function 
def print_plus():
    print('+', end = ' ')
def print_dash():
    print('-', end = ' ')
def print_bar():
    print('|', end = ' ')
def print_space():
    print(' ', end = ' ')
def print_end():
    print()
def nothing():
    pass

def print_grid2(m, n):
    # gardians
    if not (isinstance(m, int) and isinstance(n, int)):
        print('Number of cells and cell size must be integeres! \nPlease enter integer arguments.')
        return None  
    elif (m <= 0 or n <= 0):
        print ('Number of cells and cell size cannot be negative or zero! \nPlease enter positive arguments.')
        return None
    
    def number_of_cubes(f): #control number of cubes
        for i in range(1, m + 1):
            f()
    def cub_size(f): #control cub side
        for i in range(1, n + 1):
            f()
    
    def control_number_cubes(f, g, h):
        f()
        number_of_cubes(g)
        h()
    def control_cub_size(f, g, h):
        f()
        cub_size(g)
        h()
    
    def print_beam():
        control_cub_size(nothing, print_dash, print_plus)     
    def print_post():
        control_cub_size(nothing, print_space, print_bar)
    def print_multiple_beams():
        control_number_cubes(print_plus, print_beam, print_end)
    def print_multiple_posts():
        control_number_cubes(print_bar, print_post, print_end)
    def print_row():
        control_cub_size(nothing, print_multiple_posts, print_multiple_beams)
    
    control_number_cubes(print_multiple_beams, print_row, nothing)

print_grid2(3, 4)
print_grid2(5, 3)

#=============================================
# END
#=============================================