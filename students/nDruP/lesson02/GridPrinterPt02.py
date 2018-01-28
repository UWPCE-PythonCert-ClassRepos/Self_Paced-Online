"""
Print grid based on given parameter.
print_grid(3) would print:

+ - + - +
|   |   |
+ - + - +
|   |   |
+ - + - +

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
    printPlusMinus(n)
    for y in range(2):
        for x in range(n//2):
            printBarSpace(n)
        printPlusMinus(n)
    return

def printPlusMinus(n):
    print('+', end='')
    for plus in range(2):
        for minus in range(n//2):
            print(' -',end='')
        print(' +', end='')
    print()
    return

def printBarSpace(n):
    print('|',end='')
    for bar in range(2):
        print(' '*(n+((n+1)%2)),end='')
        print('|',end='')
    print()
    return

print('print_grid(3)')
print_grid(3)
print('print_grid(8)')
print_grid(8)
print('print_grid(15)')
print_grid(15)
