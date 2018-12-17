#!/usr/bin/env python3

def print_grid (grid_size = 1, cell_size = 1):
    """This function prints a grid. print_grid(x,y) prints a grid x cells by x cells with cells of size y."""

    for i in range(grid_size):
        #Print grid row by row
        print(('+' + ' -'*cell_size + ' ')*grid_size + '+')
        for k in range(cell_size):
            print(('|' + '  '*cell_size + ' ')*grid_size + '|')

    # Finish grid with bottom line
    print(('+' + ' -'*cell_size + ' ')*grid_size + '+')
