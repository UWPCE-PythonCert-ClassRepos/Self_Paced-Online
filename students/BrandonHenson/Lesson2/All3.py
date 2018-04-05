'''
Brandon Henson
3/31/18
Lesson 2 Part 1
Making a grid
Brandon ChangedFunGrid to fun_grid 4/1/18
'''

def fun_grid():
################################      define a bunch of characters that are used          ##########################
 #plus symbol used in the tops    
	plus = '+'
 #minus symbol used in the tops
	minus = '-'
 #line symbol used for the columns
	pipe = '|'
 #space used everywhere   
	space = ' '
 #concatenated symbols to make the horizontal "tops" as I call them   
	horiz = plus + minus*4 + plus + minus*4 + plus
 #concatenated symbols to make the sides   
	vert = pipe + space*4 + pipe + space*4 + pipe
 #print our grid
	print(horiz)
    print(vert)
    print(vert)
    print(vert)
    print(vert)
    print(horiz)
    print(vert)
    print(vert)
    print(vert)
    print(vert)
    print(horiz)
#call the function
fun_grid()


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


	
	
	
	'''
Brandon Henson
3/31/18
Lesson 2 Part 3
Making an adjustable grid
Brandon added comments 4/1/18
'''
################################            add comments
# create a function with two variables
def print_grid2(n, v):
######################################      define all the needed characters
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
print_grid2(4,4)