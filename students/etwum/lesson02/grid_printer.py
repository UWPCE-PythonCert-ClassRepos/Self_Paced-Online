def print_grid(size, units):
    print('+' + '-'*units)


while(True):

    x = int(input('Please enter a number to determine the rows and column in the grid'))
    y = int(input('Please enter the unit size'))

    print_grid(x,y)
    exit = input('Would you like exit ')
    if exit.lower() == 'y':
        break
    else:
        continue