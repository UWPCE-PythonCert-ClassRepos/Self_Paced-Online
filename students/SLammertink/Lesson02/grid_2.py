# Author: SLammertink
# Exercise 2_1
# run python grid_2.py

def grid_2(spaces):
    ''' This function will print a simple grid defined by the input spaces '''
    plus = '+'
    minus = ' - '
    vert = '|'
    space = '   '
    spaces = spaces // 2
    hor_line = (plus + ( spaces * minus) + plus + (spaces * minus) + plus)
    vert_line = (vert + (spaces * space) + vert + (spaces * space) + vert)
    print(hor_line)
    for i in range( spaces):
        print(vert_line)
    print(hor_line)
    for i in range(spaces):
        print(vert_line)
    print(hor_line)
