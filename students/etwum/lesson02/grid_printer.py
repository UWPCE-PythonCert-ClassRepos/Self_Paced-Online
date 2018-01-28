def print_grid(size, units):
    #columns
    if size == 1:
        print('+' + '-'*units + '+')
    else:
        print(('+' + '-' * units + '+') +('-' * units + '+')* (size-1))

    #rows


while(True):
    boolInput = False
    while boolInput != True:
        try:
            x = int(input('Please enter a number to determine the rows and column in the grid: '))
            y = int(input('Please enter a number to determine the the unit size: '))
        except (ValueError) as b:
            print('Please numbers only')
            print()
        else:
            boolInput = True

    print_grid(x,y)
    exit = input('Would you like exit ')
    if exit.lower() == 'y':
        break
    else:
        continue