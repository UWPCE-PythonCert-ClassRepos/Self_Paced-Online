def print_grid(size, units):
    # this function is used to print a grid based on size and unit parameters

    if size == 1:
        print('+' + ' - ' * units + '+')
        print(((("|" + "   " * units + "|") * (size) + "\n") * (units) +
               ('+' + ' - ' * units + '+') * (size) + "\n") * (size))

    else:

        # columns

        print(('+' + ' - ' * units + '+') +(' - ' * units + '+')* (size-1))

        print(((("|" + "   "*units + "|") + ("   " * units + '|')*(size-1)+"\n")*(units) +
        ('+' + ' - ' * units + '+') + (' - ' * units + '+') * (size - 1) + "\n")*(size-1))

        print(((("|" + "   " * units + "|") + ("   " * units + '|') * (size - 1) + "\n") * (units) +
               ('+' + ' - ' * units + '+') + (' - ' * units + '+') * (size - 1) + "\n") * (size - 2))

while(True):
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
    exit_game = input('Would you like to exit (y or n)')
    if exit_game.lower() == 'y':
        break
    else:
        continue
        print()