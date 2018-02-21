# function accepts two parameters to adjust grid size and cell size


# defines symbology for lines and columns
pipe = "|"
dash = " - "
corner = "+"

def print_grid(size, res):
# main function sets the global size
# and resolution parameters for the grid

    def corners_and_dashes():
        # prints the horizontal lines with "corners" and "dashes"
        cell_size = size
        grid_size = res
        # sets size and resolution counters to
        # user's input from main function
        while grid_size > 0:
            print(corner + dash * cell_size, end="")
            grid_size = grid_size - 1
            if grid_size < 1:
                print(corner)
                # ends the string of corners and dashes
            else:
                print(" ", end="")
                # allows the string to continue on the same line

    def pipes():
        # prints the vertical lines with "pipes"
        # uses same method as for the horizontal lines
        cell_size = size
        grid_size = res
        while grid_size > 0:
            print(pipe + "   " * cell_size, end="")
            grid_size = grid_size - 1
            if grid_size < 1:
                print(pipe)
            else:
                print(" ", end="")

    def call_pipes():
        # calls the "pipes" function the appropriate number of times 
        # for each row of cells based on the user-defined cell size
        size_counter = size
        while size_counter > 0:
            pipes()
            size_counter = size_counter - 1
    
    def call_row():
        # calls the "call_pipes" and "corners_and_dashes" functions
        # the appropriate number of times based of the user-defined
        # resolution input
        row_counter = res
        while row_counter > 0:
            call_pipes()
            corners_and_dashes()
            row_counter = row_counter -1    

    corners_and_dashes()
    call_row()
    

    
    
