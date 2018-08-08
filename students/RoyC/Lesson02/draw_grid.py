# grid square corner character
corner = "+"

# grid horizontal and vertical edge characters
horiz = "-"
vert = "|"

# grid fill character (no fill)
sp = " "

def drawDivider():
    """Returns one horizontal divider line for the grid"""
    return corner + 4*horiz + corner + 4*horiz + corner

def drawBlankLine():
    """Returns one horizontal inner-cell line for the grid"""
    return vert + 4*sp + vert + 4*sp + vert
	
# Draw the grid!
print(drawDivider())

for i in range(4):
    print(drawBlankLine())

print(drawDivider())

for i in range(4):
    print(drawBlankLine())

print(drawDivider())
