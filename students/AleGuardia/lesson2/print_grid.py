# collection of functions to print grids by Alejandro Guardia


def print_grid_std():
    # prints a standard grid, takes no arguments
    q_rows = 11
    joint = "+"
    row_marks = " - "
    colum_marks="|"
    row = joint+row_marks*4+joint+row_marks*4+joint
    colum = colum_marks+" "*12+colum_marks+" "*12+colum_marks
    for i in range(q_rows):
        if i == 0 or i == q_rows//2 or i == q_rows-1:
            print(row)
            print()
            continue
        print(colum)
        print()


print_grid_std()
