# function accepts two parameters to adjust grid size and cell size


# defines the bits and bobs
pipe = "|"
dash = " - "
corner = "+"

def print_grid(size, res):
    
    def corners_and_dashes():
        cell_size = size
        grid_size = res
        while grid_size > 0:
            print(corner + dash * cell_size, end="")
            grid_size = grid_size - 1
            if grid_size < 1:
                print(corner)
            else:
                print(" ", end="")

    def pipes():
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
        size_counter = size
        while size_counter > 0:
            pipes()
            size_counter = size_counter - 1
    
    def call_row():
        row_counter = res
        while row_counter > 0:
            call_pipes()
            corners_and_dashes()
            row_counter = row_counter -1    

    corners_and_dashes()
    call_row()
    

    
    
