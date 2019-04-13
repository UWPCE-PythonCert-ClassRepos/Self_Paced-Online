#Grid Printer

def print_beam(col, size):
    """Print a beam or multiple beams in a single line.

    Args:
        col (int): the number of columns for the beam.
        size (int): the number to change the size of the beam.
    Returns: 
        None
    
    """
    
    plus = "+ "
    minus = "- "

    print(plus, end="")
    for line in range(col-1):
        print(minus * size +  plus, end="")
    print(minus * size +  plus)

def print_post(col, size):
    """Print a post or multiple posts in a single line.

    Args:
        col (int): the number of columns for the post.
        size (int): the number to change the size of the post.
    Returns: 
        None

    """
    
    post = "| "
    space = "  "

    print(post, end="")
    for line in range(col-1):
        print(space * size +  post, end="")
    print(space * size +  post)
    
def print_grid(col, size):
    """Print a grid.

    Args:
        col (int): the number of columns/rows for the grid.
        size (int): the number to change the size of the box in a grid.
    Returns: 
        None

    """
    
    print_beam(col, size) #Print initial beam
    for line in range(col): 
        for line in range(size):
            print_post(col, size) #Prints posts in for loop based on number of col/rows
        print_beam(col,size) #Prints the final beam after the printing the post 
        
if __name__ == "__main__": #Run tests
    print("Beam:")
    print_beam(2,3)
    print()
    print("Post:")
    print_post(2,3)
    print()
    print("2 x 2 Grid, Size 4 Box:")
    print_grid(2,4)
    print()
    print("3 x 3 Grid, Size 4 Box:")
    print_grid(3,4)
    print()
    print("5 x 5 Grid, Size 3 Box:")
    print_grid(5,3)
