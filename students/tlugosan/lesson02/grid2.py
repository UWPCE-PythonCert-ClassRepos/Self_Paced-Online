#write a function to print a grid whixh takes a parameter that
# defines how big a square is in the grid


def draw_grid2(block_size):
#    block_size = 4
    grid_size = 2
    plus_sign = "+"
    bar_sign = "|"
    minus_sign = "-"
    space_sign = " "
    total_lenght = (grid_size+1) + (grid_size*block_size)

    for i in range(total_lenght):
        for j in range(total_lenght):
            if(i%(block_size+1)==0):
                if(j%(block_size+1)==0):
                    print(plus_sign, end=' ')
                else:
                    print(minus_sign, end=' ')
            else:
                if(j%(block_size+1)==0):
                    print(bar_sign, end=' ')
                else:
                    print(space_sign, end=' ')
        print()


if __name__ == '__main__':

    print("test for drawing a grid")

    # happy past test -> pass
#    draw_grid2(2)

    # test for neg parametrs -> pass
#    draw_grid2(0)

    # test for neg parameters (-1) should throw ZeroDivisionError: integer division or modulo by zero
#    draw_grid2(-1)

    # test for neg parameters -> nothing should be drawn
#    draw_grid2(-2)
