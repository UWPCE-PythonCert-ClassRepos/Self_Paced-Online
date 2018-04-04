'''
Brandon Henson
3/31/18
Lesson 2 Part 3
Making an adjustable grid
Brandon added comments 4/1/18
'''
# add comments
# create a function with two variables


def print_grid2(n, v):
    # define the plus symbol
    plus = '+'
# define the minus symbol
    minus = ' - '
# define the pipe symbol
    pipe = '|'
# define the space symbol
    space = '   '
# concatenate the first top line
    top = minus * v + plus
# concatenate the top lines
    top1 = plus + top * n
# concatenate the middle lines
    middle = (pipe + space * v)*n + pipe
# printing the grid
    print(top1)
    for i in range(n):
        for i in range(v):
            print(middle)
        print(top1)
print_grid2(4, 4)
