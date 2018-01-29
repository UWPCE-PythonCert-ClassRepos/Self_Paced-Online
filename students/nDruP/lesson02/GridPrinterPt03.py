"""
Write a function that draws a similar grid with a specified number of rows and columns, and with each cell a given size.

For example, print_grid2(3,4) results in:

+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +

(three rows, three columns, and each grid cell four “units” in size)
"""

def print_grid(space, size):
    """
    Print a (space x space) grid with (size x size) grid spaces
    """
    printTopBottomBorder(space,size)
    for y in range(space):
        printSideBorder(space,size)
        printTopBottomBorder(space,size)
    return

def printTopBottomBorder(space,size):
    """
    Print a Top/Bottom border(s) for (space) amount of 
    (size x size) large grid spaces.
    """
    print('+', end='')
    for plus in range(space):
        for minus in range(size):
            print(' -',end='')
        print(' +', end='')
    print()
    return

def printSideBorder(space,size):
    """
    Print side border(s) for (space) amount of 
    (size x size) large grid spaces
    """
    for x in range(size):
        print('|',end='')
        for bar in range(space):
            print('  '*size,end='')
            print(' |',end='')
        print()
    return

print('print_grid(3.4)')
print_grid(3,4)
print('print_grid(2,4)')
print_grid(2,4)
print('print_grid(2,7)')
print_grid(2,7)
