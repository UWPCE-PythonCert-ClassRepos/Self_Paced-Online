#Part 1

def makingGrid():
    """Print a grid"""
    fullline = '+ - - - - + - - - - +'
    emptyline = '|         |         |'
    print(fullline)
    print(emptyline)
    print(emptyline)
    print(emptyline)
    print(emptyline)
    print(fullline)
    print(emptyline)
    print(emptyline)
    print(emptyline)
    print(emptyline)
    print(fullline)

makingGrid()

#Part 2   

def print_grid(grid_size):
    """Print a grid for which the size is determined by user input"""
    side_len = grid_size // 2
    row = "+" + " - " * side_len + "+" + " - " * side_len + "+"
    column = "|" + " " * (side_len * 3) + "|" + " " * (side_len * 3) + "|"
    print(row)
    for a in range(side_len):
        print(column)
    print(row)
    for a in range(side_len):
        print(column)
    print(row)

#print_grid(3)
#print_grid(15)

#Part 3

def print_grid2(grid_size, unit_number):
    """Print a grid for which the size and number of units are determined by user input"""
    top_row = ('+ ' + '- ' * grid_size) * unit_number + '+' + '\n'
    middle_row = ('| ' + ' ' * 2 * grid_size) * unit_number + '|' + '\n'
    row = top_row + middle_row * grid_size
    grid = row * unit_number + top_row
    print(grid)

#print_grid2 (3,4)
#print_grid2 (5,3)















def boxOfSetSize(boxsize):
    """This is a function that makes a 2x2 grid - user must specify size"""
    halfsize = floor(boxsize/2)
    filledline = '+ '+'- '*halfsize+'+ '+'- '*halfsize+'+'
    emptyline = '| ' + '  ' * halfsize + '| ' + '  ' * halfsize + '|'
    print(filledline)
    for i in range(halfsize):
        print(emptyline)
    print(filledline)
    for i in range(halfsize):
        print(emptyline)
    print(filledline)



def print_grid(size):
    """
    print a 2x2 grid with a total size of size
    :param size: total size of grid -- it will be rounded if not one more than
        a multiple of 2
    """
    number = 2
    box_size = int((size - 1) // 2)  # size of one grid box: integer division
    print("box_size:", box_size)
    # top row
    top = ('+ ' + '- ' * box_size) * number + '+' + '\n'
    middle = ('| ' + ' ' * 2 * box_size) * number + '|' + '\n'

    row = top + middle * box_size

    grid = row * number + top

    print(grid)


def print_grid2(number, size):
    """
    print a number x number grid with each box of size width and height
    :param number: number of grid boxes (row and column)
    :param size: size of each grid box
    """
    # top row
    top = ('+ ' + '- ' * size) * number + '+' + '\n'
    middle = ('| ' + ' ' * 2 * size) * number + '|' + '\n'

    row = top + middle * size

    grid = row * number + top

    print(grid)


def print_grid3(size):
    """
    same as print_grid, but calling print_grid2 to do the work
    """
    number = 2
    box_size = (size - 1) // 2  # size of one grid box: note integer divsion!
    print_grid2(number, box_size)


print_grid_trivial()

print_grid(11)
print_grid(7)

print_grid2(3, 3)
print_grid2(3, 5)

print_grid3(11)
