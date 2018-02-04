'''
elmar_m / 22e88@mailbox.org
-------------------------------
Lesson02: Grid Printer Exercise
'''

'''
Part 1:
Hardcoded and primitive, executed once when 
module is imported or file is executed doing a
"python grid_printer.py".
'''
a_line_hardcoded = '+' + '----' + '+' + '----' + '+'
b_line_hardcoded = '|' + '    ' + '|' + '    ' + '|'

print(a_line_hardcoded)

for z in range(2):
    for i in range(4):
        print(b_line_hardcoded)
    print(a_line_hardcoded)

'''
Part 2:
A function with one argument. Recycling my function
from part 3 by removing the second function argument
and instead putting it hardcoded into the function body.
'''
def gprint_single(number):
    '''
    print a grid with <number> rows and
    columns a fixed size for width and height.
    '''
    unit = 4

    a_part = '+' + unit * '-'
    b_part = '|' + unit * ' '

    a_full = number * a_part + '+'
    b_full = number * b_part + '|'

    print(a_full)

    for n in range(number):
        for i in range(unit):
            print(b_full)
        print(a_full)

'''
Part 3:
'''
def gprint(number, unit):
    '''
    print a grid with <number> rows and
    columns and <unit> width and height.
    '''

    a_part = '+' + unit * '-'
    b_part = '|' + unit * ' '

    a_full = number * a_part + '+'
    b_full = number * b_part + '|'

    print(a_full)

    for n in range(number):
        for i in range(unit):
            print(b_full)
        print(a_full)

if __name__ == '__main__':
    print('i wanna be a module, please import me!')
