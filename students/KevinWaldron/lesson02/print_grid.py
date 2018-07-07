def print_grid(size, cell):
    """ Prints a grid with the given size (rows / columns) and cell size """
    rowStr = ("+" + (" -" * cell) + " ") * size + "+"
    colStr = ("|" + (2 * cell * " ") + " ") * size + "|"

    print(rowStr)
    for i in range(size):
        for j in range(cell):
            print(colStr)
        print(rowStr)
