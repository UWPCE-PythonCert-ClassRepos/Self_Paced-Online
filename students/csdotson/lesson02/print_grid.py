# Lesson 2 Assignment - Grid Printer

def print_grid(n):
    # Define rows to print
    horizontal = ("+ " + ("- " * n)) * 2 + "+"
    vertical = ("|" + (" " * (2*n + 1))) * 2 + "|"

    # Do the printing
    print(horizontal)
    for i in range(n):
        print(vertical)
    print(horizontal)
    for i in range(n):
        print(vertical)
    print(horizontal)


def print_grid2():
