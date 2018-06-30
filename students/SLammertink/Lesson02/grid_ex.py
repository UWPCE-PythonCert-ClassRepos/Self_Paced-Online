# Author: SLammertink
# UW Lesson 02 Grid printer excercise
# run as python grid.py
#


def easy_grid():
    ''' This function will print a four by four grid '''
    plus = '+'
    minus = ' - '
    vert = '|'
    spaces = '   '
    hor_line = (plus + ( 4 * minus) + plus + (4 * minus) + plus) # define the hor line
    vert_line = (vert + (4 * spaces) + vert + (4 * spaces) + vert) # define the vert line
    print(hor_line)
    for i in range(1, 5):
        print(vert_line)
    print(hor_line)
    for i in range(1, 5):
        print(vert_line)
    print(hor_line)

# Task 2

def grid_2(spaces):
    ''' This function will print a simple grid defined by the input spaces '''
    plus = '+'
    minus = ' - '
    vert = '|'
    space = '   '
    spaces = spaces // 2 # divide the spaces equally
    hor_line = (plus + ( spaces * minus) + plus + (spaces * minus) + plus)
    vert_line = (vert + (spaces * space) + vert + (spaces * space) + vert)
    print(hor_line)
    for i in range( spaces ):
        print(vert_line)
    print(hor_line)
    for i in range( spaces ):
        print(vert_line)
    print(hor_line)

    # Task 3

    def grid_3(columns, spaces):
    ''' Function to print the width and amount of columns of cells '''
    plus = '+'
    minus = ' - '
    vert = '|'
    space = '   '
    hor_line = (plus + (minus * spaces))
    hor_line_corrected = ((hor_line * columns) + plus)
    vert_line = (vert + space * spaces) * columns + vert
    print(hor_line_corrected)
    for i in range(columns):
        for i in range(spaces):
            print(vert_line)
        print(hor_line_corrected)


