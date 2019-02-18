
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



if __name__ == "__main__":
    print('Lesson 2: Grid Exercise')
    print('Lesson 2: Grid Exercise, Part 1 - a grid with no inputs')
    print(grid_no_inputs())