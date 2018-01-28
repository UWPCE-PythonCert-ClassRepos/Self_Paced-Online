#!/usr/bin/env python3


def print_row(n, sz, bottom):
    '''
    This function prints a single row of n cells where each cell is of size sz.
    The bottom line of the row is only printed if 'bottom' is True.
    '''

    if n < 0 or sz < 0:
        return None

    # Top and bottom line definition
    tb = ('+ ' + ('- ' * sz)) * n + '+' + '\n'
    # Inner line definition
    inner = ('| ' + (' ' * 2 * sz)) * n + '|' + '\n'

    row = tb + (sz * inner)
    if bottom:
        row += tb

    print(row, end='')


def print_fixed_grid():
    '''
    This function prints a 2 x 2 cell grid where length = width = 8
    '''

    tmb = '+ - - - - + - - - - +\n'
    bars = '|         |         |\n'

    print(tmb + (4 * bars) + tmb + (4 * bars) + tmb)


def print_grid(d):
    '''
    This function prints a 2 x 2 cell grid where length = width = d
    '''

    if d < 0:
        return None

    print_row(2, int(d / 2), False)
    print_row(2, int(d / 2), True)
    print()


if __name__ == '__main__':
    print_fixed_grid()
    print_grid(4)
