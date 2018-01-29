def print_grid(dimensions, units):
    # this function is used to print a grid based on size and unit parameters

    # if/else used to create a 1x1 grid or any grid larger
    if dimensions == 1:
        # creates 1x1 grid

        # column
        print('+' + ' - ' * units + '+')

        # row
        print(((("|" + "   " * units + "|") * (dimensions) + "\n") * (units) +
               ('+' + ' - ' * units + '+') * (dimensions) + "\n") * (dimensions))

    else:
        # creates a grid bigger than 1x1

        # columns
        print(('+' + ' - ' * units + '+') +(' - ' * units + '+')* (dimensions-1))

        # rows
        print(((("|" + "   "*units + "|") + ("   " * units + '|')*(dimensions-1)+"\n")*(units) +
        ('+' + ' - ' * units + '+') + (' - ' * units + '+') * (dimensions - 1) + "\n")*(dimensions))


while(True):
    # get user input for the size and units of the grid or exit the program

    # boolean used to continue or exit the while loop based on user input
    boolInput = False

    # while loop to get user input
    while boolInput != True:

        # try/except block to catch user inputs other than whole numbers
        try:
            grid_size = int(input('Please enter a number to determine the rows and column in the grid: '))
            unit_size = int(input('Please enter a number to determine the the unit size: '))
        except ValueError as b:
            print('Please input whole numbers only')
            print()
        else:
            boolInput = True

    # run the print grid function
    print_grid(grid_size,unit_size)

    # exit the program or continue the loop
    exit_program = input('Would you like to exit? (y or n) ')
    if exit_program.lower() == 'y':
        break
    else:
        continue
