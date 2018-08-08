# grid square corner character
corner = "+"

# grid horizontal and vertical edge characters
horiz = "-"
vert = "|"

# grid fill character (no fill)
sp = " "

def drawDivider(cellWidth):
    """Return one horizontal divider line for the grid"""
    return corner + cellWidth*horiz + corner + cellWidth*horiz + corner

def drawBlankLine(cellWidth):
    """Return one horizontal inner-cell line for the grid"""
    return vert + cellWidth*sp + vert + cellWidth*sp + vert
	
def printGrid(gridWidth):
    """Draw a 4x4 grid gridWidth spaces wide (rounded to even cell widths)"""
    cellWidth = (gridWidth-1)//2
	
	# draw the top edge
    print(drawDivider(cellWidth))
    
	# draw the upper cell 
    for i in range(cellWidth):
        print(drawBlankLine(cellWidth))
    
	# draw the middle divider 
    print(drawDivider(cellWidth))
    
	# draw the lower cell 
    for i in range(cellWidth):
        print(drawBlankLine(cellWidth))
	
	# draw the bottom edge
    print(drawDivider(cellWidth))

#Let's test some sizes
print("\n10:\n")
printGrid(10)

print("\n15:\n")
printGrid(15)

print("\n3:\n")
printGrid(3)

