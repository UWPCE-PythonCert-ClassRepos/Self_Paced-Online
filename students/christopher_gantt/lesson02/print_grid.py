def grid_one():
    print("+ - - - - + - - - - +")
    print("|         |         |")
    print("|         |         |")
    print("|         |         |")
    print("|         |         |")
    print("+ - - - - + - - - - +")
    print("|         |         |")
    print("|         |         |")
    print("|         |         |")
    print("|         |         |")
    print("+ - - - - + - - - - +")


def print_grid(n = 8):
    print('+' + ' -'*(n//2) + ' +' + ' -'*(n//2) + ' +')

    for number in range(n//2):
        print('|' + '  '*(n//2) + ' |' + '  '*(n//2) + ' |')
    
    print('+' + ' -'*(n//2) + ' +' + ' -'*(n//2) + ' +')
    
    for number in range(n//2):
        print('|' + '  '*(n//2) + ' |' + '  '*(n//2) + ' |')
    
    print('+' + ' -'*(n//2) + ' +' + ' -'*(n//2) + ' +')



def print_grid2(rows_columns = 3, cell_units = 3):
    print('+' + ((' -'*cell_units + ' +')*rows_columns))

    for num in range(rows_columns):
        for number in range(cell_units):
            print('|' + (('  '*cell_units + ' |')*rows_columns))
        print('+' + ((' -'*cell_units + ' +')*rows_columns))



print_grid()
print_grid2(5,2)












