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

print('Running function print_grid_p1() produces the grid below.' + '\n')
print_grid_p1()

# Part 2:
# Write a function that takes one integer argument and
# prints a grid just like above, but the size of the grid is given
# by the argument

def print_grid_p2(spaces_between_pipes):
    ''' This function takes an int argument
        and prints a grid
    '''
    if spaces_between_pipes % 2 == 0:
        # have to do this because if an even integer is provided
        # the grid will be crooked
        spaces_between_pipes = spaces_between_pipes + 1
        dashes = int((spaces_between_pipes / 2) - 0.5)
    else:
        dashes = int((spaces_between_pipes / 2) - 0.5)
    
    def print_plus_minus():
        ''' This function will print plus and minus'''
        print(plus + dashes*(space + minus) + space + plus + dashes*(space + minus) + space + plus)
    
    def print_pipes_spaces():
        ''' This function will print pipes and spaces between '''
        for row in range(dashes):
            print(pipe + spaces_between_pipes*space + pipe + spaces_between_pipes*space + pipe)
    
    for i in range(2):
        print_plus_minus()
        for j in range(1):
            print_pipes_spaces()
    print_plus_minus()

print('Running function print_grid_p2() produces the grid below.' + '\n')
print_grid_p2(3)
print_grid_p2(15)
print_grid_p2(5)


# Part 3:
# Write a function that draws similar grid with a specified
# number of rows and columns, and with each given size

def print_grid_p3(rows, columns):
    pass