# Author: SLammertink
# UW Lesson 2 grid 3 exercise

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
