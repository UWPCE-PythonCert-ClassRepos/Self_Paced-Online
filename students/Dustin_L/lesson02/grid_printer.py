#!/usr/bin/env python3


def print_fixed_grid():
    '''
    This function prints a 2 x 2 cell grid where length = width = 8
    '''

    tmb = '+ - - - - + - - - - +\n'
    bars = '|         |         |\n'

    print(tmb + (4 * bars) + tmb + (4 * bars) + tmb)


if __name__ == '__main__':
    print_fixed_grid()
