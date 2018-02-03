# -------------------------------------------#
# Student:   Tri Nguyen
# Instructor: Natasha Aleksandrova
# Date:  01-Feb-2018
# -------------------------------------------#

# Declare variables
plus = '+'
minus = '-'
space = ' '
pipe = '|'

# Part 1:
# Write a function that draws a grid like below:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +


def print_grid_p1():
    ''' This function will print a grid like the one above '''

    # this will print the plus and minus signs
    print(plus + 4*(space + minus) + space + plus + 4*(space + minus) + space + plus)

    for row in range(4):
        # spaces between the pipes are calculated as follows
        # spaces = (len('+ - - - - + - - - - +') - 3) / 2
        # spaces = 9

        print(pipe + 9*space + pipe + 9*space + pipe)

    print(plus + 4*(space + minus) + space + plus + 4*(space + minus) + space + plus)

    for row in range(4):
        print(pipe + 9*space + pipe + 9*space + pipe)

    print(plus + 4*(space + minus) + space + plus + 4*(space + minus) + space + plus)


# Part 2:
# Write a function that takes one integer argument and
# prints a grid just like above, but the size of the grid is given
# by the argument

def print_grid_p2(n):
    ''' This function takes an int argument
        and prints a grid
    '''
    if n % 2 == 0:
        # have to do this because if an even integer is provided
        # the grid will be crooked
        n = n + 1
        dashes = int((n / 2) - 0.5)
    else:
        dashes = int((n / 2) - 0.5)

    def print_plus_minus():
        ''' This function will print plus and minus'''
        print(plus + dashes*(space + minus) + space + plus + dashes*(space + minus) + space + plus)

    def print_pipes_spaces():
        ''' This function will print pipes and spaces between '''
        for row in range(dashes):
            print(pipe + n*space + pipe + n*space + pipe)

    for i in range(2):
        print_plus_minus()
        for j in range(1):
            print_pipes_spaces()
    print_plus_minus()


# Part 3:
# Write a function that draws similar grid with a specified
# number of rows and columns, and with each given size

def print_grid_p3(rows_cols, size):
    ''' this function prints rows and columns and the size of the cell '''

    for row_col in range(rows_cols):
        # print the plus and minus
        print((plus + (space + minus)*size + space) * rows_cols + plus)
        for unit in range(size):
            # print the pipe and spaces between pipe
            print((pipe + space * (2*size + 1))*rows_cols + pipe)
    # print the last plus minus
    print((plus + (space + minus)*size + space) * rows_cols + plus)

# Presentation

print('Part 1 - print_grid_p1() will print the below' + '\n')
print_grid_p1()

print('\n' + 'Part 2 - print_grid_p2(3) or print_grid_p2(5) will print the below' + '\n')
print_grid_p2(3)
print()
print_grid_p2(5)

print('\n' + 'Part 3 - print_grid_p3(3,4) or print_grid_p3(5,3) will print the below')
print()
print_grid_p3(3, 4)
print()
print_grid_p3(5, 3)
