def printgrid(gridSize,cubesXY):
    for x in range(0, cubesXY):
        for y in range(0,gridSize):
            if y == 0:
                if cubesXY == 1:
                    print("+ " + "- " * gridSize + "+ ")
                if cubesXY > 1:
                    if x == 0:
                        print("+ " + "- " * gridSize + "+ ", end="")
                    elif x < cubesXY - 1:
                        print("- " * gridSize + "+", end="")
                    else:
                        print("- " * gridSize + "+")

            if y != 0 or y != gridSize -1 or gridSize == 1:
                if cubesXY == 1:
                    print("| " + "  " * gridSize + "| ")
                if cubesXY > 1:
                    print(" " * gridSize + "| ", end="")


            if y == gridSize - 1:
                if cubesXY == 1:
                    print("+ " + "- " * gridSize + "+ ")
                if cubesXY > 1:
                    print("- " * gridSize + "+ ", end="")




printgrid(1,2)