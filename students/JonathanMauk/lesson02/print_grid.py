def print_grid():  # manual/static values version
    print("+" + " -" * 4 + " +" + " -" * 4 + " +")
    print("|" + " " * 9 + "|" + " " * 9 + "|")
    print("|" + " " * 9 + "|" + " " * 9 + "|")
    print("|" + " " * 9 + "|" + " " * 9 + "|")
    print("|" + " " * 9 + "|" + " " * 9 + "|")
    print("+" + " -" * 4 + " +" + " -" * 4 + " +")
    print("|" + " " * 9 + "|" + " " * 9 + "|")
    print("|" + " " * 9 + "|" + " " * 9 + "|")
    print("|" + " " * 9 + "|" + " " * 9 + "|")
    print("|" + " " * 9 + "|" + " " * 9 + "|")
    print("+" + " -" * 4 + " +" + " -" * 4 + " +")


def print_grid2(n):  # single parameter version
    borders = n // 2
    # uses assignment's formatting if number entered is odd
    if n % 2 != 0:
        print("+" + (" -" * borders) + " +" + (" -" * borders) + " +")
        for i in range(borders):
            print("|" + (" " * n) + "|" + (" " * n) + "|")
        print("+" + (" -" * borders) + " +" + (" -" * borders) + " +")
        for i in range(borders):
            print("|" + (" " * n) + "|" + (" " * n) + "|")
        print("+" + (" -" * borders) + " +" + (" -" * borders) + " +")
    # adjusts formatting for even, removing a plus sign and space
    else:
        print("+" + (" -" * borders * 2) + " +")
        for i in range(borders):
            print("|" + (" " * n) + "|" + (" " * n) + "|")
        print("+" + (" -" * borders * 2) + " +")
        for i in range(borders):
            print("|" + (" " * n) + "|" + (" " * n) + "|")
        print("+" + (" -" * borders * 2) + " +")


def print_grid3(rc, s):  # two parameter version, rc = rows and columns, s = size of cells
    cell_space = s * 2 + 1
    for i in range(rc):
        print("+" + ((" -" * s) + " +") * rc)
        for i in range(s):
            print("|" + ((" " * cell_space) + "|") * rc)
    print("+" + ((" -" * s) + " +") * rc)
