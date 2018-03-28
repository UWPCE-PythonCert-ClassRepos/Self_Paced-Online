"""
Generalize base_grid.py by writing a function parameterized by integer
cell size to print a two-row by two-column grid of arbitrary size.
"""


def print_grid(cell_length):
    """print a 2-row by 2-column grid of integer cell length."""
    plus = '+'
    pipe = '|'

    for x in range(2):
        print(2*(plus + ' ' + cell_length*('- ')) + plus)
        for y in range(cell_length):
            print(2*(pipe + ' ' + 2*cell_length*(' ')) + pipe)
    print(2*(plus + ' ' + cell_length*('- ')) + plus)


print_grid(7)
