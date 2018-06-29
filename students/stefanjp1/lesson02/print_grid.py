
def print_grid(cell_size, cells_across=2):
    """Return a square grid of different sizes and number of cells."""
    cell_size_adj = cell_size // cells_across
    
    for row in range(cells_across):
        print('+' + (' -' * cell_size_adj + ' +') * cells_across )
        
        for i in range(cell_size_adj):
            print('|' + ('  ' * cell_size_adj + ' |') * cells_across )
    
    print('+' + (' -' * cell_size_adj + ' +') * cells_across )


print_grid(3)

print_grid(15)


def print_grid2(cells_across, cell_size):
    """Return a square grid of different sizes and number of cells."""
    
    for row in range(cells_across):
        print('+' + (' -' * cell_size + ' +') * cells_across )
        
        for i in range(cell_size):
            print('|' + ('  ' * cell_size + ' |') * cells_across )
    
    print('+' + (' -' * cell_size + ' +') * cells_across )


print_grid2(3,4)

print_grid2(5,3)

