# python3

# grid.py

# functions that draws a grid

#  --------------------  Ex. 1  --------------------

def draw_grid_1():
    """
    no options
    2 x 2 grid
    4 x 4 cell size
    """
    rows = 10
    columns = 20
    for row in range(rows + 1):
        if row == 0 or row % 5 == 0:
            for column in range(columns + 1):
                if column == 0 or column % 10 == 0:
                    print('+', end='')
                elif column % 2 != 0:
                    print(' ', end='')
                else:
                    print('-', end='')
            print()
        else:
            for column in range(columns + 1):
                if column == 0 or column % 10 == 0:
                    print('|', end='')
                else:
                    print(' ', end='')
            print()


def draw_grid_2():
    """
    no options
    2 x 2 grid
    4 x 4 cell size
    """
    rows = 10
    plus = '+'
    divider = ' - - - - '
    open    = '         '
    bar = "|"

    horizontal_divider = plus + divider + plus + divider + plus
    vertical_divider = bar + open + bar + open + bar

    for row in range(rows + 1):
        if row == 0 or row % 5 == 0:
            print(horizontal_divider)
        else:
            print(vertical_divider)

#  --------------------  Ex. 2  --------------------

def draw_grid_3(m):
    """
    one options
    m: cell size, m x m
    grid is 2 x 2
    """
    if m % 2 == 1 and m > 4:
        n = m - 1
    elif m % 2 == 0 and m > 4:
        n = m - 2
    rows = n
    columns = 2 * n
    half = rows // 2
    for row in range(rows + 1):
        if row == 0 or row % half == 0:
            for column in range(columns + 1):
                if column == 0 or column % (2 * half) == 0:
                    print('+', end='')
                elif column % 2 != 0:
                    print(' ', end='')
                else:
                    print('-', end='')
            print()
        else:
            for column in range(columns + 1):
                if column == 0 or column % (2 * half) == 0:
                    print('|', end='')
                else:
                    print(' ', end='')
            print()

#  --------------------  Ex. 3  --------------------

class Grid:

    """
    grid_size is the number of cells in the grid, grid_size x grid_size
    cell_size is the size of each cell, cell_size x cell_size
    """

    def __init__(self, grid_size, cell_size):
        self.g_size = grid_size
        self.c_size = cell_size
        self.h_divider = "-".join(" " * (self.c_size + 1))
        self.v_fill = " ".join(" " * (self.c_size + 1))
        self.top = self.h_divider.join("+" * (self.g_size + 1)) + "\n"
        # looks something like this:  + - - - - + - - - - + - - - - +
        self.inbetween = self.v_fill.join("|" * (self.g_size + 1)) + "\n"
        # looks something like this:  |         |         |         |

    def __grid(self):
        """
        assembles the '+ - - - - + - - - - + - - - - +'
        and the       '|         |         |         |'
        to make a grid
        """
        inbetween_row = self.c_size * self.inbetween
        g = (self.top + inbetween_row) * self.g_size + self.top
        return g

    def __str__(self):
        """
        returns a string in shape of the grid
        """
        return self.__grid()

def print_grid(m, n):
        """
        m: print a grid of size m, a square m x m grid,
        n: each cell in the grid is of size n, n x n cell
        """
        gr = Grid(m, n)
        print(gr)
