"""
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

def print_grid(n):
    #Print 2x2 grid of size n
    printTopBottomBorder(n)
    for y in range(2):
        printSideBorder(n)
        printTopBottomBorder(n)
    return

def printTopBottomBorder(n):
    #Print 2*(n//2)+3 length Top/Bottom borders of grid spaces 
    print('+', end='')
    for plus in range(2):
        for minus in range(n//2):
            print(' -',end='')
        print(' +', end='')
    print()
    return

def printSideBorder(n):
    #Print n//2 length side borders of grid spaces
    for x in range(n//2):
        print('|',end='')
        for bar in range(2):
            print(' '*(n+(1-n%2)),end='')
            print('|',end='')
        print()
    return

print('print_grid(3)')
print_grid(3)
print('print_grid(8)')
print_grid(8)
print('print_grid(15)')
print_grid(15)
