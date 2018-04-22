# ############################################################### 
def test():
    print ("PRINT TEST FUNCTION")
    first_plus = "+"
    plus  = " +"
    minus = " -"
    space = "  "
    first_pipe = "|"
    pipe  = " |"

    # print the top line of the grid
    # + - - - - + - - - - +
    print (first_plus + 4*minus + plus + 4*minus + plus)

    #print the grid body  
    # |         |          |
    # |         |          |
    # |         |          |
    # |         |          |
    for i in range( 4 ): print (first_pipe + 4*space + pipe + 4*space + pipe) 
    
    # print the bottom line of the grids
    # + - - - - + - - - - +
    print (first_plus + 4*minus + plus + 4*minus + plus)


# ############################################################### 
def print_grid( num ):
    func_des = "print_grid({:d})".format(num)
    print (func_des)
    
    size = int( num/2)
    grid_num = 2
    # for each grid in the first column
    for i in range(grid_num): 
        # print a row of horizotal grids
        print_horizontal_line( grid_num, size)
        for j in range(size): print_pipe_line( grid_num, size)
    
    print_horizontal_line( grid_num, size)


# ############################################################### 
def print_grid_2(grid_num, size):
    func_str = "print_grid_2 ({:d}, {:d})".format(grid_num, size)
    print (func_str)
    
    # for each grid in the first column 
    for i in range( grid_num): 
        # print a row of horizotal grids
        print_horizontal_line(grid_num, size)
        for i in range ( size):print_pipe_line( grid_num, size)
    
    # print the bottom line
    print_horizontal_line( grid_num, size)

# ############################################################### 
def print_horizontal_line(rep, size):
    first_plus = "+"
    plus = " +"
    minus= " -"

    print (first_plus, end='') 
    for i1 in range(rep):
        for i2 in range(size):
            print (minus, end='')
        print (plus, end='')
    print()

def print_pipe_line(rep, size):
    first_pipe = "|"
    pipe  = " |"
    
    print( first_pipe, end='')
    for i3 in range( rep): # to count up to grid_num line
        print_space(size)
        print (pipe, end="")
    print()

def print_space( size):
    space = "  "
    for i in range(size):
        print ( space, end='')




if __name__ == "__main__":
    print ("Hello, this is mayc4t hw 2")
    test()
    print_grid( 15)
    print_grid_2( 7, 4)
