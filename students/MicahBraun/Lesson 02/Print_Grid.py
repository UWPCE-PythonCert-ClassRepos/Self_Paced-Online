# ------------------------------------------------------------------------
# NAME:        MICAH BRAUN
# PROJECT:     Print_Grid.py
# PURPOSE:     Write a Function that prints out a grid
# DATE:        05/02/2018
#
# DESCRIPTION: Function to take in input from user describing aspect(s) of
#              grid and then prints out the grid to the user in the termin-
#              -al.
#
# ------------------------------------------------------------------------

# Processing -------------------------------------------------------------

#  ----  PART II  ----
def simple_grid_print(grid):

    # Algorithm based upon paper criteria
    rows = grid + 2             # "rows" are equal to the grid value entered plus 2 ('+')
    cols = (grid * 2) + 3       # "columns" are equals to # rows * 2 + 3 ('+)


    if grid % 2 == 0:           # If grid entry is even (it will end up making
        rows += 1               # the square uneven, so increase number of rows by 1
                                # now grid is technically uneven

    for row in range(rows):     # for each item in number of items(rows)

        for col in range(cols): # for each item in number of items(columns)

            if row == 0 or row == int(rows/2) or row == rows -1:    # if item is beginning, middle or end

                # --  Formatting beam structure  -- #

                if col == 0:                        # beginning, print '+' no '\n'
                    print('+', end='')
                elif col == cols -1:                # end, print '+'
                    print('+')
                elif int(cols/2) == col:            # middle:
                    if grid % 2 == 0:               # if grid is even, pad '+' with ' '
                        print(' + ', end='')        # if grid is uneven, no padding
                    else:                           # print '+' no '\n'
                        print('+', end='')
                elif col % 2 == 0:                  # if col item is an even number
                    print('-', end='')              # print '-' with no '\n'

                else:                               # else if col item is uneven item num
                    print(' ', end='')              # print ' ' no '\n'

            else:

                # --  Formatting line structure  -- #

                if col == 0:                        # if column is at starting position 0
                    print('|', end='')              # print '|' no '\n'
                elif col == int(cols/2):            # if column is at middle pos
                    if grid % 2 == 0:               # print '|' no '\n'
                        print(' | ', end='')        # (has padding if grid is even or not)
                    else:
                        print('|', end='')
                elif col == cols -1:                # if column is at end position of grid
                    print("|")                      # print '|'

                else:
                    print(' ', end='')              # all other circumstances, print ' ' no '\n'
#  ----  PART III  ----
def print_grid(area, unit):
    for row in range(area):                           # for number of items in area (x, y)
        print(("+ " + "- " * unit) * area + "+")      # print(('+ - ' * y) * x + '+')
        for dash in range(unit):                      # for number of items in unit y (x, y)
            print(("| " + "  " * unit) * area + "|")  # print(('|  ' * y) * x + '|')
    print(("+ " + "- " * unit) * area + "+")          # print ending line


# Display -------------------------------------------------------------------
print("Simple Grid: ")                                # format output
simple_grid_print(3)
print('\n' * 2)
print("Complex Grid: ")
print_grid(3, 5)
