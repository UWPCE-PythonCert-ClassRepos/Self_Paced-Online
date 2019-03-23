# all answers 


x =  '+ - - - - + - - - - +'
y = '|         |         |'
for i1 in range(2):
    print(x)
    for i2 in range(4):
        print(y)
print(x) 



# second part of UW python homework 2. creates a square of user specified size, rounding down
# to run in ipython, import this file then run part2.print_grid(x)
import math

def print_grid(size):
    rsize = math.floor(size/2)
    x =  '+' + ' -' *rsize + ' +' + ' -' *rsize + ' +'
    y = '|' + '  ' * rsize + ' |' + '  ' *rsize + ' |'
    for i1 in range(2):
        print(x)
        for i2 in range(rsize):
            print(y)
    print(x) 



# third part of UW python homework 2
# function that draws a square grid with a specified number size and units
# print_grid2(3,4)  three rows, three columns, and each grid cell four “units” in size

def print_grid2(size, units):
    x = '+'
    y = '|'
    for j1 in range(size):
        x = x + ' -' * units + ' +'
        y = y + '  ' * units + ' |'

    for i1 in range(size):
        print(x)
        for i2 in range(units):
            print(y)
    print(x) 