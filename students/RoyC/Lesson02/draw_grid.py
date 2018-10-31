def printGrid(cellWidth, gridWidth):
    """Draw a grid gridWidth cells square, each cell cellWidth square """
    dividerLine = gridWidth*("+" + cellWidth*" -" + " ") + "+"
    innerLine = gridWidth*("|" + cellWidth*"  " + " ") + "|"
	
    for i in range(gridWidth):	
        # draw cells with top edges
        print(dividerLine)
        for i in range(cellWidth):
            print(innerLine)
			
    # draw the bottom edge
    print(dividerLine)

if __name__ == "__main__":
    #Let's test some sizes
    print("\n10/4:\n")
    printGrid(10, 4)

    print("\n15/2:\n")
    printGrid(15, 2)

    print("\n3/8:\n")
    printGrid(3, 8)

