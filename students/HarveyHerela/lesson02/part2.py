import sys

# Prints a specific row
# Use 'edge' as the corner pieces and middle
# and 'filler' as the filler pieces
def print_row( edge, filler, side ):
    # Special case, side <= 1
    iter = 2
    if side <= 1:
        iter = 1
    # print the left side, then the right side,
    # with an edge in-between
    print(edge, end = ' ')
    for t in range(0, iter):
        half = side // 2
        for x in range(0,half):
            print(filler, end=' ')
        print(edge, end = ' ')
    
    print()

# print_grid
# parameters: 1 parameter for length of side
def print_grid( side ):
    # Print a top row
    print_row('+','-',side)
    
    # Now print an open box, twice
    half = side // 2
    
    # Special case for side <= 1
    iter = 2
    if side <= 1:
        iter = 1
    
    for t in range(0, iter):
        # First, print out the appropriate number
        # of vertical pieces
        for y in range(0,half):
            print_row('|', ' ', side)
        # Now print out the bottom row
        print_row('+','-',side)

#get the parameter
if len(sys.argv) < 2:
    print("Missing arguments!")
    exit()

try:
    num = int(sys.argv[1])
    
    if num < 1:
        raise ValueError("Value should be greater than 0")
    print_grid(num)

except Exception as ex:
    print("Try again with a positive integer")
    
print()