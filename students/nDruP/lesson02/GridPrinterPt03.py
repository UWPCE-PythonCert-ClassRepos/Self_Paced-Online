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
    printPlusMinus(space,size)
    for y in range(space):
        for x in range(size):
            printBarSpace(space,size)
        printPlusMinus(space,size)
    return

def printPlusMinus(space,size):
    print('+', end='')
    for plus in range(space):
        for minus in range(size):
            print(' -',end='')
        print(' +', end='')
    print()
    return

def printBarSpace(space,size):
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
