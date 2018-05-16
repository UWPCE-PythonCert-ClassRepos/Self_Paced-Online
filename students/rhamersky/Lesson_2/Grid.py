# Description: This program will create a grid.
# Developer: Ryan Hamersky
# Date: 04/29/2018
# Rev: A - 05/15/2018 add comment to the code.

# -----Data Section-----

# -----Process Section-----

def row(row, units):
    '''
    Creates a row (+ & -) for the grid.
    :param row: How many rows the user would like for the grid.
    :param units: The width of the columns.
    :return: Returns gridrow which is a row of + and -.
    '''
    gridrow = "+ "
    for row in range(0, row):
        for unit in range(0, units):
            gridrow = gridrow + "- "
        gridrow = gridrow + "+ "
    return gridrow

def column(column, units_pipe):
    '''
    Creates the column edges with the pipe "|" character.
    :param column: How many columns the user would like for the grid.
    :param units_pipe: The width of the columns.
    :return: Returns gridcolumn which is a column edge using the pipe "|" character.
    '''
    gridcolumn = "|"
    for column in range(0, column):
        for unit in range(0, units_pipe * 2 + 1):
            gridcolumn = gridcolumn + " "
        gridcolumn = gridcolumn + "|"
    return gridcolumn


# -----Presentation Section-----

if __name__ == '__main__':

    # User input
    intRowCloumn = int(input("How many rows and columns for your grid? "))
    intUnits = int(input("How many units for your grid cell? "))

    # Creates grid without the bottom row.
    for i in range(0, intRowCloumn):
        print(row(intRowCloumn, intUnits))
        for j in range(0, intUnits):
            print(column(intRowCloumn, intUnits))

    # Prints bottom row to complete grid
    print(row(intRowCloumn, intUnits))