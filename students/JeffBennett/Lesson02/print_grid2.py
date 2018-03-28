"""
Write a two-parameter function which prints a grid parameterized by integer n
rows and n columns, and by integer cell length.
"""


def print_grid2(n, cell_length):
    """Print an n-row by n-column grid of integer cell length."""
    plus = '+'
    pipe = '|'

    for x in range(n):
        print(n*(plus + ' ' + cell_length*('- ')) + plus)
        for y in range(cell_length):
            print(n*(pipe + ' ' + 2*cell_length*(' ')) + pipe)
    print(n*(plus + ' ' + cell_length*('- ')) + plus)


print_grid2(5, 3)
