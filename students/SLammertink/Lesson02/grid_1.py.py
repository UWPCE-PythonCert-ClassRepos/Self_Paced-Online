# Author: SLammertink
# UW Lesson 02 Grid printer excercise
# run as python grid.py

def easy_grid():
    ''' This function will print a four by four grid '''
    plus = '+'
    minus = ' - '
    vert = '|'
    spaces = '   '
    hor_line = (plus + ( 4 * minus) + plus + (4 * minus) + plus)
    vert_line = (vert + (4 * spaces) + vert + (4 * spaces) + vert)
    print(hor_line)
    for i in range(1, 4):
        print(vert_line)
    print(hor_line)
    for i in range(1, 4):
        print(vert_line)
    print(hor_line)


