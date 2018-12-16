#!/usr/bin/env python3

def print_grid (grid_size = 1, cell_size = 1):

    for i in range(grid_size):
        print(('+' + ' -'*cell_size + ' ')*grid_size + '+')
        for k in range(cell_size):
            print(('|' + '  '*cell_size + ' ')*grid_size + '|')
    print(('+' + ' -'*cell_size + ' ')*grid_size + '+')
