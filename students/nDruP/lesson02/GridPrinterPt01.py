"""
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
#Print the above ^ grid.
def printGrid1():
    print('Part 1 gridPrinter')
    for x in range(2):
        printPlusMinus1()
        printBarSpace1()
        printBarSpace1()
        printBarSpace1()
        printBarSpace1()
    printPlusMinus1()
    return
    
#Print Top, Middle, and Bottom row of grid
def printPlusMinus1():
    for x in range(11):
        if x%5==0:
            print('+ ',end='')
        else:
            print('- ',end='')
    print()
    return

#Print sides of grid
def printBarSpace1():
    for x in range(11):
        if x%5==0:
            print('| ',end='')
        else:
            print('  ',end='')
    print()
    return

printGrid1()
