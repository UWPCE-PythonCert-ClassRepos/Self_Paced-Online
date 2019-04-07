#Grid Printer

def print_beam(col, size):
    plus = "+ "
    minus = "- "

    print(plus, end="")
    for line in range(col-1):
        print(minus * size +  plus, end="")
    print(minus * size +  plus)

def print_post(col, size):
    post = "| "
    space = "  "

    print(post, end="")
    for line in range(col-1):
        print(space * size +  post, end="")
    print(space * size +  post)
    
def print_grid(col, size):
    """
    col: columns/rows
    size: size of each box
    """
    print_beam(col, size) #Print initial beam
    for line in range(col): 
        for line in range(size):
            print_post(col, size) #Prints posts in for loop based on number of col/rows
        print_beam(col,size) 

def main():
    print("2 x 2 Grid, Size 4 Box:")
    print_grid(2,4)
    print()
    print("3 x 3 Grid, Size 4 Box:")
    print_grid(3,4)
    print()
    print("5 x 5 Grid, Size 3 Box:")
    print_grid(5,3)
        
if __name__ == "__main__":
    main()

