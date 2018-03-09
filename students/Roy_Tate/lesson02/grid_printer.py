# Author: Roy Tate (githubtater)


# PART 1

plus = '+ '
minus = '- '
bar = '| '
space = '  '


def print_basic_grid():
    multiplier = 4
    print(plus + minus * multiplier + plus + minus * multiplier + plus)
    for x in range(1, multiplier + 1):
        print(bar + space * multiplier + bar + space * multiplier + bar)
    print(plus + minus * multiplier + plus + minus * multiplier + plus)

    for x in range(1, multiplier + 1):
        print(bar + space * multiplier + bar + space * multiplier + bar)
    print(plus + minus * multiplier + plus + minus * multiplier + plus)


print_basic_grid()


# PART 2

def print_grid_with_variable(multiplier):
    print(plus + minus * multiplier + plus + minus * multiplier + plus)

    for x in range(1, multiplier + 1):
        print(bar + space * multiplier + bar + space * multiplier + bar)
    print(plus + minus * multiplier + plus + minus * multiplier + plus)

    for x in range(1, multiplier + 1):
        print(bar + space * multiplier + bar + space * multiplier + bar)

    print(plus + minus * multiplier + plus + minus * multiplier + plus)


print_grid_with_variable(3)


# PART 3


def print_grid_two_variables(var1, var2):
    '''Prints a grid that is var1 x var1 in size. The size of the individual cells are based on var2'''
    horiz_string = plus + minus * var2
    vert_string = bar + space * var2
    for x in range(0, var1):
        print(horiz_string * var1 + plus)
        for y in range(0, var2):
            print(vert_string * var1 + bar)
    print(horiz_string * var1 + plus)


print_grid_two_variables(7,2)

































































# author: githubtater