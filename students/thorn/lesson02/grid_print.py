'''
Thomas Horn
Exercise for Lesson 2 - Part 1 (Grid)
'''

def main():
    part_1()
    part_2(8)
    part_3(5, 6)


def part_1():
    """  Prints a 2x2 grid of 4x4 squares. """
    # Building blocks of the grid.
    vert = '|'
    flat = ' - '
    corner = '+'
    empty = ' '
    flat_row = (corner + (flat * 4) + corner + (flat * 4) + corner + "\n")
    vert_row = (vert + (empty * 12) + vert + (empty * 12) + vert + "\n")*4

    print(flat_row + vert_row + flat_row + vert_row + flat_row)


def part_2(size):
    """  Takes in an int parameter and prints a grid with that size. """
    # Building blocks of the grid.
    try:
        vert = '|'
        flat = ' - '
        corner = '+'
        empty = ' '
        flat_row = (corner + (flat * size) + corner + 
                   (flat * size) + corner + "\n")

        vert_row = (vert + (empty * (size*3)) + vert + 
                   (empty*(size*3)) + vert + "\n")*size
        
        print(flat_row + vert_row + flat_row + vert_row + flat_row)
    except TypeError:
        print("Please enter an integer.")


def part_3(grid_size, side_length):
    """ Creates a grid of variables column/rows and side lengths. """
    vert = '|'
    flat = ' - '
    corner = '+'
    empty = ' '

    # Create vars for each horizontal and vertical line.
    lines_per_side = grid_size
    units_per_segment =  side_length

    lines = ((corner + (flat*units_per_segment)) * lines_per_side + corner)
    vert_line = vert + (empty * (side_length*3))

    # Loop through the number of lines and fill in the vertical lines each time.
    for i in range(lines_per_side):
        print(lines)
        for i in range(side_length):
            print(vert_line*side_length)
    print(lines)
    






if __name__ == "__main__":
    main()  
