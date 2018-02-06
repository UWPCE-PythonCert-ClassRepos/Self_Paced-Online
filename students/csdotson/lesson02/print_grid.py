# Lesson 2 Assignment - Grid Printer

def print_grid(n):
    # Define rows to print
    horizontal = ("+ " + ("- " * n)) * 2 + "+"
    vertical = ("|" + (" " * (2 * n + 1))) * 2 + "|"

    # Do the printing
    print(horizontal)
    for i in range(n):
        print(vertical)
    print(horizontal)
    for i in range(n):
        print(vertical)
    print(horizontal)


def print_grid2(grid_dim, cell_size):
    # Define rows to print
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
