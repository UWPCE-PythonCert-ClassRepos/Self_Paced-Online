# collection of functions to print grids by Alejandro Guardia


def print_grid_std():
    # prints a standard grid, takes no arguments
    q_rows = 11
    joint = "+"
    row_marks = " - "
    column_marks="|"
    row = joint+row_marks*4+joint+row_marks*4+joint
    column = column_marks+" "*12+column_marks+" "*12+column_marks
    for i in range(q_rows):
        if i == 0 or i == q_rows//2 or i == q_rows-1:
            print(row)
            print()
            continue
        print(column)
        print()


print_grid_std()


def print_grid_custom(n):
    # takes a grid size value and prints the grid

    q_marks = (n//2)
    q_rows = q_marks*2 + 3
    joint = "+"
    row_marks = " - "
    column_marks = "|"
    blank = len(row_marks)*q_marks*" "
    row = joint + row_marks * q_marks + joint + row_marks * q_marks + joint
    column = column_marks + blank + column_marks + blank + column_marks
    for i in range(q_rows):
        if i == 0 or i == q_rows // 2 or i == q_rows - 1:
            print(row)
            print()
            continue
        print(column)
        print()


print_grid_custom(3)


def print_grid_custom_two(number, units):
    # takes a grid and column size value and prints the grid

    joint = "+"
    row_marks = " - "
    column_marks = "|"
    blank = len(row_marks)*units*" "
    row = joint + (row_marks*units+joint)*number
    column = column_marks + (blank + column_marks)*number
    for i in range(number):
        print(row)
        print()
        for j in range(units):
            print(column)
            print()
    print(row)


print_grid_custom_two(5,3)