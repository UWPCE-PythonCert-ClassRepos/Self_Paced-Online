'''
Brandon Henson
3/31/18
Lesson 2 Part 2
Making a better grid
Brandon added comments 4/1/18
'''
######################################      add a bunch of comments
#create a function with 1 variable from user
def print_grid(n):
######################################      define all the needed characters
# define the plus symbol
    plus = '+'
# define the minus symbol
    minus = '-'
# define the pipe symbol
    pipe = '|'
# define the space symbol
    space = ' '
# number of minus
    numofminus = int(n/2)
# first top of grid
    top1 = space+ plus + minus * numofminus + plus + minus * numofminus + plus
# the other tops
    top = plus + minus*numofminus + plus + minus*numofminus + plus
# mid sections of grid
    middle = pipe + space*numofminus + pipe + space*numofminus + pipe
# printing it all
    print(top1,'\n',middle,'\n',top,'\n',middle,'\n',top)

