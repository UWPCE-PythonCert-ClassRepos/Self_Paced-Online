# Lesson 2 Assignment - Grid Printer

def print_grid(n):
    """Print 2 x 2 grid with cell size n"""
    horizontal = ("+ " + ("- " * n)) * 2 + "+"
    vertical = ("|" + (" " * (2 * n + 1))) * 2 + "|"

    # Do the printing
    print(horizontal)
    for j in range(2):
        for i in range(n):
            print(vertical)
            if i == (n - 1):
                print(horizontal)
            else:
                continue


def print_grid2(grid_dim, cell_size):
    """Print grid_dim x grid_dim grid with given cell_size"""
    horizontal = ("+ " + ("- " * cell_size)) * grid_dim + "+"
    vertical = ("|" + (" " * (2 * cell_size + 1))) * grid_dim + "|"

    # Do the printing
    print(horizontal)
    for j in range(grid_dim):
        for i in range(cell_size):
            print(vertical)
            if i == (cell_size - 1):
                print(horizontal)
            else:
                continue
