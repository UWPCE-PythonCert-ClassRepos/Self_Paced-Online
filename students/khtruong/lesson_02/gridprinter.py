"""Example module docstrings text"""


def print_grid(grid_dimension=1, grid_size=1):
    """Return a specified grid dimension with specified grid size."""

    if grid_dimension < 1:
        grid_dimension = 1
    else:
        grid_dimension = int(round(grid_dimension))

    if grid_size < 1:
        grid_size = 1
    else:
        grid_size = int(round(grid_size))

    # initializing variables
    plus = '+'
    minus = '-'
    line = '|'
    space = ' '
    major = ''
    minor = ''

    # creating horizonal major with '+' & '-', and horizonal minor with '|'
    for i in range(0, grid_dimension):
        minusnspace = minus + space
        major = major + plus + space + (minusnspace * grid_size)
        minor = minor + line + space + (2 * grid_size * space)

    major = major + plus
    minor = minor + line

    # looping to print major and minor
    for i in range(0, grid_dimension):
        print(major)
        for j in range(0, grid_size):
            print(minor)

    print(major)
    return
