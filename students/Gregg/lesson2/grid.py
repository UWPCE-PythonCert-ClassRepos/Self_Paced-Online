
def grid_no_inputs():
    """Produce a 2x2 grid with sides of length 4"""
    corner = "+ "
    h_side = "- "*4
    h_spacer = " "*8
    v_side = "| "
    edge_row = corner+h_side+corner+h_side+corner
    spacer_row = v_side + h_spacer + v_side +h_spacer + v_side
    row_list = []
    row_list.append(edge_row)
    for i in range(2):
        for i in range(4):
            row_list.append(spacer_row)
        row_list.append(edge_row)
    grid_string = ('\n').join(row_list)
    #print(grid_string) - seems to be more in keeping with a good funciton if
    #I only print it in the script
    return grid_string

def grid2x2(side_length):
    """Produce a 2x2 grid with sides of length side_length"""
    repeats = abs(side_length//2)
    corner = "+ "
    h_side = "- "*repeats
    h_spacer = " "*(repeats*2)
    v_side = "| "
    edge_row = corner+h_side+corner+h_side+corner
    spacer_row = v_side + h_spacer + v_side +h_spacer + v_side
    row_list = []
    row_list.append(edge_row)
    for i in range(2):
        for i in range(repeats):
            row_list.append(spacer_row)
        row_list.append(edge_row)
    grid_string = ('\n').join(row_list)
    #print(grid_string) - seems to be more in keeping with a good funciton if
    #I only print it in the script
    return grid_string


if __name__ == "__main__":
    print('Lesson 2: Grid Exercise')
    print('Lesson 2: Grid Exercise, Part 1 - a grid with no inputs')
    print(grid_no_inputs())
    print('Lesson 2: Grid Exercise, Part 2 - grid side length from input')
    print('With input = 3 - grid2x2(3):')
    print(grid2x2(3))
    print('With input = 15 - grid2x2(15):')
    print(grid2x2(15))