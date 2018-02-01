#!/usr/bin/env python3


def print_row(n, sz, bottom):
    """Print a single row

    Print a single row of n cells of size sz. The bottom line of the row is only
    printed if 'bottom' is True.

    Args:
        n (int): number of cells
        sz (int): size of each cell
        bottom (bool): include bottom line if True
    """
    if n < 0 or sz < 0:
        return

    # Top and bottom line definition
    tb = ('+ ' + ('- ' * sz)) * n + '+' + '\n'
    # Inner line definition
    inner = ('| ' + (' ' * 2 * sz)) * n + '|' + '\n'

    row = tb + (sz * inner)
    if bottom:
        row += tb

    print(row, end='')


def print_fixed_grid():
    """Print a 2 x 2 cell grid where length = width = 0"""
    tmb  = '+ - - - - + - - - - +\n'
    bars = '|         |         |\n'

    print(tmb + (4 * bars) + tmb + (4 * bars) + tmb)


def print_grid(d):
    """Print a 2 x 2 cell grid where length = width = d

    Args:
        d (int): length and width of grid
    """
    if d < 0:
        return

    print_row(2, int(d / 2), False)
    print_row(2, int(d / 2), True)
    print()


def print_grid2(n, sz):
    """Print a n x n cell grid where each cell is of size sz.

    Args:
        n (int): grid dimensions
        sz (int): size of each cell
    """
    if n < 0 or sz < 0:
        return

    for i in range(n):
        print_row(n, sz, True if (i == n - 1) else False)
    print()


if __name__ == '__main__':
    print_fixed_grid()
    print_grid(4)
    print_grid2(5, 1)
