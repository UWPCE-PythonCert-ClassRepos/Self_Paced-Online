def grid_one(size):
    plus = ("+ " + "- " * (size//2)) * 2 + "+"  # make a generic top/bottom of cells
    vert = ("|" + " " * size) * 2 + "|"  # make a generic side of cells
    print(plus)  # print top of cells
    for i in range(size//2):  # print sides of cells
        print(vert)
    print(plus)  # print top/bottom of cells
    for i in range(size//2):  # print sides of cells
        print(vert)
    print(plus)  # print bottom of cells


def grid_two(col, cell):
    plus = ("+ " + "- " * cell) * col + "+"  # generic cell top/bottom
    vert = ("|" + " " * (cell*2+1)) * col + "|"  # generic cell side
    for i in range(col):  # loop to print however many rows of cells were specified
        print(plus)
        for x in range(cell):  # loop to make sides of cells as large as specified
            print(vert)
    print(plus)

