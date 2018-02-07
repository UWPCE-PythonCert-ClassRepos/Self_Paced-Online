def prow(x,y=2):
    """print the horizontal rows"""
    for i in range(y):
        print("+", "- " * x, end = "")
    print("+")

def pcolumn(x,y=2):
    """print the columns"""
    for i in range(y):
        print("|", " " * x, end = "")
    print("|")

def print_grid(x):
    """print a 2x2 grid with squares of size x/2 by x/2"""
    row = int(x/2)
    if x % 2 == 0:
        col = x
    else:
        col = x - 1
    for i in range(2):
        prow(row)
        for i in range(row):
            pcolumn(col)
    prow(row)

def print_grid2(y,z):
    """print a y by y grid with squares of size z by z"""
    for i in range(y):
        prow(z,y)
        for i in range(z):
            pcolumn(z*2,y)
    prow(z,y)