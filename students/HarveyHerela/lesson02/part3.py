import sys

# Prints a specific row
# Use 'edge' as the corner pieces and middle
# and 'filler' as the filler pieces
def print_row( edge, filler, numCells, cellDim ):
    print( edge, end = ' ')
    for c in range (0, numCells):
        for x in range (0, cellDim):
            print(filler, end = ' ')
        print(edge, end = ' ')
    
    print()

# print_grid2
# param1: number of cells
# param2: dimensions of the cell. cells are squares, so width = height
def print_grid2(numCells, cellDim):
    # Calculate the total lenght of a row
    # Each cell is cellDim high, but that's only the
    # vertical portion. Each cell also has a bottom and top row.
    # However, the bottom of one cell is the top of the next.
    # So the formula is (numCells * (cellDim + 1)) + 1
    rowLen = (numCells * (cellDim + 1)) + 1
    
    # Draw the first row
    print_row('+', '-', numCells, cellDim)
    
    # Now draw each cell
    for c in range (0, numCells):
        for y in range (0,cellDim):
            print_row('|', ' ', numCells, cellDim)
        print_row('+', '-', numCells, cellDim)
    

#get the parameter
if len(sys.argv) < 3:
    print("Missing arguments!")
    exit()

try:
    cells = int(sys.argv[1])
    cellDim = int(sys.argv[2])
    
    if (cells < 1) or (cellDim < 1):
        raise ValueError("Value should be greater than 0")
    print_grid2(cells, cellDim)

except Exception as ex:
    print("Try again with positive integers")
    
print()