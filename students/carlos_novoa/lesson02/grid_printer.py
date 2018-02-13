#!/usr/bin/env python

"""
Lesson2, Grid Printer Exercise
"""

# ::::: Part 1 ::::: #


def part1():
    """
    static 8 unit grid
    """
    r_a = '+ - - - - + - - - - +'
    r_b = '|         |         |'
    count = 0
    while count < 11:
        if (count == 0 or count % 5 == 0):
            print(r_a)
        else:
            print(r_b)
        count += 1


# ::::: Part2 ::::: #


def part2(n):
    """
    dynamic grid with single argument
    """
    if (n == 1):
        return False
    grid_size = 2  # 2x2 default size from lesson examples
    hw_ratio = 1 / 2  # row height to unit width ratio
    """
    Round odd units down to
    maintain uniformity of spaces/dashes,
    like print_grid(3) and print_grid(15)
    lesson examples
    """
    inner_width = n - 1 if n % 2 == 0 else n
    inner_height = int(hw_ratio * n)
    borders_num = grid_size + 1
    total_width = inner_width * grid_size + borders_num
    total_height = inner_height * grid_size + borders_num

    # make rows string
    row = ''
    for i in range(total_width):
        if (i == 0 or i == total_width - 1):
            # left and right borders
            row += '+'
        elif(i == int(total_width / 2)):
            # center border
            row += '+'
        elif(i % 2 == 0):
            # inner units (even)
            row += '-'
        else:
            # inner units (odd)
            row += ' '

    # make columns string
    col = ''
    for i in range(total_width):
        if (i == 0 or i == total_width - 1):
            # left and right borders
            col += '|'
        elif(i == int(total_width / 2)):
            # center border
            col += '|'
        else:
            # inner units
            col += ' '

    # output grid
    for i in range(total_height):
        if (i == 0):
            # top border
            print(row)
        elif (i == int(total_height / 2)):
            # middle border
            print(row)
        elif (i == total_height - 1):
            # bottom border
            print(row)
        else:
            # columns
            print(col)


# ::::: Part2 ::::: #


def part3(xy, u):
    borders_num = xy + 1
    inner_width = u * 2 + 1
    total_height = xy * u + borders_num
    row_inner = ''
    col_inner = ''

    # make inner string
    for i in range(1, inner_width + 1):
        col_inner += ' '
        if (i % 2 == 0):
            row_inner += '-'
        else:
            row_inner += ' '

    # make rows string
    row = ''
    for i in range(borders_num):
        if (i == borders_num - 1):
            row += '+'
        else:
            row += '+' + row_inner

    # make cols string
    col = ''
    for i in range(borders_num):
        if (i == borders_num - 1):
            col += '|'
        else:
            col += '|' + col_inner

    # output grid
    for i in range(total_height):
        if (i == 0 or i == total_height + 1):
            print(row)
        elif (i % (u + 1) == 0):
            print(row)
        else:
            print(col)
