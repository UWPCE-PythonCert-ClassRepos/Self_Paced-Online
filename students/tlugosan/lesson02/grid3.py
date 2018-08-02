""" Write a function that draws a grid with a specified number of rows and columns and with each cell a given size.
print_grid2(3,4) results in a 3 by 3 with 4 lines as the cell size  """


def draw_grid3(grid_size, block_size):

    plus_sign = "+"
    bar_sign = "|"
    minus_sign = "-"
    space_sign = " "
    total_length = (grid_size + 1) + (grid_size * block_size)

    for i in range(total_length):
        for j in range(total_length):
            if i % (block_size + 1) == 0:
                if j % (block_size + 1) == 0:
                    print(plus_sign, end=' ')
                else:
                    print(minus_sign, end=' ')
            else:
                if j % (block_size + 1) == 0:
                    print(bar_sign, end=' ')
                else:
                    print(space_sign, end=' ')
        print()


if __name__ == '__main__':

    print("this grid is inside of main")
    draw_grid3(4,2)

# draw_grid3(-1,1)

# draw_grid3(1,0)
# refactor to ensure block_size bigger than 0

# draw_grid3(1,1)

# draw_grid3(0,1)
# refactor to ensure grid_size bigger than 0

# draw_grid3(1,-2)
# block_size must be !=-1
# throws ZeroDivisionError: integer division or modulo by zero
