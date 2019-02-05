# Problem 1
def createGrid1():
    # Assign variables to the only two lines that appear in the grid.
    one = "\n+ - - - - + - - - - +"
    two = "\n|         |         |"

    # Print the grid based on the desired pattern.
    print(one, two*4, one, two*4, one)

createGrid1()

# Problem 2
def createGrid2(n):
    # Calculate the integer length to make each section of the grid.
    num = n//2
    one = "\n+" + " - "*num + "+" + " - "*num + "+"
    two = "\n|" + "   "*num + "|" + "   "*num + "|"

    # Print the grid based on the value created in num variable.
    print(one, two*num, one, two*num, one)

createGrid2(5)

# Problem 3
"""This one was much more difficult than the previous two codes. I had to eliminate the spaces in the "-" so that 
everything would line up properly. I also had to use the end= " " which I avoided in the first two problems. To me,
 the code is broken into three main parts. The first part being the creation of the horizontal lines of the grid,
 the second being the creation of the vertical lines of the grid, and the third being the creation of the final 
 line at the bottom of the grid. """
def createGrid3(grids, length):
    for x in range(grids):
        for y in range(grids):
            print("+", end=" ")
            for z in range(length):
                print("-", end=" ")
        print("+")
        for y in range(length):
            for z in range(grids):
                print("|", end=" ")
                for zz in range(length):
                    print(" ", end=" ")
            print("|")
    for x in range(grids):
        print("+", end=" ")
        for y in range(length):
            print("-", end=" ")
    print("+")

createGrid3(3,4)

