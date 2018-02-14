"""
Part1

Print a grid that looks like:
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
"""


def print_grid1():
    #Print the above ^ grid.
    print('Part 1 Grid Printer:')
    for x in range(2):
        printPlusMinus1()
        printBarSpace1()
        printBarSpace1()
        printBarSpace1()
        printBarSpace1()
    printPlusMinus1()
    return


def printPlusMinus1():
    #Print Top, Middle, and Bottom row of grid
    for x in range(11):
        if x % 5 == 0:
            print('+ ', end='')
        else:
            print('- ', end='')
    print()
    return


def printBarSpace1():
    #Print sides of grid
    for x in range(11):
        if x % 5 == 0:
            print('| ', end='')
        else:
            print('  ', end='')
    print()
    return


print_grid1()


"""
Part 2

Print grid based on given parameter.
print_grid(3) would print:
+ - + - +
|   |   |
+ - + - +
|   |   |
+ - + - +

print_grid(8):
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +


print_grid(15) prints:
+ - - - - - - - + - - - - - - - +
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
+ - - - - - - - + - - - - - - - +
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
+ - - - - - - - + - - - - - - - +
"""


def print_grid2(n):
    #Print 2x2 grid of size n
    printTopBottomBorder2(n)
    for y in range(2):
        printSideBorder2(n)
        printTopBottomBorder2(n)
    return


def printTopBottomBorder2(n):
    #Print 2*(n//2)+3 length Top/Bottom borders of grid spaces
    print('+', end='')
    for plus in range(2):
        for minus in range(n // 2):
            print(' -', end='')
        print(' +', end='')
    print()
    return


def printSideBorder2(n):
    #Print n//2 length side borders of grid spaces
    for x in range(n // 2):
        print('|', end='')
        for bar in range(2):
            print(' ' * (n + (1 - n % 2)), end='')
            print('|', end='')
        print()
    return


print('\n\nGrid Printer part 2:')
print('print_grid(3)')
print_grid2(3)
print('print_grid(8)')
print_grid2(8)
print('print_grid(15)')
print_grid2(15)


"""
Part 3

Write a function that draws a similar grid with a
specified number of rows and columns, and with each cell a given size.

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


def print_grid3(space, size):
    """
    Print a (space x space) grid with (size x size) grid spaces
    """
    printTopBottomBorder3(space, size)
    for y in range(space):
        printSideBorder3(space, size)
        printTopBottomBorder3(space, size)
    return


def printTopBottomBorder3(space, size):
    """
    Print a Top/Bottom border(s) for (space) amount of
    (size x size) large grid spaces.
    """
    print('+', end='')
    for plus in range(space):
        for minus in range(size):
            print(' -', end='')
        print(' +', end='')
    print()
    return


def printSideBorder3(space, size):
    """
    Print side border(s) for (space) amount of
    (size x size) large grid spaces
    """
    for x in range(size):
        print('|', end='')
        for bar in range(space):
            print('  ' * size, end='')
            print(' |', end='')
        print()
    return

print('\n\nGrid Printer Part 3:')
print('print_grid(3.4)')
print_grid3(3, 4)
print('print_grid(2,4)')
print_grid3(2, 4)
print('print_grid(2,7)')
print_grid3(2, 7)
