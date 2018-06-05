def pS(x):  # printSign
    print(x + " ", end="")
    return


def print_grid2(gDimension = 3, gSize = 4):
    gSize = gSize + 1  # adds to gSize based on images on assignment page
    for row in range(0, (gSize) * (gDimension) + 1):  # controls the row you are on
        if row % (gSize) == 0:  # 0th, gSize, gSize*2, etc
            for col in range(0, (gSize) * (gDimension) + 1):  # writes the symbols in columns
                if col % gSize == 0:
                    pS("+")
                else:  # all other columns
                    pS("-")
                if col == gSize * gDimension:
                    print()
        else:  # i.e. all other rows
            for col in range(0, gSize * gDimension + 1):
                if col % gSize == 0:
                    pS("|")
                else:
                    pS(" ")
                if col == gSize * gDimension:
                    print()


print_grid2()
