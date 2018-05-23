'''
    File Name: Grid_Printer.py
    Author: Matt Hudgins
    Date created: 2/18/18
    Date last modified: 2/18/18
    Python Version 3.6.4
'''


def grid(size, multi):
    plus = '+ '
    minus = '- '
    vertical = '| '

    plus_minus_row = (plus + minus * size) * multi + plus
    vertical_bar_row = (vertical + (('  ' * size) + vertical) * multi)
    print(plus_minus_row)
    for i in range(size):
        print((vertical_bar_row + '\n') * size + plus_minus_row)


grid(3, 4)
grid(5, 3)
