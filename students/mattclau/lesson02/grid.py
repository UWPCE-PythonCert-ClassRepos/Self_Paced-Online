corner = '+'
horz = '-'
vert = '|'
space = ' '

def printHoriz(gridSize, sideLen):
    for i in range(gridSize):
        print(corner, (horz+space)*sideLen, end = '')
    print(corner)

def printVert(gridSize, sideLen):
    for i in range(sideLen):
        for i in range(gridSize):
            print(vert, space*sideLen*2, end = '')
        print(vert)

def printGrid(gridSize, SideLen):
    for i in range(gridSize):
        printHoriz(gridSize, SideLen)
        printVert(gridSize, SideLen)
    printHoriz(gridSize, SideLen)

side = input("Length of sides: ")
gridSize = input("Size of grid: ")


printGrid(int(gridSize), int(side))