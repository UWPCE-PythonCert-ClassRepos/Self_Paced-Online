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
