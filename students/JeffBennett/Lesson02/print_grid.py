"""
Create a function that takes one integer argument and prints a grid.
The grid has a two-by-two cellular structure and is parameterized by
cell length.  Cell length refers to total pipes on a left cell edge or total
minus signs on a top cell edge.  All cells are equal squares.
"""


def print_grid(cell_length):
    """Print a 2-row by 2-column grid with integer cell length."""
    plus = '+'
    pipe = '|'

    for x in range(2):
        print(2*(plus + ' ' + cell_length*('- ')) + plus)
        for y in range(cell_length):
            print(2*(pipe + ' ' + 2*cell_length*(' ')) + pipe)
    print(2*(plus + ' ' + cell_length*('- ')) + plus)


print_grid(6)
