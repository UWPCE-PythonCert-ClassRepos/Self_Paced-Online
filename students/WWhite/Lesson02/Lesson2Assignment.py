def print_grid():

    # -------------------------------------#
    # Desc: Function to create a simple 2x2 unit grid
    # Dev: Will White
    # Date: 3/24/2018
    # ChangeLog: (When,Who,What)
    # -------------------------------------#

    plus = '+'  # Variable for plus signs
    minus = '-'  # Variable for minus signs
    line = '|'  # Variable for vertical lines

    boxTopEdge = (" " + minus)*4 + " "  #
    boxTop = (plus + boxTopEdge) * 2 + plus

    for i in range(0, 2):
        print(boxTop)  # Prints the top and middle rows
        for j in range(0, 4):
            print((line + " " * 9) * 2 + line)  # Prints the rows with open space
    print(boxTop)  # Prints the final bottom row



def print_grid1(size):

    # -------------------------------------#
    # Desc: Function to create a 2x2 unit grid that varies in size
    # Dev: Will White
    # Date: 3/24/2018
    # ChangeLog: (When,Who,What)
    # -------------------------------------#

    plus = '+'  # Variable for plus signs
    minus = '-'  # Variable for minus signs
    line = '|'  # Variable for vertical lines

    boxTopEdge = ""  # Empty variable for us to add to
    for i in range(0, size):  # Loop through user input to create section length
        if i % 2 == 0:  # Alternate between spaces and minus signs
            boxTopEdge += " "
        else:
            boxTopEdge += minus

    boxTop = (plus + boxTopEdge) * 2 + plus  # Create row of plus & minus signs

    for i in range(0, 2):
        print(boxTop)  # Prints the top and middle rows
        for j in range(0, size // 2):
            print((line + " " * size) * 2 + line)  # Prints the rows with open space
    print(boxTop)  # Prints the final bottom row


def print_grid2(units,size):

    # -------------------------------------#
    # Desc: Function to create a grid that varies in size and number of units
    # Dev: Will White
    # Date: 3/24/2018
    # ChangeLog: (When,Who,What)
    # -------------------------------------#

    plus = '+'  # Variable for plus signs
    minus = '- '  # Variable for minus signs and space
    line = '| '  # Variable for vertical lines and space

    boxTopEdge = " " + minus*size

    boxTop = (plus + boxTopEdge) * units + plus  # Create row of plus & minus signs

    for i in range(0, units):
        print(boxTop)  # Prints the top and middle rows
        for j in range(0, size):
            print((line + " " * size*2) * units + line)  # Prints the rows with open space
    print(boxTop)  # Prints the final bottom row
