def print_grid(size, units):
    # this function is used to print a grid based on size and unit parameters


    if size == 1:

        # column
        print('+' + ' - ' * units + '+')
        #row
        print(((("|" + "   " * units + "|") * (size) + "\n") * (units) +
               ('+' + ' - ' * units + '+') * (size) + "\n") * (size))

    else:

        # columns
        print(('+' + ' - ' * units + '+') +(' - ' * units + '+')* (size-1))

        #rows
        print(((("|" + "   "*units + "|") + ("   " * units + '|')*(size-1)+"\n")*(units) +
        ('+' + ' - ' * units + '+') + (' - ' * units + '+') * (size - 1) + "\n")*(size))


while(True):
    # get user input for the size and units of the grid or exit the program
    boolInput = False
    while boolInput != True:
        try:
            x = int(input('Please enter a number to determine the rows and column in the grid: '))
            y = int(input('Please enter a number to determine the the unit size: '))
        except (ValueError) as b:
            print('Please input numbers only')
            print()
        else:
            boolInput = True

    print_grid(x,y)
    exit_program = input('Would you like to exit (y or n)')
    if exit_program.lower() == 'y':
        break
    else:
        continue
        print()