def printgrid(gridSize,numOfCubes):
    for x in range(0, numOfCubes):
        for y in range(0,gridSize):
            if y == 0:
                print("+ " + "- " * gridSize + "+ ", end="")

            elif y >= 1 and y != gridSize - 1:
                print("- " * gridSize + "+ ", end="")
            else:
                print("- " * gridSize + "+")
        #for y in range(0,numOfCubes):
        #    if x > 0:
        #        if y == 0 or y == gridSize:
        #            print("- " * gridSize + "+", end="")
        #        else:
        #            print(" " * gridSize + "|", end="")
        #if x == gridSize - 1:
        #    print("+ " + "- " * gridSize + "+")
        #if x == gridSize - 1:
        #    print("- " * gridSize + "+")

printgrid(3,3)