#part 1 write a function that draws a grid

def print_grid1():
    hrzntl = ("+" + "-" * 4) * 2 + "+"
    vrtcl = ("|" + " "*4) * 2 + "|"
    print(hrzntl)
    print(vrtcl)
    print(vrtcl)
    print(vrtcl)
    print(vrtcl)
    print(hrzntl)
    print(vrtcl)
    print(vrtcl)
    print(vrtcl)
    print(vrtcl)
    print(hrzntl)
 
print("part 1")
print_grid1()

#part 2 write a function to make it an variable size

def print_grid2(n):
    hrzntl = ("+" + "-" * n) * (n) + "+\n"
    vrtcl = ("|" + " " *n) * (n) + "|\n"
    grid2 = (hrzntl + vrtcl * n) * (n) + hrzntl
    print(grid2)
    
print("part 2")
print_grid2(2)

#part 3 write a function to make it variable by row/col and unit size
def print_grid3(rowcol,unit):
    hrzntl = ("+" + "-" * unit) * rowcol + "+\n"
    vrtcl = ("|" + " " * unit) * rowcol + "|\n"
    grid3 = (hrzntl + vrtcl * rowcol) * rowcol + hrzntl
    print(grid3)

print("part 3")
print_grid3(3,6)