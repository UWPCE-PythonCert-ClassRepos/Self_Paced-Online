import sys
import os

POS = "+ "
NEG = "- "
PIPE = '|'
SPACE = ' '

def print_grid(n=2):
    '''
    simple print prid function that print 
    '''
    print_grid_base(n, n,4)

def print_grid2(size, cellSize):
    print_grid_base(size, size, cellSize)

def print_grid_base(rowSize=2, colSize=3, cellSize=4):
    '''
    function to print a grid with given rowSize, colSize and cellSize
    '''

    horizontal = POS
    vertical = PIPE
    for i in range(cellSize):
        horizontal += NEG
    
    horizontal = (horizontal *colSize) + POS
    
    for i in range(colSize):
        vertical += (" " * ((cellSize * 2) +1)) + PIPE 
    

    for i in range(rowSize):
        print(horizontal)
        for i in range(cellSize): 
            print(vertical)
    print(horizontal)


print_grid(4)

print_grid2(3,2)




