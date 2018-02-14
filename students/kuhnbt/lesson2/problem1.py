# Part 1


def pattern1(width):
    """ Print top/middle/last lines of grid """
    print('+' + width*'-' + '+' + width*'-' + '+')


def pattern2(width):
    """ Print inbetween lines of grid """
    print('|' + width*' ' + '|' + width*' ' + '|')


# Printing figure from part 1 of assigment

pattern1(4)
for _ in range(4):
    pattern2(4)
pattern1(4)
for _ in range(4):
    pattern2(4)
pattern1(4)

# Part 2


def pattern3(width):
    """Helper function prints top/mid/bottom pattern for
    print_grid/print_grid2"""
    print('+' + int(width/2)*'-' + '+' + int(width/2)*'-' + '+')


def pattern4(width):
    """Helper function prints inbetween pattern for
    print_grid/print_grid2"""
    print('|' + int(width/2)*' ' + '|' + int(width/2)*' ' + '|')


def print_grid(size):
    """Print a grid with height/width given by integer size. If size
    is even, rounds up to the next odd number"""
    if size % 2 == 0:
        size += 1
    for row in range(size):
        if row == 0 or row/(size-1) == .5 or size-row == 1:
            pattern3(size)
        else:
            pattern4(size)


# Part 3
def print_grid2(width, cell_size):
    """Print a grid with given width (in number of cells) and cell
    size"""
    break_line = ('+' + '-'*cell_size)*width + '+'
    fill_line = ('|' + ' '*cell_size)*width + '|'
    for cell in range(width):
        print(break_line)
        for row in range(cell_size):
            print(fill_line)
    print(break_line)