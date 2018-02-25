#Part 1: Print a simple grid

def print_simple_grid():
    """
    Write a function that draws a grid like the following:

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

    Args: None
    """

    header = '+ - - - - + - - - - +'
    row = '|         |         |'
    
    for n in range(0,11):
        if n == 0 or n == 5 or n == 10:
            print(header)
        else:
            print(row)


#Part 2: Function with parameter

def print_grid(n):
    """
    Prints a grid where the size of the grid is provided by an argument.

    Args:
    n:  The size of the grid
    """

    # y is the middle divider between columns and rows
    y = int(n/2)

    header = '+ ' + (y * '- ')
    row = '| ' + (y * '  ')

    # When n is an odd number, the middle divider in inclusive. The grid is essentially the same as n - 1
    if (n % 2 == 1):
        n -= 1

    for i in range (0, n + 3 ):
        if i == 0 or i == (y + 1) or i == (n + 2):
            print (2 * header + '+')
        else:
            print (2 * row + '|')


#Part 3: Function with two parameters

def print_grid2(grid, cell):
    """
    Draws a grid with a specified number of rows and columns, and with each cell a given size.

    Args:
    grid:  The number of rows and columns in the grid.
    cell:  The size of each cell in the grid.
    """

    # Integer conversion in case of decimal numbers
    grid = int(grid)
    cell = int(cell)

    header = grid * ('+' + ' ' + (cell * '- ')) + '+'
    row = grid * ('|' + ' ' + ((2 * cell) * ' ')) + '|'
    count = 0

    while (count < grid):
        for n in range(0, cell + 1):
            if n == 0 :
                print (header)
            else:
                print (row)
        count = count + 1

    print (header)


print_simple_grid()
print()
print_grid(8)
print()
print_grid2(5,3)