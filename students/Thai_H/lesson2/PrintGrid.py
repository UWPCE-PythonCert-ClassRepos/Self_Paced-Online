def top_or_bottom(col,size):

    for c in range(col):
        print('+', end = '')
        print( size * (' -'), end = ' ' )
        if c == col-1:
            print ('+')


def sides(col,size):
    for row_of_bar in range(size):
        for c in range(col):
            print ('|' , end = '')
            print ((2*size+1) * (' '), end = '')
            if c == col-1:
                print ('|')



def printgrid(row,col,size):
    # for each row, print top edge, and the side
    for r in range(row):
        top_or_bottom(col,size)
        sides(col,size)
        if r == row-1:
            top_or_bottom(col,size)


##---- print grids of squares
# (row, column, number of chars as size of edge)
# all arguments must be int > zero
printgrid(3, 3, 3)

