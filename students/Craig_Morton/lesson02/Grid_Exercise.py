# ------------------------------------------------- #
# Title: Lesson 2, pt 1/3, Grid Printer Exercise
# Dev:   Craig Morton
# Date:  8/13/2018
# Change Log: CraigM, 8/13/2018, Grid Printer Exercise
#  ------------------------------------------------ #

# Variables

plus = "+ "
minus = "- "
pipe = "| "
space = "  "

# Grid Part One: Simple grid


def print_grid_one():
    """Prints grid without parameter"""
    size = 4
    print(plus + minus * size + plus + minus * size + plus)
    for y in range(1, size + 1):
        print(pipe + space * size + pipe + space * size + pipe)
    print(plus + minus * size + plus + minus * size + plus)

    for y in range(1, size + 1):
        print(pipe + space * size + pipe + space * size + pipe)
    print(plus + minus * size + plus + minus * size + plus)

# Grid Part Two: Grid with one parameter


def print_grid_two(size):
    """Prints grid with one parameter"""
    print(plus + minus * size + plus + minus * size + plus)

    for y in range(1, size + 1):
        print(pipe + space * size + pipe + space * size + pipe)
    print(plus + minus * size + plus + minus * size + plus)

    for y in range(1, size + 1):
        print(pipe + space * size + pipe + space * size + pipe)

    print(plus + minus * size + plus + minus * size + plus)

# Grid Part Three: Grid with two parameters


def print_grid_three(size1, size2):
    """Prints grid with two parameters"""
    row = plus + minus * size2
    column = pipe + space * size2
    for y in range(0, size1):
        print(row * size1 + plus)
        for x in range(0, size2):
            print(column * size1 + pipe)
    print(row * size1 + plus)


print_grid_one()
print_grid_two(10)
print_grid_three(25, 2)
